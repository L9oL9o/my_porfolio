from django.shortcuts import render
from django.views import View

from cv_app.models import *


# class ForRun(View):
#     def get(self, request):
#         return render(request, 'index.html')


class AboutView(View):
    def get(self, request, ):
        about_objs = About.objects.all()
        context = {
            "about_items": about_objs
        }
        return render(request, 'index.html', context)

