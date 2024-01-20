from django.urls import path

from cv_app.views import ForRun

urlpatterns = [
    path('', ForRun.as_view(), name='index')
]