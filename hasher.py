#!/usr/bin/python3
from ez import *
import hashlib
import os
assure(('pyperclip'), True, True)
import pyperclip
while True:
    senha=str(input('> ')).encode('utf-8')
    if senha.decode('utf-8')=='!':exit()
    hashs=('sha224', 'sha256', 'sha3_512', 'sha1', 'sha3_384')
    for i in hashs:
        senha=eval(f"hashlib.{i}({senha})").hexdigest().encode('utf-8')
    senha=senha.decode('utf-8')
    try:pyperclip.copy(senha);print('hash moved to clipboard')
    except:print('failed to copy your hash automatically')
    print(senha)
