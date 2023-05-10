from django.http import HttpRequest
from django.shortcuts import render
import time

def get_useragent_on_request_middleware(get_response):

    print("initial call")

    def middleware(request: HttpRequest):
        print("before get response")
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)
        print("after get response")
        return response

    return middleware

class CountRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.responses_count = 0
        self.exceptions_count = 0
        self.request_history = {}

    def __call__(self, request: HttpRequest):
        self.requests_count += 1
        print("request count", self.requests_count)
        ip_address = request.META.get('REMOTE_ADDR')
        if ip_address in self.request_history:
            last_request_time = self.request_history[ip_address]
            if time.time() - last_request_time < 1:
                return render(request, "requestdataapp/error-request.html")
        self.request_history[ip_address] = time.time()
        response = self.get_response(request)
        self.responses_count += 1
        print("responses count", self.responses_count)
        return response




    def process_exceptions(self, request: HttpRequest, exceptions: Exception):
        self.exceptions_count += 1
        print("got", self.exceptions_count, "exceptions so far")