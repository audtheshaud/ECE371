import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair, encrypt, decrypt


SERVER_IP = gethostbyname("192.168.1.10")  # Alterra hosting
# SERVER_IP = gethostbyname("AidanEOS")  # Aidans laptop hostname
# SERVER_IP = gethostbyname("insertname") # Adi's laptop hostname

PORT_NUMBER = 5000
SIZE = 1024
print(
    "Test client sending packets to IP {0}, via port {1}\n".format(
        SERVER_IP, PORT_NUMBER
    )
)

mySocket = socket(AF_INET, SOCK_DGRAM)
message = "hello"

# first generate the keypair
# get these two numbers from the excel file
# for seat 5B:  p - 1297211	q - 1297601


p = 1297211
q = 1297601
###################################your code goes here#####################################
# generate public and private key from the p and q values
public, private = generate_keypair(p, q)  # make keypairs

message = "public_key: %d %d private_key: %d %d" % (
    public[0],
    public[1],
    private[0],
    private[1],
)  # send over private and public keys
mySocket.sendto(message.encode(), (SERVER_IP, PORT_NUMBER))
while True:
    message = input()
    message.join("\n")
    ###################################your code goes here#####################################
    # message is a string input received from the user, encrypt it with RSA character by character and save in message_encoded
    # message encoded is a list of integer ciphertext values in string format e.g. ['23131','352135','54213513']
    # hint: encrypt each character in message using RSA and store in message_encoded
    message_encoded = [
        str(encrypt(public, char)) for char in message
    ]  # encrypt the message, make string so code.encode works
    [
        mySocket.sendto(code.encode(), (SERVER_IP, PORT_NUMBER))
        for code in message_encoded
    ]  # do not change [sends message through socket]
sys.exit()
