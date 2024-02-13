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
<title>Titolo</title>
<style>
body {{
    font-family: Arial, sans-serif;
}}
</style>
</head>
<body>
<h1>Titolo</h1>
<h2>Sottotitolo</h2>
</body>
</html>
"""
        self.wfile.write(stringa.encode('utf-8'))
        return
