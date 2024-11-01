#function for finding gcd of two numbers using euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#uses extened euclidean algorithm to get the d value
def get_d(num, modulo):
    ###################################your code goes here#####################################
    remainder = modulo
    quotient_list = []
    num_list = []
    modulo_list = []
    while remainder != 0:
        num_list.append(num)
        modulo_list.append(modulo)
        remainder = modulo % num
        quotient = modulo // num
        quotient_list.append(quotient)
        modulo = num
        num = remainder
    num_list.reverse()
    modulo_list.reverse()
    x = num
    y = modulo    
    for i in range(len(quotient_list)):
        num = num_list[i]
        modulo = modulo_list[i]
        tempx = x
        tempy = y
        x = tempy - (modulo // num) * tempx
        y = tempx
    return (x % modulo_list[-1] + modulo_list[-1]) % modulo_list[-1]
    
def is_prime (num):
    if num > 1: 
      
        # Iterate from 2 to n / 2  
       for i in range(2, num//2): 
         
           # If num is divisible by any number between  
           # 2 and n / 2, it is not prime  
           if (num % i) == 0: 
               return False 
               break
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
    n=p*q
    eulers_totient=(p-1)*(q-1)
    print(eulers_totient)
    e=65537 # Fermat prime
    d = get_d(e,eulers_totient)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    ###################################your code goes here#####################################
    #plaintext is a single character
    #cipher is a decimal number which is the encrypted version of plaintext
    #the pow function is much faster in calculating power compared to the ** symbol !!!
    m = ord(plaintext)
    cipher=pow(m, pk[0], pk[1])
    return cipher

def decrypt(pk, ciphertext):
    ###################################your code goes here#####################################
    #ciphertext is a single decimal number
    #the returned value is a character that is the decryption of ciphertext
    m = pow(ciphertext, pk[0], pk[1]) 
    plain=chr(m)
    return plain

