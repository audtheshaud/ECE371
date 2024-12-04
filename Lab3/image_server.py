import re
import struct
import sys
from socket import AF_INET, SOCK_DGRAM, gethostbyname, socket

import des
from RSA import decrypt

PORT_NUMBER = 5000
SIZE = 8192

# hostName = gethostbyname( '192.168.1.3' )
# hostName = gethostbyname("DE1_SoC")
# hostName = gethostbyname("AidanEOS")
hostName = gethostbyname("192.168.1.10")


mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))
client_public_key = ""
des_key = ""
while True:
    (data, addr) = mySocket.recvfrom(SIZE)
    data = data.decode()
    if data.find("public_key") != -1:  # client has sent their public key\
        ###################################your code goes here#####################################
        # retrieve public key and private key from the received message (message is a string!)

        # code taken from ./chat_server.py
        keys = re.search(
            r"public_key: (\d+) (\d+) private_key: (\d+) (\d+)", data
        )  # use regex to find message of key
        public_key_e = int(keys.group(1))
        public_key_n = int(keys.group(2))  # extract private and public keys
        private_key = (int(keys.group(3)), int(keys.group(4)))

        print("public key is : %d, %d" % (public_key_e, public_key_n))
    elif data.find("des_key") != -1:  # client has sent their DES key
        ###################################your code goes here####################
        # read the next 8 bytes for the DES key by running (data,addr) = mySocket.recvfrom(SIZE) 8 times and then decrypting with RSA
        for _ in range(8):
            (data, addr) = mySocket.recvfrom(SIZE)
            encrypted_byte = int(
                data.decode()
            )  # collect part of key and convert to int
            decrypted_byte = decrypt(private_key, encrypted_byte)  # decrypt
            des_key += decrypted_byte  # append to des_key
        print("DES key is :" + des_key)
        # now we will receive the image from the client
        (data, addr) = mySocket.recvfrom(SIZE)
        # decrypt the image
        ###################################your code goes here####################
        # the received encoded image is in data
        # perform des decryption using des.py
        # coder=des.des()
        # the final output should be saved in a byte array called rr_byte

        # code taken from ECE371/lab2/main.py and modified with des_key_decoded = des_key and r = data
        decoder = des.des()  # set decoder to des.des()
        des_key_decoded_str = ""
        for i in des_key:  # convert des_key to string
            des_key_decoded_str = des_key_decoded_str + str(i)
        rr = decoder.decrypt(  # decrypt without cipher block chaining
            des_key, data, cbc=False
        )  # this is in string  format, must convert to byte format
        rr_byte = bytearray()
        for x in rr:  # convert to ASCII then to bytes
            rr_byte += bytes([ord(x)])
        # write to file to make sure it is okay
        file2 = open(r"Lab3/penguin_decrypted.jpg", "wb")
        file2.write(bytes(rr_byte))
        file2.close()
        print("decypting image completed")
        break
    else:
        continue
        # python2: print data ,
