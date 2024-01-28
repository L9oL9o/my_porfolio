from django.urls import path

from cv_app.views import *

urlpatterns = [
    path('', GetObjectsView.as_view(), name='index'),
    path('detail/project/<str:slug>/', get_project_details, name='detail')
]
