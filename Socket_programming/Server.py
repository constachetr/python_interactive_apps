import socket  # Import the socket module to enable network communication
import threading  # Import the threading module to handle multiple clients simultaneously

# Define constants for the server
HEADER = 64  # The fixed length of the header that will store the length of the message
PORT = 5150  # The port number on which the server will listen for incoming connections
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = "localhost"  # The IP address of the server (localhost means the local machine)
ADDR = (SERVER, PORT)  # The address tuple containing the server's IP address and port number
FORMAT = "utf-8"  # The encoding format used for messages (UTF-8)
SERVER_EXIT = "!DISCONNECT"  # Special message indicating the client wants to disconnect

# Create and bind the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket using IPv4 and TCP protocol
server.bind(ADDR)  # Bind the server to the specified address and port

# Counter for active connections
active_connections = 0

# Function to handle communication with a single client
def handleClient(conn, addr):
    global active_connections
    print(f"[NEW CONNECTION] {addr} connected.")
    active_connections += 1  # Increment the counter
    print(f"[ACTIVE CONNECTIONS] {active_connections}")
    connected = True  # Flag to keep track of whether the client is still connected
    while connected:  # Loop to keep handling messages from the client until they disconnect
        try:
            # Receive the length of the incoming message
            msgLength = conn.recv(HEADER).decode(FORMAT)
            if msgLength:  # Check if a message length was received
                msgLength = int(msgLength)  # Convert the message length from string to integer
                msg = conn.recv(msgLength).decode(FORMAT)  # Receive the actual message based on its length
                if msg == SERVER_EXIT:  # Check if the received message is the disconnect message
                    break
                    connected = False  # Set the connected flag to False to break the loop
                print(f"[{addr}] {msg}")  # Print the received message along with the client's address

                # Sending a reply back to the client
                reply = f"{SERVER}: received your message"  # Create a reply message
                send(reply, conn)  # Send the reply back to the client
        except Exception as e:  # Catch any exceptions that occur during message handling
            print(f"[ERROR] {e}")  # Print any error that occurs
            connected = False  # Ensure the connection is closed in case of an error

    conn.close()  # Close the connection when the client disconnects
    active_connections -= 1  # Decrement the counter
    print(f"[DISCONNECTED] {addr} disconnected.")
    print(f"[ACTIVE CONNECTIONS] {active_connections}")

# Function to send a message to the client
def send(msg, conn):
    message = msg.encode(FORMAT)  # Encode the message using the specified format
    msgLength = len(message)  # Get the length of the encoded message
    sendLength = str(msgLength).encode(FORMAT)  # Convert the length to a string and then encode it
    sendLength += b" " * (HEADER - len(sendLength))  # Pad the encoded length to match the HEADER size
    conn.send(sendLength)  # Send the length of the message
    conn.send(message)  # Send the actual message

# Function to start the server and listen for incoming connections
def start():
    server.listen()  # Start listening for incoming connections
    print(f"[LISTENING] Server is listening on {SERVER}")  # Print a message indicating that the server is listening
    while True:  # Loop to continuously accept new connections
        conn, addr = server.accept()  # Accept a new connection (conn is the new socket object, addr is the client's address)
        thread = threading.Thread(target=handleClient, args=(conn, addr))  # Create a new thread to handle the client connection
        thread.start()  # Start the new thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")  # Print the number of active connections (subtracting one for the main thread)

print("[STARTING] server is starting...")  # Print a message indicating that the server is starting
start()  # Call the start() function to begin listening for connections




