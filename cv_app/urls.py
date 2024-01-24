from django.urls import path

from cv_app.views import *

urlpatterns = [
    path('', GetObjectsView.as_view(), name='index'),
    # path('<int:pk>/')
]
