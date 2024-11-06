import socket  # Import the socket module to enable network communication
import threading  # Import the threading module to handle multiple clients simultaneously

# Define constants for the server
HEADER = 64  # The fixed length of the header that will store the length of the message
PORT = 5150  # The port number on which the server will listen for incoming connections
SERVER = "localhost"  # The IP address of the server (localhost means the local machine)
ADDR = (SERVER, PORT)  # The address tuple containing the server's IP address and port number
FORMAT = "utf-8"  # The encoding format used for messages (UTF-8)
SERVER_EXIT = "!DISCONNECT"  # Special message indicating the client wants to disconnect

# Create and bind the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a socket using IPv4 and UDP protocol
server.bind(ADDR)  # Bind the server to the specified address and port

# Function to handle communication with a single client
def handleClient(data, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    print(f"[{addr}] {data}")

    # Sending a reply back to the client
    reply = f"{SERVER}: received your message"  # Create a reply message
    server.sendto(reply.encode(FORMAT), addr)  # Send the reply back to the client

# Function to start the server and listen for incoming connections
def start():
    print(f"[LISTENING] Server is listening on {SERVER}")  # Print a message indicating that the server is listening
    while True:  # Loop to continuously accept new connections
        data, addr = server.recvfrom(HEADER)  # Receive data from a client
        thread = threading.Thread(target=handleClient, args=(data.decode(FORMAT), addr))  # Create a new thread to handle the client
        thread.start()  # Start the new thread

print("[STARTING] server is starting...")  # Print a message indicating that the server is starting
start()  # Call the start() function to begin listening for connections
