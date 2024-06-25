import os
import json

json_file = open("config.json")
server_data = json.load(json_file)

service_list = []

for s in server_data['servers']:
    command = 'systemctl is-active ' + s['service_name']
    service_status = os.system(command)

    if service_status == "active":
        service_list.append({"service": s['name'], "status": "active"})

    if service_status == "inactive":
        service_list.append({"service": s['name'], "status": "inactive"})


print(service_list)