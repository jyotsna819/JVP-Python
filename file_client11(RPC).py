import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

# Write to file on server
response = proxy.write_file("demo.txt", "Hello, this is a local RPC test!")
print(response)

# Read from file on server
print("File content:")
print(proxy.read_file("demo.txt"))
