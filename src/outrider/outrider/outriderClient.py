import json
import os.path
import requests
from django.conf import settings

class OutriderClient:
	ENDPOINT_BASE = "%s/outpost/api/v1.0/colleges/" %settings.API_SERVER
	username=None
	password=None
	use_raw_response=False

	def __init__(self, use_raw_response=False):
		self.use_raw_response = use_raw_response

	def request(self, method, url, *args, **kwargs):
		url = "%s%s" % (self.ENDPOINT_BASE, url)
		print url
		response = requests.request(method, url, *args, **kwargs)

		if self.use_raw_response:
			return response

		return json.loads(response.text)
