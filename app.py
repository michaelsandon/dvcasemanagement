from flask import Flask, render_template, jsonify, request
#from database import get_cases_from_database
from database import load_all_dv_cases, load_dv_case, add_report_to_db
from flask_googlemaps import GoogleMaps, Map
import os

app = Flask(__name__)
gmapapikey = os.environ['GOOGLEMAPS_API_KEY']

Safehouseloactions = [{'lat': -31.8838752, 'lng': 115.8426928}]


@app.route("/")
def render_app():
  return render_template('home.html')


@app.route("/cases")
def render_cases():
  CASES = load_all_dv_cases()
  print(CASES[0])
  return render_template('cases.html', CASES=CASES)


@app.route("/cases/<id>")
def render_case_by_id(id):
  case = load_dv_case(id)
  return render_template('case_details.html', CASE=case)


@app.route("/support")
def render_support():
  return render_template('support.html', gmapapikey=gmapapikey)


@app.route("/support/incidentreported", methods=['POST'])
def render_incidentreported():
  recordid = add_report_to_db(request.form)
  data = load_dv_case(recordid)
  return jsonify(dict(data))


@app.route("/statistics")
def render_stats():
  return render_template('statistics.html')


@app.route("/api/cases")
def list_cases():
  return jsonify(CASES)


print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
