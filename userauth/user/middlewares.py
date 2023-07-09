from django.shortcuts import render

class siteUnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('middleware')
        response = render(request, 'user/siteUnderConstruction.html') 
        return response
