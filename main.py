"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, Response, request, render_template, jsonify
import urllib, urllib2
import json
import os
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return 'You Select your Options from here'

@app.route('/embed/<owner>/<repo>')
def embed(owner, repo):
	uri = "https://api.github.com/repos/{0}/{1}/contributors".format(owner, repo)

	response = urllib2.urlopen(uri)
	contributors = json.load(response)  

	resp = render_template('embed.html', contributors=contributors)
	resp = "document.write(" +json.dumps(str(resp)) + ")"
	return resp

@app.route('/test')
def test():
    return "<script src='http://localhost:8080/embed/fossrit/kettlefish' type='text/javascript'></script>"
  
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def page_not_found(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
