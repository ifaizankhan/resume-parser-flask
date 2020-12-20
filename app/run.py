from flask import Flask
from flask import render_template, request, redirect, url_for, jsonify, flash

import pyresparser
from pyresparser import ResumeParser
import pandas as pd
import json

#from flask_jsonpify import jsonpify

import os
from fnmatch import fnmatch

from werkzeug.utils import secure_filename


import nltk
nltk.download('stopwords')


app = Flask(__name__)

UPLOAD_FOLDER = "./uploads/"

ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def hello_world():
	#return 'Hey, we have here Flask in a Docker container!'
	return render_template('index.html')


# @app.route('/', methods=['POST'])
# def index():
#    if request.method == 'POST':
#        if 'files[]' not in request.files:
#            print('No file attached in request')
#            return redirect(request.url)
#        files = request.files.getlist("file[]")
#        print(files)
#        for file in files:
#        	if file and allowed_file(file.filename):
#        		filename = secure_filename(file.filename)
#        		file.save(os.path.join(UPLOAD_FOLDER, filename))
#        	#return render_template('index.html')
#    		return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the files part
		if 'files[]' not in request.files:
			#flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(UPLOAD_FOLDER, filename))
		#flash('File(s) successfully uploaded')
		return redirect('/')


@app.route('/parse', methods=['GET', 'POST'])
def parse():
	root_path = './uploads'
	pattern = "*.pdf"
	list_resumes=[]
	for path, subdirs, files in os.walk(root_path):
		#print(files)
		for n in files:
			print(n)
		for name in files:
			if fnmatch(name, pattern):
				list_resumes.append(ResumeParser('./uploads/%s' % os.path.join(name)).get_extracted_data())
	print(list_resumes)
	return jsonify(list_resumes)



# @app.route('/process', methods=['GET', 'POST'])
# def process():
# 	df = pd.DataFrame(parse(list_resumes))
# 	df = df.astype(str)
# 	list_of_list = [[]]
# 	list_of_list[0] = list(df.columns)
# 	list_of_list.extend(df.values.tolist())	

# 	result = predict(list_of_list, ["what were the candidate names?"])


@app.route('/display')
def dir_listing():
	your_path = './uploads'
	files = os.listdir(your_path)
	return jsonify(files)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
