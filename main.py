import requests
from bs4 import BeautifulSoup
import flask
from googlesearch import search
from flask import Flask
app = Flask(__name__)
from flask import request, jsonify


reqs = None 


@app.route('/api/v1/findtitle/', methods = ['GET', 'POST', 'DELETE'])
def hello_name():


 for j in search((request.args['query']), tld="co.in", num=1, stop=1, pause=2):


# using the BeaitifulSoup module

# displaying the title

  for title in BeautifulSoup(requests.get(j).text, 'html.parser').find_all('title'):
   return (title.get_text())

app.run()
