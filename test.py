resp = {
    "CICD_Artifact Bucket": {
        "sensitive": '',
        "type": "string",
        "value": "app1-dev-2-artifact"
    },
    "CICD_Repo HTTP URL": {
        "sensitive": '',
        "type": "string",
        "value": "https://git-codecommit.us-west-2.amazonaws.com/v1/repos/hack2-dev-2"
    },
    "CICD_Repo SSH URL": {
        "sensitive": '',
        "type": "string",
        "value": "ssh://git-codecommit.us-west-2.amazonaws.com/v1/repos/hack2-dev-2"
    },
    "EC2_ELB Public Dns": {
        "sensitive": '',
        "type": "string",
        "value": "hack2-dev-2-elb-377121987.us-west-2.elb.amazonaws.com"
    },
    "EC2_Server Public DNS": {
        "sensitive": false,
        "type": "list",
        "value": [
            "ec2-34-215-119-106.us-west-2.compute.amazonaws.com",
            "ec2-54-218-70-236.us-west-2.compute.amazonaws.com"
        ]
    },
    "RDS_Database Name": {
        "sensitive": false,
        "type": "string",
        "value": "hack2"
    },
    "RDS_Endpoint": {
        "sensitive": false,
        "type": "string",
        "value": "i-1-id.cnstrnkzp2jn.us-west-2.rds.amazonaws.com:3306"
    },
    "RDS_User Name": {
        "sensitive": false,
        "type": "string",
        "value": "abc"
    }
}