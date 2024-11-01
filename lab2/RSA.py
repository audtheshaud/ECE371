#function for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(num, modulo):
    ###################################your code goes here#####################################
    remainder = modulo # Initialize the remainder to any value greater than 0
    num_list = [] # List of all the numbers used in the Euclidean Algorithm, starting with e
    modulo_list = [] # List of all the modulos used in the Euclidean Algorithm, starting with euler's totient
    while num != 0: # Euclidean algorithm that goes until num = 0, and modulo = 1
        num_list.append(num) # Adds current num to the list
        modulo_list.append(modulo) # Adds current modulo to the list
        remainder = modulo % num # Finds the remainder
        modulo = num # Change to continue to the ext line in the algorithm
        num = remainder # Change to continue to the ext line in the algorithm
    num_list.reverse() # Reverse the list to go backwards
    modulo_list.reverse() # Reverse the list to go backwards
    x = num # Initial Value is 0
    y = modulo # Initial Value is 1
    for i in range(len(num_list)): # Iterate through `num_list` and `modulo_list` to compute the Extended Euclidean Algorithm
        # Each iteration of the loop reverses one step of the Euclidean Algorithm
        # This is to reconstruct the coefficients for the linear combination that finds the GCD(e, euler's totient)
        num = num_list[i]
        modulo = modulo_list[i]
        tempx = x
        tempy = y
        x = tempy - (modulo // num) * tempx
        y = tempx
    # By the end of the loop, x holds a value such that the original num*x + original modulo*y = GCD(e, euler's totient)
    # The function adjusts the x value to be within the range of modulo_list[-1], ensuring a positive result
    return (x % modulo_list[-1] + modulo_list[-1]) % modulo_list[-1] 
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
           else: 
               return True
    else: 
        return False


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    ###################################your code goes here#####################################
    n=p*q # Calculate n
    eulers_totient=(p-1)*(q-1) # Calculate Euler's Totient
    e=65537 # Fermat prime, most used value in RSA for e
    d = get_d(e,eulers_totient) # Call get_d using the e and 
    return ((e, n), (d, n)) # Return (Public key, Private Key)

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    m = ord(plaintext) # Turn character into an integer
    cipher=pow(m, pk[0], pk[1]) # c = m^e mod n using the Public Key (e, n)
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    m = pow(ciphertext, pk[0], pk[1]) # m = c^d mod n using the Private Key (d, n)
    plain=chr(m) # Turn integer into a character
    return plain

