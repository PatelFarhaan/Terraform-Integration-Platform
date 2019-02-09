import json

status_result = None
try:
    status_result = json.loads(open("failure_apply.json", "r").read())['status']
except:
    status_result = json.loads(open("success_apply.json", "r").read())['status']

print(status_result)