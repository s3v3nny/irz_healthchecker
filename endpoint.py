import http.server
import json
import os


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        json_file = open("config.json")
        json_data = json.load(json_file)
        status_list = []
        for s in json_data['servers']:
            command = 'systemctl is-active ' + s['service_name']
            service_status = os.system(command)

            if service_status == 1:
                print("active here")
                status_list.append({'service_name': s['name'],
                                    'status': "active"})

            if service_status == 0:
                print("inactive here")
                status_list.append({'service_name': s['name'],
                                    'status': "inactive"})
        json_file.close()
        print(json.dumps(status_list))
        self.wfile.write(json.dumps(status_list).encode())


httpd = http.server.HTTPServer(('', 8080), RequestHandler)
httpd.serve_forever()
