import socketserver


class SimpleTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print("before proccessing data.....")
        return


    def handle(self):
        data = self.request.recv(1024)
        print(f"Received -> {data}".encode('utf-8'))
        self.request.send("thanks".encode('utf-8'))
        return


    def finish(self):
        print("after proccessing data....")
        return socketserver.BaseRequestHandler.finish(self)


class SimpleTCPServer(socketserver.TCPServer):
    def server_activate(self):
        print("server is activated....")
        return socketserver.TCPServer.server_activate(self)

    def server_close(self):
        print("server is shuting down..")
        return socketserver.TCPServer.server_close(self)

    def verify_request(self, request, client_address):
        print("blocking some ip address..")
        return socketserver.TCPServer.verify_request(self, request, client_address)

    def finish_request(self, request, client_address):
        print("sending data to request handler..")
        return socketserver.TCPServer.finish_request(self, request, client_address)


server = SimpleTCPServer(('127.0.0.1', 8001), SimpleTCPHandler)

ip, port = server.server_address
print(ip, port)
server.serve_forever()
