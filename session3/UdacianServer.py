#!/usr/bin/env python3
#
# Udacian activity to practice http get and post 
#
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

memory = []
form = '''<!DOCTYPE html>
  <title>Udacian</title>
  <form method="POST" >
    <textarea name="name" placeholder="name"></textarea>
    <br>
    <textarea name="city" placeholder="city"></textarea>
    <br>
    <textarea name="enrollment" placeholder="enrollment"></textarea>
    <br>
    <textarea name="nanodegree" placeholder="nanodegree"></textarea>
    <br>
    <textarea name="status" placeholder="status"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
  {}
  </pre>
'''


class MessageHandler(BaseHTTPRequestHandler):
    def do_POST(self):
      output=''
      length = int(self.headers.get('Content-length', 0))  
      data = self.rfile.read(length).decode()
      name = parse_qs(data)["name"][0]
      city = parse_qs(data)["city"][0]
      enrollment = parse_qs(data)["enrollment"][0]
      nanodegree = parse_qs(data)["nanodegree"][0]
      status= parse_qs(data)["status"][0]
      output = (name + " is Living in " + city + " and is studying " + nanodegree + " and enrolled in " + enrollment + ", he/she is " + status )
      self.send_response(200)
      self.send_header('Content-type', 'text/html; charset=utf-8')
      self.end_headers()
      self.wfile.write(form.format(output).encode())
      
    def do_GET(self):
    	#get the info and display it
      self.send_response(200)
      self.send_header('Content-type', 'text/html; charset=utf-8')
      self.end_headers()
      self.wfile.write(form.format('').encode())
    

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
