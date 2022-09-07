# coding:utf-8
import time

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

# reponse time: wsgi or socket interface

class TimeItMiddleware(MiddlewareMixin):

    # auth or http header
    # return HttpResponse(thus only excute process_response) or NONE
    def process_request(self, request):
        return

    def process_view(self, request, func, *args, **kwargs):
        # @PARA func : view
        if request.path != reverse('index'):
            return None

        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('{:.2f}s'.format(costed))
        return response


    # only if func Exception or template render Exception
    # NOTE: no entrypoint if func is called manually in process_view
    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        # after view when return render(request)
        return response

    def process_response(self, request, response):
        return response