import os

from flask import Flask
from flask_elasticsearch import FlaskElasticsearch

def create_app():
	
	app = Flask(__name__)
		
	# configure elastic
	es.init_app(app)
	
	
	# common prefix for all routes in blueprints
	APP_URL_PREFIX = os.environ.get('MY_APP_PREFIX',None)
	# register all blueprints
	from .views import blueprints
	for bp in blueprints:
		app.register_blueprint(bp,url_prefix=APP_URL_PREFIX)


	return app

	
es = FlaskElasticsearch()
app = create_app()	
	
