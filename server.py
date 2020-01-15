import http.server
import socketserver
import random

random.seed(a=None)

nomes = list()
with open('nomes.txt') as f:
    for l in f:
        nome = l.strip().lower()
        if nome not in nomes:
            nomes.append(nome)

print("{} nomes na lista".format(len(nomes)))


class NameGenerator(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(bytes(random.choice(nomes), 'utf8'))


handler = NameGenerator

with socketserver.TCPServer(("", 8080), handler) as httpd:
    print("Listening...")
    httpd.serve_forever()
