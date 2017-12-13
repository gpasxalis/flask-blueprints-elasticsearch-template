from flask import Blueprint


hello2 = Blueprint('hello2',__name__)


@hello2.route('/test',methods=['POST'])
def test():

	return "This is a test"
	
	
