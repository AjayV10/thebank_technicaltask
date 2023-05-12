from django.http import HttpResponse
class Run(object):
	def __init__(self,get_response):
		self.get_response = get_response
	def __call__(self,request):
		response = self.get_response(request)
		return response
	def process_exception(self,request,exception):
		x="<html><center><h1>Internal Error Occured</h1><br><br><h3>Please contact the admin</h3></center></html>"
		return HttpResponse(x)