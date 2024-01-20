from django.urls import path

from cv_app.views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='index')
]
