import scrapy
import json

class HuntsmanSpider(scrapy.Spider):
	user, pwd
	token = ""
    name = 'nscasports.com'
    start_urls = ['http://https://recruit-match.ncsasports.org/clientrms/user_accounts/sign_in']

	def loadCredentials(self):
		with open('auth.json') as auth_data
			account = json.load(auth_data)
			user = account["user"]
			pwd = account["password"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': user, 'password': pwd},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        if "authentication failed" in response.body:
            self.logger.error("Login failed")
            return

        # continue scraping with authenticated session...
