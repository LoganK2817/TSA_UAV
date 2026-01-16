import network
import socket


ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(
    ssid="ESP32-WH",
    password="1203-1003",  # must be at least 8 characters
    authmode=network.AUTH_WPA2_PSK,
    max_clients=2
)

# Simple web server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print("Listening on", addr)

while True:
    cl, addr = s.accept()
    print('Client connected from', addr)
    request = cl.recv(1024)
    response = """\
HTTP/1.1 200 OK

<iframe src="https://www.appanageark.com" width="600" height="400" title="Description of the embedded content">
  Your browser does not support iframes, but you can visit the website directly [Link to website].
</iframe>

"""
    cl.send(response)
    cl.close()
