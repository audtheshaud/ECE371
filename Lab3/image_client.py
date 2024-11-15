import des
import sys
from socket import socket, AF_INET, SOCK_DGRAM, gethostbyname
from RSA import generate_keypair, encrypt, decrypt
import struct

SERVER_IP = gethostbyname("192.168.1.10")  # Alterra hosting
# SERVER_IP = gethostbyname("DE1_SoC")
# SERVER_IP = gethostbyname("AidanEOS")
PORT_NUMBER = 5000
SIZE = 1024
des_key = "secret_k"
print(
    "Test client sending packets to IP {0}, via port {1}\n".format(
        SERVER_IP, PORT_NUMBER
    )
)

mySocket = socket(AF_INET, SOCK_DGRAM)
message = "hello"

# first generate the keypair
# get these two numbers from the excel file for seat 5B:  p - 1297211	q - 1297601
p = 1297211
q = 1297601
###################################your code goes here#####################################
# generate public and private key from the p and q values
public, private = generate_keypair(p, q)  # make keypairs
# send key

message = "public_key: %d %d private_key: %d %d" % (
    public[0],
    public[1],
    private[0],
    private[1],
)  # send over private and public keys
mySocket.sendto(message.encode(), (SERVER_IP, PORT_NUMBER))
# send des_key
message = "des_key"
mySocket.sendto(message.encode(), (SERVER_IP, PORT_NUMBER))
###################################your code goes here#####################################
# encode the DES key with RSA and save in DES_encoded, the value below is just an example
des_encoded = []
for char in des_key:  # encode each char in des_key
    encrypted_char = str(encrypt(public, char))
    des_encoded.append(encrypted_char)

# old code
# des_encoded = ["2313", "3231", "532515", "542515", "5135151", "31413", "15315", "14314"]
[mySocket.sendto(code.encode(), (SERVER_IP, PORT_NUMBER)) for code in des_encoded]
# read image, encode, send the encoded image binary file
file = open(r"Lab3/penguin.jpg", "rb")  # relative path, need to update
data = file.read()
file.close()
###################################your code goes here#####################################
# the image is saved in the data parameter, you should encrypt it using des.py
# set cbc to False when performing encryption, you should use the des class
# coder=des.des(), use bytearray to send the encryped image through network
# r_byte is the final value you will send through socket

# code taken from ECE371/lab2/main.py
coder = des.des()
r = coder.encrypt(des_key, data, cbc=False)  # encrypted image
# write the encrypted image into file
r_byte = bytearray()
for x in r:
    r_byte += bytes([ord(x)])

# send image through socket
mySocket.sendto(bytes(r_byte), (SERVER_IP, PORT_NUMBER))
print("encrypted image sent!")
