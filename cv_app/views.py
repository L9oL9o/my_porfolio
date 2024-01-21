from django.shortcuts import render
from django.views import View
from cv_app.models import *
from django.views.generic import ListView

from django.views.generic import ListView
from cv_app.models import *


class GetObjectsView(ListView):
    queryset = About.objects.all()
    template_name = 'index.html'
    context_object_name = 'about_items'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['facts_item'] = Fact.objects.all()
        context['static_items'] = StaticObjects.objects.all()
        context['contact_items'] = Contact.objects.all()
        context['portfolio_items'] = Portfolio.objects.all()
        context['service_items'] = Service.objects.all()
        context['testimonials_item'] = Testimonials.objects.all()
        # context['model8_objects'] = Model8.objects.all()

        return context

# class GetObjectsView(View):
#     def get(self, request):
#         about_objs = About.objects.all()
#         fact_objs = Fact.objects.all()
#
#         context = {
#             "about_objs": about_objs,
#             "facts_item": fact_objs,
#         }
#         return render(request, 'index.html', context)


# from cv_app.models import About, Fact


# class AboutView(View):
#     def get(self, request):
#         about_objs = About.objects.all()
#         context = {
#             "about_items": about_objs
#         }
#         return render(request, 'index.html', context)
#
#
# class FactsView(View):
#     def get(self, request):
#         fact_objs = Fact.objects.all()
#         context = {
#             "facts_item": fact_objs
#         }
#         return render(request, 'index.html', context)
