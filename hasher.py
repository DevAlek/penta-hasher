#!/usr/bin/python3
from random import randint as random
from ez import *
import hashlib
import os
assure(('pyperclip', 'click'), True, True)
import pyperclip
import click
external_input=False
hashs=('sha224', 'sha256', 'sha3_512', 'sha1', 'sha3_384')
@click.command()
@click.option('--isenha', default=False, help='string to hash')
@click.option('--ihash', default=False,help='hash method')
def external(isenha, ihash):
	global external_input
	try:
		if ',' in ihash:ihash=ihash.replace(' ', '').ihash.split(',')
	except:pass
	senha=''
	if isenha:
		external_input=True
		if check(('all',False),ihash):ihash=hashs
		if check((list,tuple),type(ihash)):
			for i in ihash:
				senha=eval(f"hashlib.{i}({senha.encode('utf-8')})").hexdigest()
		else:senha=eval(f"hashlib.{ihash}({senha.encode('utf-8')})").hexdigest()
		try:pyperclip.copy(senha);print('hash moved to clipboard')
		except:print('failed to copy your hash automatically')
		click.echo(senha)
	if not external_input:
		senha=''
		while True:
			try:
				senha=str(input('> '))
				if senha=='':new=random(100000, 999999);print(new);senha=str(new)
				if senha=='!':break;exit()
				for i in hashs:
					senha=eval(f"hashlib.{i}({senha.encode('utf-8')})").hexdigest()
				try:pyperclip.copy(senha);print('hash moved to clipboard')
				except:print('failed to copy your hash automatically')
				print(senha)
			except:pass
external()
