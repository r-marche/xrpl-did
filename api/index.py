from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>{title}</title>
<style>
body {{
    background-color: {background_color};
    font-family: Arial, sans-serif;
}}
</style>
</head>
<body>
<h1>{title}</h1>
<h2>{subtitle}</h2>
</body>
</html>
"""

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        html_content = HTML_TEMPLATE.format(title="XRPL DID", subtitle="test-sottotitolo", background_color="#ffffff")
        
        self.wfile.write(bytes(html_content, "utf8"))
        
        # self.wfile.write('Hello, world!'.encode('utf-8'))
        return
