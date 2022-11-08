from tinydb import TinyDB, Query
from flask import Flask, request

HOSTNAME = "http://zezi.fun"
db = TinyDB('db.json')
query = Query()
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
	#if request.method == "POST":
		#if uinput[5]:
		#uinput = str(request.form["url"])
		#insert(uinput)
	return target(last_id())
	#else:
		#pass
		#return f'<form action="#" method="post"><p>URL: <input type="text" name="url"></p></form>'

@app.route("/<id>")
def short(id):
	result = db.search(query.id == int(id))
	return f'<meta http-equiv="Refresh" content="0; url=\'{result[0]["url"]}\'" />'

def target(id):
	result = db.search(query.id == int(id))
	return f'{HOSTNAME}/{id}'

def last_id():
	results = db.search(query.id == 0)
	return results[0]['url']

def insert(z):
	x = last_id()
	db.insert({'id': x+1, 'url': z})
	db.update({'url': x+1}, query.id == 0)

if __name__ == "__main__":
	app.run()
