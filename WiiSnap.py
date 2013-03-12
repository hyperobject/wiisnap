#WiiSnap by Technoboy10
import SimpleHTTPServer
class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
	path = self.path
	print path
	ospath = os.path.abspath('')
	if 'setled' in path:
		regex = re.compile("\/setled([0-9]+)")
		m = regex.match(path)
		led = m.group(1)
		wm.led = int(led)
	elif 'rumble' in path:
		regex = re.compile('\/rumble(on|off)')
		m = regex.match(path)
		setr = m.group(1)
		if setr == 'on':
			wm.rumble = 1
		elif setr == 'off':
			wm.rumble = 0
	"""elif 'getled' in path:
		f = open(ospath + '/return', 'w+')
		f.write(str(wm.state['led']))
		f.close()
		f = open(ospath + '/return', 'rb')
		ctype = self.guess_type(ospath + '/return')
		self.send_response(200)
	        self.send_header("Content-type", ctype)
	        fs = os.fstat(f.fileno())
	        self.send_header("Content-Length", str(fs[6]))
	        self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
	        self.send_header("Access-Control-Allow-Origin", "*")
	        self.end_headers()"""
if __name__ == "__main__":
    print "WiiSnap by Technoboy10"
    import re
    import os
    import SocketServer
    import cwiid
    print "Please connect a Wiimote by pressing 1 and 2 on your Wiimote."
    #try:
    wm = cwiid.Wiimote()
    wm.rpt_mode = cwiid.RPT_BTN
    #except:
        #print "Wiimote not found. Please press 1 and 2 on your Wiimote and try again."
        #quit()
    PORT = 1280 #Major device code for a Wiimote

    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()

