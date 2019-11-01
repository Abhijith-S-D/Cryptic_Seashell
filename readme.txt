Cryptic Seashell

As you see Nature is very mysterious. Every design in it has its own value.
Yes I'm talking about golden ratio "phi". This is also called as nature's number.

Our Cryptic seashell is a very ancient method used by marine gods to communicate with people.
Here I present the same kind of communication with this project.

This project consists of 3 files
1: encryptor.py : This is a script which was used to encrypt a mp4 file.
2: encoded.txt : This is the message in encrypted format.
3: decryptor.py : This is the script with an empty function which needs to be filled by you (fibDecoding).

Explaination of encryption:
    Any binary file is composed of bytes of data where each byte can be converted to a number between 0-256.
    Inspired by fibonacci series, we can encode every number into binary string using 
    Zeckendorf’s Theorem (Non-Neighbouring Fibonacci Representation) through fibonnacci coding.(https://www.geeksforgeeks.org/fibonacci-coding/)
    Inspired by all these algorithms, I Cryptic Seashell has been designed as a symmetric encryption algorithm.

    For every byte that Cryptic seashell watches, it adds a secret key to the number representation of the byte
    and extracts the  Non-Neighbouring binary Fibonacci Representation of the resulting number upto 13 digits and appends it to a text file (encoded.txt)


Task to do:
    Analyse the encryptor.py script and complete the "fibDecoding" function. Then using the correct SECRET (key)
    decrypt the encoded.txt to obtain the message.

    Requirements: python 3 :)

Clue for SECRET key:
    I was born in the square of Karnataka Rajyotsava. My roots are in the day and month of my birth. I have 3 faces.