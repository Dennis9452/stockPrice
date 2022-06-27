#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import http.server
from nbaStats import NBAstats
from http.server import SimpleHTTPRequestHandler

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = http.server.HTTPServer
Protocol     = "HTTP/1.0"

nbaStats = NBAstats()



if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 5000
server_address = ('172.21.103.174', port)

class S(HandlerClass):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print ("got get request %s" % (self.path))
        if self.path == '/':
          self.path = '/index.html'
          self.path = '/nbaStats.py'
          return SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/player':
            self.path = '/nbaStats.py'
            return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print ("got post!!")
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)
        test_data = simplejson.loads(post_body)
        print ("post_body(%s)" % (test_data))
        return SimpleHTTPRequestHandler.do_POST(self)



HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
finally:
    # Clean-up server (close socket, etc.)
    httpd.server_close()
