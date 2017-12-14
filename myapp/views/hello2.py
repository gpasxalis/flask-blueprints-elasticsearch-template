from flask import Blueprint, render_template, request, url_for


hello2 = Blueprint('hello2',__name__)


@hello2.route('/test', methods = ["POST", "GET"])
def test():

	#return "This is a test"
	test = request.form.get('test')
	#test = request.form["test"]
	return render_template("test.html", test=test)
	
	
