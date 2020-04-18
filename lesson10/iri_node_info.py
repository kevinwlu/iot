from iota import Iota

# Create a new instance of the IOTA API object
# Specify which node to connect to
api = Iota(adapter = 'https://nodes.devnet.iota.org:443')

# Call the `get_node_info()` method for information about the node and the Tangle
response = api.get_node_info()

print(response)
