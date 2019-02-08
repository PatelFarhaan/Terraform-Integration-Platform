#!/bin/bash
#
# terraform-app
#
# This to terraform the servers for the Galleon App

# By storing the date now, we can calculate the duration of provisioning at the
# end of this script.
start_seconds="$(date +%s)"

# get location of current dir
CWD="$(pwd)"
CONFIG=$1
TERRAFORM="terraform"
VERSION="0.11.11"
HOME=/home/ec2-user
SCRIPTS=/home/ec2-user/scripts
LOG=$CONFIG/terraform-app.log
TIMESTAMP=`date "+%Y-%m-%d %H:%M:%S"`

### FUNCTIONS

#
# Abort with <msg>
#

abort() {
  echo
  echo "  $@" 1>&2
  echo
  exit 1
}

#
# Log <msg>.
#

log() {
  echo "  ○ $@" >> $LOG
}

#
# Return the terraform command to run.
#

terraform_command() {
  #local key="`config_get key`"
  #test -n "$key" && local identity="-i $key"
  echo "$TERRAFORM"
}

#
# Run the given terraform <cmd>.
#

run_terraform() {
  cd $CONFIG
  local terraform="`terraform_command`"
  log $TIMESTAMP $terraform $@
  $terraform $@
  if [ $? -ne 0 ]; then
	log  $TIMESTAMP “CRITICAL: Failed.”
	touch $CONFIG/failure_$1.go
  else
	log $TIMESTAMP “Success”
	touch $CONFIG/success_$1.go
  fi
}

init_ec2() {
  #mkdir -p $CONFIG
  cp $SCRIPTS/provider.tf $SCRIPTS/assumerolepolicy.json $SCRIPTS/network.tf $SCRIPTS/ec2_multiple.tf $SCRIPTS/policys3bucket.json $SCRIPTS/variable_ec2.tf $SCRIPTS/output_ec2.tf $CONFIG/
}

init_rds() {
  #mkdir -p $CONFIG
  cp $SCRIPTS/provider.tf $SCRIPTS/assumerolepolicy.json $SCRIPTS/network.tf $SCRIPTS/rds.tf $SCRIPTS/policys3bucket.json $SCRIPTS/variable_rds.tf $SCRIPTS/output_rds.tf $CONFIG/
}

init_cicd() {
  #mkdir -p $CONFIG
  cp $SCRIPTS/provider.tf $SCRIPTS/assumerolepolicy.json $SCRIPTS/network.tf $SCRIPTS/cicd.tf $SCRIPTS/policys3bucket.json $SCRIPTS/variable_cicd.tf $SCRIPTS/outputs_cicd.tf $CONFIG/
}

create_infra() {
  run_purge
  run_terraform get $CONFIG 2>$CONFIG/error_get.log
  run_terraform init $CONFIG 2>$CONFIG/error_init.log
  run_terraform plan -out=tfplan -input=false -var-file=$CONFIG/ec2.tfvars.json -var-file=$CONFIG/rds.tfvars.json -var-file=$CONFIG/cicd.tfvars.json $CONFIG  2>$CONFIG/error_plan.log
  run_terraform apply -input=false  $CONFIG/tfplan 2>$CONFIG/error_apply.log
  run_terraform output -json >> $CONFIG/output.json 2>$CONFIG/error_output.log
}

run_purge() {
  rm -rf $CONFIG/output.json
  rm -rf $CONFIG/success_*.go
  rm -rf $CONFIG/failure_*.go  
}

run_destroy() {
  run_purge
  run_terraform get $CONFIG
  run_terraform destroy -input=false -auto-approve=true -var-file=$CONFIG/rds.tfvars.json -var-file=$CONFIG/ec2.tfvars.json $CONFIG
}

while test $# -ne 0; do
  arg=$2;
echo $arg;
 case $arg in
	ec2) init_ec2 $@; exit ;;
	rds) init_rds $@; exit ;;
	cicd) init_cicd $@; exit;;
	create) create_infra $@; exit ;;
	delete) run_destroy $@; exit ;;
  esac
done


