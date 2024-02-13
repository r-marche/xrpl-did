from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        html_content = HTML_TEMPLATE.format(title="XRPL DID", subtitle="test-sottotitolo", background_color="#ffffff")
        
        self.wfile.write(bytes(html_content, "utf8"))
        
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return
