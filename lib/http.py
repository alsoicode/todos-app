from django.http import HttpResponse


class JsonResponse(HttpResponse):
    def __init__(self, content):
        super(JsonResponse, self).__init__(content,
            content_type='application/json')
