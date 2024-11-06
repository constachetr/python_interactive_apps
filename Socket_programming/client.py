import socket  # Import the socket module to enable network communication

# Define constants for the client
HEADER = 64  # The fixed length of the header that will store the length of the message
PORT = 5150  # The port number on which the server is listening
FORMAT = "utf-8"  # The encoding format used for messages (UTF-8)
SERVER_EXIT = "!DISCONNECT"  # Special message indicating the client wants to disconnect
SERVER = "localhost"  # The IP address of the server (localhost means the local machine)
ADDR = (SERVER, PORT)  # The address tuple containing the server's IP address and port number

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Create a socket using IPv4 and TCP protocol
# Function to send a message to the server
def send(msg):
    message = msg.encode(FORMAT)  # Encode the message using the specified format
    msgLength = len(message)  # Get the length of the encoded message
    sendLength = str(msgLength).encode(FORMAT)  # Convert the length to a string and then encode it
    sendLength += b" " * (HEADER - len(sendLength))  # Pad the encoded length to match the HEADER size
    client.send(sendLength)  # Send the length of the message
    client.send(message)  # Send the actual message

    # Receiving response from server
    recvLength = client.recv(HEADER).decode(FORMAT)  # Receive the length of the response message from the server
    if recvLength:  # Check if a response length was received
        recvLength = int(recvLength)  # Convert the response length from string to integer
        response = client.recv(recvLength).decode(FORMAT)  # Receive the actual response message based on its length
        print(f"Server: {response}")  # Print the response from the server


try:
    client.connect(ADDR)  # Connect to the server using the specified address
    print("Connected to the server.")  # Print a message indicating that the client is connected to the server
    while True:  # Loop to keep sending messages to the server until the client decides to disconnect
        #send("Hello There!")
        msg = input("Enter message: ")  # Prompt the user to enter a message
        send(msg)  # Send the entered message to the server
        if msg == SERVER_EXIT:  # Check if the entered message is the disconnect message
            break  # Break the loop to disconnect from the server
finally:
    client.close()  # Close the connection to the server
    print("Disconnected from the server.")  # Print a message indicating that the client is disconnected from the server






