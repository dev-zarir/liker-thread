from flask import Flask, request, jsonify
from helper import liker_machine
from urllib.parse import unquote_plus
from threading import Thread

app=Flask(__name__)
app.config["SECRET_KEY"]="jejejekdijsnendnjdi"
all_reacts = ['LIKE', 'LOVE', 'HAHA', 'WOW', 'SAD', 'ANGRY']

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method=='GET':
		return '<h1>App is Working</h1>'
	react=unquote_plus(request.form.get('react'))
	post_id=unquote_plus(request.form.get('post_id'))
	cookie=unquote_plus(request.form.get('cookie'))
	if not react in all_reacts:
		return jsonify({'success':False, 'msg':'Invalid Reaction Name, Available Reactions are' + ' '.join(all_reacts)})
	if len(cookie)<100:
		return jsonify({'success':False, 'msg':'Cookie Length Must be greater than 100 characters.'})
	else:
		t=Thread(target=liker_machine, args=(react, post_id, cookie))
		t.setDaemon(True)
		t.start()
		return jsonify({'success':True, 'msg':'Task added to the thread.'})



if __name__=="__main__":
	app.run(host="0.0.0.0", port=80, debug=False)
