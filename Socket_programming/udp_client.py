import socket  # Import the socket module to enable network communication

# Define constants for the client
HEADER = 64  # The fixed length of the header that will store the length of the message
PORT = 5150  # The port number on which the server is listening
FORMAT = "utf-8"  # The encoding format used for messages (UTF-8)
SERVER_EXIT = "!DISCONNECT"  # Special message indicating the client wants to disconnect
SERVER = "localhost"  # The IP address of the server (localhost means the local machine)
ADDR = (SERVER, PORT)  # The address tuple containing the server's IP address and port number

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a socket using IPv4 and UDP protocol

# Function to send a message to the server
def send(msg):
    message = msg.encode(FORMAT)  # Encode the message using the specified format
    client.sendto(message, ADDR)  # Send the message to the server

    # Receiving response from server
    response, _ = client.recvfrom(HEADER)  # Receive the response from the server
    print(f"Server: {response.decode(FORMAT)}")  # Print the response from the server

try:
    print("Connected to the server.")  # Print a message indicating that the client is connected to the server
    while True:  # Loop to keep sending messages to the server until the client decides to disconnect
        msg = input("Enter message: ")  # Prompt the user to enter a message
        send(msg)  # Send the entered message to the server
        if msg == SERVER_EXIT:  # Check if the entered message is the disconnect message
         break  # Break the loop to disconnect from the server
finally:
    client.close()  # Close the connection to the server
    print("Disconnected from the server.")  # Print a message indicating that the client is disconnected from the server
