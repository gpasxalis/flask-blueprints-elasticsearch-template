from flask import Blueprint, render_template, request

from ..app import es


hello = Blueprint('hello',__name__)
test = Blueprint('test',__name__)


@hello.route('/')
def index_page():
	#health_doc = es.cluster.health()

	#return "This is a test"
	return  render_template('index_page.html')
	
#@test.route('/test',methods = ['POST', 'GET'])	
#def test():
#	if request.method == 'POST':
#		box=request.form['test']
#		 #return redirect(url_for('index_page'))


@test.route('/test')
def test():
	#health_doc = es.cluster.health()

	return "This is a test"
	