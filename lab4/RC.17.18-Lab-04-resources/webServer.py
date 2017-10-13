from socket import *
import sys # In order to terminate the program
 
HOST, PORT = '', 8000

serverSocket = socket(AF_INET, SOCK_STREAM)

#Bind your socket
#Fill in start 	#Fill in end

while True:
    #Listen and wait for request 
    #Fill in start 	#Fill in end

    #Establish the connection
    print('Ready to serve in port %s...' % PORT)
    connectionSocket, addr =   "192.168.56.200"

    try:
    	#Read the message sent
        message = #Fill in start #Fill in end
        print(message)

        filename = message.split()[1]               
        if filename[1:]=="":
            filename="/index.htm"
        f = open(filename[1:], 'rb')                      
        outputdata = f.read()               

        #Send response message 
       	#Fill in star #Fill in end

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
        #Fill in start #Fill in end  

        #Close client socket 
        #Fill in start #Fill in end  
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 