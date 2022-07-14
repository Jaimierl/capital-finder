from http.server import BaseHTTPRequestHandler
# Base url handler
from urllib import parse

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        country = dictionary.get("country")
        capital = dictionary.get("capital")




        self.send_response(200)
         # We have reached somewhere valid
        self.send_header('Content-type', 'text/plain')
         # Formatting the content
        self.end_headers()
        message = "Hello World!  We made some changes."
        self.wfile.write(message.encode())
       #Without the encode you will not be able to see the text on the screen.
        return
