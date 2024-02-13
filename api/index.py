from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        #self.wfile.write(bytes(HTML_TEMPLATE, "utf8"))
        stringa = """
<!DOCTYPE html>
<html>
<head>
<title>XRPL DID</title>
<style>
body {{
    background-color: #ffcccc
    font-family: Arial, sans-serif;
}}
</style>
</head>
<body>
<h1>XRPL DID</h1>
<h2>Una demo da implementare</h2>
</body>
</html>
"""
        self.wfile.write(stringa.encode('utf-8'))
        return
