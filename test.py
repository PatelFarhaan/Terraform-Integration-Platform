
def dms_json(app_name, env_name, env_id, source_ip, port, username, password, enginename, location):
    data = {
        "dms_appname":"{}".format(app_name),
        "dms_envname":"{}".format(env_name),
        "dms_envid":"{}".format(env_id),
        "dms_src_servername":"{}".format(source_ip),
        "dms_src_port":"{}".format(port),
        "dms_src_username": "{}".format(username),
        "dms_src_password": "{}".format(password),
        "dms_src_enginename": "{}".format(enginename)
    }

    json_data = json.dumps(data)

    file = open(location + '/dms.tfvars.json', 'w')

    for i in json_data:
        file.write(i)

    file.close()