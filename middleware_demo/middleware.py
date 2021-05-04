# file: middleware_demo/middleware.py

#  init takes get_response, while call returns the same object after taking request as a parameter.


# class JSONTranslationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         response = self.get_response(request)
#         return response




# class JSONTranslationMiddleware:
#     def __init__(self, get_response):
#         print(" BEFORE this is in middleware")
#         self.get_response = get_response


#         self.translations = {
#             "en": {"greeting": "Hello", "header": "Welcome Django!"},
#             "nl": {"greeting": "Hallo", "header": "Welkom Django!"},
#         }

#     def __call__(self, request):
#         print(" after this is in middleware")
#         response = self.get_response(request)
#         print("are we in again... yes we are going in to...")
#         return response      



'''middleware offers an hook made for context manipulation: process_template_response.
 It takes request and response, and has access to the context through response.context_data.  '''

from django.http.response import HttpResponse


class JSONTranslationMiddleware:
    def __init__(self, get_response):
        
        self.get_response = get_response
        self.translations = {
            "en": {"greeting": "Hello", "header": "Welcome Django!"},
            "nl": {"greeting": "Hallo", "header": "Welkom Django!"},
        }

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print(request.META)
        response.context_data["translations"] = self.translations
        return response