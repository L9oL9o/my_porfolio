from django.shortcuts import render
from django.views import View


class ForRun(View):
    def get(self, request):
        return render(request, 'index.html')
