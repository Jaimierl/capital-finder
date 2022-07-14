from http.server import BaseHTTPRequestHandler
# Base handler is needed

class handler(BaseHTTPRequestHandler):
    def do_Get(self):

        self.send_response(200)
        # We have reached somewhere valid
        self.send_header('Content-type', 'text/plain')
        # Formatting the content
        self.end_headers()
        message = "Hello World, my first API"
        self.wfile.write(message.encode())
        #Without the encode you will not be able to see the text on the screen.
        return