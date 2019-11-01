import argparse
import re

parser = argparse.ArgumentParser(description='Script to decrypt an encrypted file')
parser.add_argument('path', metavar='Binary File', type=str, nargs=1, help='encrypted file to be decrypted')

fib_arr = [1,2,3,5,8,13,21,34,55,89,144,233,377]


SECRET = 121

def fibDecoding(s):
    indices = [m.start() for m in re.finditer('1', s[:-1])]
    num = 0
    for ind in indices:
        num += fib_arr[ind]
    return num - SECRET

def encrypt(path):
    file = open(path, "r")
    writefile = open("final.mp4","wb+")
    try:
        bytes_read = file.read(13)
        while bytes_read:
            writefile.write(bytes([fibDecoding(bytes_read)]))
            bytes_read = file.read(13)
    finally:
        file.close()
        writefile.close() 

if __name__ == "__main__":
    args = parser.parse_args()
    encrypt(args.path[0])