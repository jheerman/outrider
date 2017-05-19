import json
import os.path
import requests

class OutriderClient:
	API_URL = "http://localhost:5000/college/api/v1.0/colleges"
	username=None
	password=None
	use_raw_response=False

	def __init__(self, use_raw_response=False):
		self.use_raw_response = use_raw_response

	def request(self, method, url, *args, **kwargs):
		url = "%s%s" % (self.API_URL, url)
		response = requests.request(method, url, *args, **kwargs)

		if self.use_raw_response:
			return response

		return json.loads(response.text)
