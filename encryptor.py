import argparse
import re

parser = argparse.ArgumentParser(description='Script to encrypt a binary file')
parser.add_argument('path', metavar='Binary File', type=str, nargs=1, help='binary file to be encrypted')

fib_arr = [1,2,3,5,8,13,21,34,55,89,144,233,377]

CHUNK_SIZE = 128

SECRET = 121

# Python program for Zeckendorf's theorem. It finds 
# representation of n as sum of non-neighbouring 
# Fibonacci Numbers. 
  
# Returns the greatest Fibonacci Numberr smaller than 
# or equal to n. 
def nearestSmallerEqFib(n): 
      
    # Corner cases 
    if (n == 0 or n == 1): 
        return n 
         
    # Finds the greatest Fibonacci Number smaller 
    # than n. 
    f1, f2, f3 = 0, 1, 1
    while (f3 <= n): 
        f1 = f2; 
        f2 = f3; 
        f3 = f1 + f2; 
    return f2

def fibEncoding(n):
    codedString = ['0','0','0','0','0','0','0','0','0','0','0','0','1']
    n += SECRET
    while(n>0):
        s = nearestSmallerEqFib(n)
        codedString[fib_arr.index(s)] = '1'
        n -= s
    return ''.join(codedString)

def encrypt(path):
    file = open(path, "rb")
    writefile = open("encoded.txt","w+")
    try:
        bytes_read = file.read(CHUNK_SIZE)
        while bytes_read:
            my_arr = list(bytes_read)
            my_arr = [fibEncoding(i) for i in my_arr]
            enc_line = ''.join(my_arr)
            writefile.write(enc_line)
            bytes_read = file.read(CHUNK_SIZE)
    finally:
        file.close()
        writefile.close() 

if __name__ == "__main__":
    args = parser.parse_args()
    encrypt(args.path[0])