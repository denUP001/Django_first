from django.shortcuts import render
from random import randint as rnd
from django.views import View
from django.http import HttpResponse, JsonResponse


class RandomView(View):
    def get(self, request):
        html = f'<h1>{rnd(1, 100)}</h1>'
        return HttpResponse(html)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')
