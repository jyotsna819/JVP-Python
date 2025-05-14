from xmlrpc.server import SimpleXMLRPCServer

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        return f"Error: {e}"

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return "Write successful"
    except Exception as e:
        return f"Error: {e}"

# Create XML-RPC server on localhost:9000
server = SimpleXMLRPCServer(("localhost", 9000))
server.register_function(read_file, "read_file")
server.register_function(write_file, "write_file")

print("Server running on http://localhost:9000/")
server.serve_forever()
