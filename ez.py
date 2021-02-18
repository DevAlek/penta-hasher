from os import system as s
import subprocess
path=subprocess.check_output("pwd", shell=True).decode("utf-8").replace("\n", "")
bk="\n"
l=len
def enough(args, min):
	return l(args)>=min

def check(array=None, name=None, mode="in", all=False):
	if type(array)!=list and type(array)!=tuple:error=f'argument "{array}" must be list or tuple type. not {type(array)}.'
	else:error=False
	true=None
	result=[]
	count=0
	if not error:
		if mode=="==" or mode=="is" or mode=="in":
			for i in range(l(array)):
				if type(name)!=list or type(name)!=tuple:true=f""" "{str(array[i])}" {mode} "{str(name)}" """
				else:true=f""" "{str(array[i])}" {mode} "{str(name[i])}" """
				if eval(true):
					if all: result.append(True)
					else:return True
				elif all: result.append(False)
			if all:
				for i in result:
					if i:count+=1
				if count==l(array):return True
		else: error=f'unknow mode "{mode}". should be "is", "==" or "in".'
	if error:print(error)
	return False

def command(line=None, name=None, mode="is"):
	try:command=line.split()[0]
	except:pass
	if type(name)==list or type(name)==tuple:
		if check(name, command, mode=mode):return True
	elif name==command:return True
	return False

def argumentyzer(line=None, limiter=0):
	args=[]
	line=line.split()
	if l(line)<2: return False
	else:line.remove(line[0])
	if check(('all','*'), limiter, mode="is"): limiter=l(line)
	for i in range(limiter):args.append(line[i])
	return args

def save(file=None, value=None, ignore=False, overwrite=False, math=False,breakline="|"):
	if math and not ".mat" in str(file): file=str(file)+".mat"
	integer=False
	have=False
	try: open(file, 'x')
	except:
		if ignore:return False
	if ".mat" in str(file) and not math and not overwrite:print(f"{file} is a math file. use math mode or overwrite the file."); return False
	if ".mat" in str(file) and not math and overwrite:file=file.replace(".mat", '')
	if breakline:rd=open(file, 'r').read().split(str(breakline))
	if not breakline:rd=open(value, 'r').readlines()
	if not overwrite and open(file, 'r').read()!='':have=True
	if have and math and not integer or have and math and type(value)!=int:
		print(f'file "{file}" in math mode, value has to be int type.'); return False
	if have and math:
		try:integer=int(open(file, 'r').read())
		except:pass
	if math and not have:open(file,"w").write("0"); integer=0
	if have and not math:open(file,"a").write(f"{value}{breakline}")
	if not have and not math:open(file,"w").write(f"{value}{breakline}")
	if not have and math:open(file,"w").write(f"{value}")
	if have and math:open(file,"w").write(str(integer + value))
	if overwrite:open(file,"w").write(str(value))
	return True

def read(file, breakline="|", to=False, mode=str):
	try:file=open(file,"r").read()
	except:return False
	if check((list, tuple), mode) and not to:file=file.split(breakline)
	elif not to: file=file.replace(breakline,"\n")
	if to:file=file.replace(breakline, to)
	return file

def logtyzer(log, file, into="both"):
	try: open(file, "x")
	except:pass
	if check(("both", "print"), into, mode="is"):print(log)
	if check(("both", "file"), into, mode="is"):open(f"{file}.html", 'a').write(f"<p>{log}</p>")
	return

def islink(line, dec=None):
	html=("http", "://", ".")
	try:dec=line.split('.')
	except:return False
	sufix=l(dec[l(dec)-1])>4 and l(dec[l(dec)-1])<2
	if sufix:return False
	if check(html, line,all=True):
		slash=line.split('://')
		try:
			domain=not check((' ', ''),''.join(''.join(dec).replace(dec[l(dec)-1], '').split("://")[1]), mode="==")
			http=check(("http", "https"), slash[0],mode="==")
			return domain and http
		except:pass
	return False

def single_assure(lib: str, output=False, sudo=False):
	result=False
	install=''
	method=[]
	got=False
	count=0
	sudo=''
	send=''
	try:exec(f'import {lib}');return True
	except:
		pip=('pip3', 'python3 -m pip', 'python-pip', 'pip', 'python -m pip')
		count=l(pip)
		for i in pip:
			if sudo:install='sudo '
			install+=f'{i} install {lib}'
			try:
				system(install)
				method.append("True")
				got=True
				count-=1
				for i in range(count):method.append("skipped")
			except:method.append("False");count-=1
	if got:
		try:exec(f'import {lib}');result=True
		except:
			if output:print('failed to import lib.')
			result=False
	if output and not got:send=f"{bk}automatic pip install failed"
	if output:send+=f"{bk}{' | '.join(pip)}{bk}{' | '.join(method)}{bk}";print(send)
	return result

def assure(libs, output=False, sudo=False):
	single=''
	install=[]
	array=False
	result=False
	if check((tuple, list),type(libs)):array=True
	if array:
		result=[]
		for lib in libs:
			if single_assure(lib, sudo=sudo):result.append("True")
			else:result.append("False")
	else: result=single_assure(libs, output=output, sudo=sudo)
	if output and array:print(f"{bk}{' | '.join(libs)}{bk}{' | '.join(result)}{bk}")
	return result

def temp(file=None, value=None, auto=True):
	pass

def man(page="all"):
	title="""
		  EZTYZER© by DevAlek
	"""
	m_check="""
• check(array, name, mode, all):
	array - list or tuple type
	name - all types
	mode - string type "==", "is" or "in"
	all - bool type
		
	it will check if name is in array.
	if "all" equals True, it will check if 
	name is in all array objects.
	"""
	m_command="""
• command(line, name, mode):
	line - string type
	name - string, list or tuple type
	mode - string type "==", "is" or "in"
		
	it will check if line starts with name.
	"""
	m_argumentyzer="""
• argumentyzer(line, limiter):
	line - string type
	limiter - int or string type "*" or "all"
		
	it will return the number of arguments
	from limiter.
	"""
	m_save="""
• save(file, value, mode, overwrite, math,breakline):
	file - string type
	value - string type
	ignore - bool type
	overwrite - bool type
	breakline - string type (default is "|")
		
	- it will save value into file.
		
	- in ignore mode, if file exists,
	it will return False
		
	- if overwrite equals False,
	it will append value + breakline to file.
		
	- if you're using triple quotes,
	set breakline to False. it will set
	it in readlines() mode.
	
	- in math mode, it will add value to file
	
	WARNING: make breakline character unique. 
	otherwise it will brake the entire file.
	"""
	m_logtyzer="""
• logtyzer(log, file, into):
	log - string type
	file - string type
	into - string type "print", "file" and "both"
		
	it will print log and save it in file.
	you can choose if you want.
	"""
	m_islink="""
• islink(line):
	line - string type
		
	it returns if is an actual link.
	"""
	m_single_assure='''
	comming soon
	'''
	m_assure='''
	comming soon
	'''
	commands=(
	title, m_check, m_command, m_argumentyzer, m_save, m_logtyzer, m_islink, m_single_assure, m_assure
	)
	if page=="all":print(''.join(commands))
	else:
		if page=='':return
		try:print(title, eval(f"""m_{page}"""))
		except:print(f"""m_{page} doesn't exists.""")
	return
