from flask import Blueprint, render_template, request, url_for
from elasticsearch import Elasticsearch

#host = "http://localhost:9200"


es = Elasticsearch()

hello2 = Blueprint('hello2',__name__)


@hello2.route('/test', methods = ["POST", "GET"])
def test():

	#return "This is a test"
	test = request.form.get('test')
	test1 = request.form.get('test1')
	#test = request.form["test"]
	res = es.search(index=test, body={"query": {"match": {"data": test1}}})
	return render_template("test.html", test=test, test1=test1, res=res)
	
	
