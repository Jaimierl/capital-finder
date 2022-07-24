from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):


    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)
        country = dictionary.get("country")
        capital = dictionary.get("capital")

        if "country" in dictionary:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dictionary["country"])
            data = r.json()
            cap = []
            for search_country in data:
                country_cap = search_country["capital"][0]
                cap.append(country_cap)
            the_capital = cap[0]
            message = f"The capital of {country} is {the_capital}"     
            # message = "Hello"
        
        if "capital" in dictionary: 
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dictionary["capital"])
            data = r.json()
            country_boi = []
            # final_country = data[0]["name"]["official"]
            #The data is in an array, then a dictionary (name) then another dictionary (official)
            for search_capital in data:
                the_country = str(search_capital["name"]["official"])
                country_boi.append(the_country)
            final_country = country_boi[0]
            message = f"{capital} is the capital of {final_country}."
            # message = "Hello"

        else:
            message = "Input a country or capital"

        self.send_response(200)
         # We have reached somewhere valid
        self.send_header('Content-type', 'text/plain')
         # Formatting the content
        self.end_headers()
        # message = "Outer Function"
        self.wfile.write(message.encode())
       #Without the encode you will not be able to see the text on the screen.
        return
