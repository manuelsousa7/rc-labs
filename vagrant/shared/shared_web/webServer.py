from socket import *
import sys # In order to terminate the program
 
HOST, PORT = '', 8000

serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind your socket
serverSocket.bind((HOST, PORT))
serverSocket.listen(1)

while True:
    #Listen and wait for request 
    #Fill in start  #Fill in end
    #serverSocket.listen(1)

    #Establish the connection
    print('Ready to serve in port %s...' % PORT)
    connectionSocket, addr = serverSocket.accept()

    try:
        #Read the message sent
        message = connectionSocket.recv(1024).decode()
        print(message)

        filename = message.split()[1]               
        if filename[1:]=="":
            filename="/index.htm"
        f = open(filename[1:], 'rb')                      
        outputdata = f.read()               

        #Send response message
        MESSAGE = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(MESSAGE.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):         
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")

        #Close client socket 
        connectionSocket.close()
    except IOError:
        filename = "/error.htm"               
        f = open(filename[1:], 'rb')                      
        outputdata = f.read() 
      
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")

        #Send the content of error file to the client
        connectionSocket.send(outputdata.encode()) 

        #Close client socket 
        connectionSocket.close() 
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 