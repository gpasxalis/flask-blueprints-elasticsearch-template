from flask import Blueprint, render_template, request, url_for

from ..app import es


hello = Blueprint('hello',__name__)
test = Blueprint('test',__name__)


@hello.route('/')
def index_page():
	#health_doc = es.cluster.health()

	#return "This is a test"
	#return  render_template('index_page.html')
	if request.method == "POST":
		text1 = request.form["test"]
		text2 = request.form["test1"]
		return redirect(url_for("hello2.test", test=text1, test1=text2))
	else:
		return render_template("index_page.html")
	
#@test.route('/test',methods = ['POST', 'GET'])	
#def test():
#	if request.method == 'POST':
#		box=request.form['test']
#		 #return redirect(url_for('index_page'))
