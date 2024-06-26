import http.server
import json
import subprocess


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        json_file = open("config.json")
        json_data = json.load(json_file)
        services = {'services': []}
        for s in json_data['services']:
            command = 'systemctl is-active ' + s['service_name']
            status = subprocess.getoutput(command)

            if status == "active":
                print("active here")
                services['services'].append({'service_name': s['name'],
                                    'status': "active"})

            if status == "inactive":
                print("inactive here")
                services['services'].append({'service_name': s['name'],
                                    'status': "inactive"})
        json_file.close()
        self.wfile.write(json.dumps(services).encode())


httpd = http.server.HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()
