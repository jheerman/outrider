from flask import Flask, jsonify
from bson import json_util
from pymongo import MongoClient
import json
import re

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.college
colleges = db.colleges
teams = db.softball

@app.route('/')
def index():
    return "Hello, Outrider!"

@app.route('/college/api/v1.0/colleges', methods=['GET'])
def get_all_colleges():
    results = colleges.find()
    return clean_and_jsonify(results);

@app.route('/college/api/v1.0/colleges/<school_name>', methods=['GET'])
def get_college(school_name): 
    results = colleges.find({"school": school_name})
    return clean_and_jsonify(results);

@app.route('/college/api/v1.0/colleges/divisions/<division>', methods=['GET'])
def get_colleges_by_division(division): 
    results = colleges.find({"division": division})
    return clean_and_jsonify(results);

@app.route('/college/api/v1.0/colleges/states/<state_abbr>', methods=['GET'])
def get_colleges_by_state(state_abbr): 
    results = colleges.find({"state_abbr": state_abbr})
    return clean_and_jsonify(results);

@app.route('/college/api/v1.0/colleges/states/<state_abbr>/division/<division>', methods=['GET'])
def get_colleges_by_state_and_division(state_abbr, division): 
    results = colleges.find({"state_abbr": state_abbr, "division": division})
    return clean_and_jsonify(results);

@app.route('/college/api/v1.0/colleges/softball', methods=['GET'])
def get_all_softball():
    results = teams.find()
    return clean_and_jsonify(results);

@app.route('/college/api/v1.0/colleges/softball/coaches/<coach_name>', methods=['GET'])
def get_softball_coaches(coach_name):
    results = teams.find({'head_coach': re.compile(coach_name, re.IGNORECASE)}) 
    return clean_and_jsonify(results);

def clean_and_jsonify(results):
    cleaned_data = json.loads(json_util.dumps(results))    
    if cleaned_data:
        return jsonify({"status": "ok", "data": cleaned_data})
    else:
	return jsonify({"status": "error", "data":[]})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
