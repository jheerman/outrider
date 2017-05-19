import json
import os.path
import requests

class OutriderClient:
	API_URL = "http://localhost:5000/api/v1/colleges"
	username=None
	password=None
	use_raw_response=False

	def __init__(self, use_raw_response=False):
		self.use_raw_response = use_raw_response

	def request(self, method, url, *args, **kwargs):
		url = "%s%s" % (self.API_URL, url)
		results = requests.request(method, url, *args, **kwargs)

		#if self.use_raw_response:
		return results

		#return json.loads(results.data)
