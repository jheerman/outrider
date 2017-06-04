import scrapy
import json

class HuntsmanSpider(scrapy.Spider):
	name = "ncsa"
	start_urls=['https://recruit-match.ncsasports.org/clientrms/user_accounts/sign_in']

	def __init(self):
		self.account = []
		self.user, self.pwd, self.token, self.utf = None
		loadCredentials(self)
	
	def loadCredentials(self):
		with open('auth.json') as auth_data:
			self.account = json.load(auth_data)
			self.user = account["user"]
			self.pwd = account["password"]
			self.token = account["token"]
			self.utf = account["utf-8"]

	def parse(self, response):
		return scrapy.FormRequest.from_response(
			response,
			formdata={'user_account[login]': self.user, 'user_account[password]': self.pwd, 'authenticity_token': self.token, 'utf-8': self.utf},
			callback=self.after_login
        )

	def after_login(self, response):
        # check login succeed before going on
		if "authentication failed" in response.body:
			self.logger.error("Login failed")
			return
		else:
			return Request(url="https://www.ncsasports.org", 
					callback=self.parse_tuition)

	def parse_tuition(self, response):
		print "Here"
