from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>XRPL DID</title>
</head>
<body>
<h1>Titolo</h1>
<h2>Sottotitolo</h2>
</body>
</html>
"""

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        #self.wfile.write(bytes(HTML_TEMPLATE, "utf8"))
        
        self.wfile.write("<h1>Hello, world!</h1>".encode('utf-8'))
        return
