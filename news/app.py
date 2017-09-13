from chalice import Chalice
from config import apiKey, api_resource, app_url
import requests, json, os
from urlparse import urlparse
import boto
import boto.s3
from boto.s3.key import Key
import os.path

app = Chalice(app_name='news')

@app.route('/sources/{category}', methods=['GET'])
def index(category):
	SOURCES = {}
	s = []

	# Get news sources
	data = requests.get(api_resource + 'sources?category=' + category + '&language=en')
	json = data.json()

	for source in json['sources']:
		SOURCES['status'] = 200
		s.append({'name': source['name'], 'url': app_url + '/source/' + source['id'], 'description': source['description']})
		
	if len(s) == 0:
		SOURCES['status'] = 404
		SOURCES['error'] = 'Sources not found. Either category blank or use business, entertainment, gaming, general, music, politics, science-and-nature, sport, or technology'
	else:
		SOURCES['sources'] = s

	return SOURCES

@app.route('/source/{source_id}', methods=['GET'])
def articles(source_id):
	data = requests.get(api_resource + 'articles?source=' + source_id + '&apiKey=' + apiKey)
	json = data.json()

	return json

@app.route('/save', methods=['GET'])
def save():
	print os.path.basename()
