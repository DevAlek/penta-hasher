import hashlib
import os
try:import pyperclip
except:
    try:os.system('pip3 install pyperclip')
    except:
        try:os.system('pip install pyperclip')
        except:print('automatic pip failed. try install pyperclip manualy'); exit()
while True:
    senha=str(input('> ')).encode('utf-8')
    sha244=hashlib.sha224(senha).hexdigest().encode('utf-8')
    sha256=hashlib.sha256(sha244).hexdigest().encode('utf-8')
    sha3_512=hashlib.sha3_512(sha256).hexdigest().encode('utf-8')
    sha1=hashlib.sha1(sha3_512).hexdigest().encode('utf-8')
    sha3_384=hashlib.sha3_384(sha1).hexdigest()
    result=sha3_384
    try:pyperclip.copy(result);print('hash moved to clipboard')
    except:print('failed to copy your hash automatically')
    print(result)
