from flask import Blueprint

from ..app import es


hello = Blueprint('hello',__name__)


@hello.route('/')
def index_page():
	health_doc = es.cluster.health()

	return "Hello there! Your elastic's health report is:\n"+str(health_doc)
	
