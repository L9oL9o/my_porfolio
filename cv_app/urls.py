from django.urls import path

from cv_app.views import *

urlpatterns = [
    path('', GetObjectsView.as_view(), name='index'),
    path('detail/project/<str:slug>/', get_project_details, name='detail'),
    # path('detail/project/<str:slug>/', get_project_detail_images, name='detail_img'),
    path('contact/', contact_view, name='contact_form'),

]
