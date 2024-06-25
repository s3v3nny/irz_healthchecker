import os
import json
import socket

server = socket.socket()
hostname = socket.gethostname()
port = 9090
server.bind((hostname, port))
server.listen(2)

while True:
    con, ip = server.accept()
    json_file = open("config.json")
    json_data = json.load(json_file)

    status_list = []
    for s in json_data['servers']:
        command = 'systemctl is-active ' + s['service_name']
        service_status = os.system(command)

        if service_status == "active":
            status_list.append({'service_name': s['name'], 'status': "active"})

        if service_status == "inactive":
            status_list.append({'service_name': s['name'], 'status': "inactive"})

    json_file.close()
    con.send(json.dumps(status_list).encode())
    con.close()
