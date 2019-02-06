def db_json(rds_eng, ins_type, red_store, rds_user, rds_pass, app_name, rds_env, rds_env_id, location):
    data = {
                "rds_engine":"{}".format(rds_eng),
                "rds_instance":"{}".format(ins_type),
                "rds_storage":"{}".format(red_store),
                "rds_username":"{}".format(rds_user),
                "rds_password":"{}".format(rds_pass),
                "rds_appname":"{}".format(app_name),
                "rds_environment":"{}".format(rds_env),
                "rds_environment_id":"{}".format(rds_env_id)
}

    json_data = json.dumps(data)

    file = open(location+'/rds.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()