import os
import json

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
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
        self.wfile.write(json.dumps(status_list).encode())
        self.send_response(200)



httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
