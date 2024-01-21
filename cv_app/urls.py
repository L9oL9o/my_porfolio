from django.urls import path

from cv_app.views import *

urlpatterns = [
    path('', GetObjectsView.as_view(), name='index'),
    # path('', FactsView.as_view(), name='index'),
    # path('', AboutView.as_view(), name='index'),
    # path('', AboutView.as_view(), name='index'),

]
