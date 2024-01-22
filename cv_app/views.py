from django.views.generic import ListView
from cv_app.static_models.static_models import *
from cv_app.static_models.partition_models import *
from cv_app.models import *


class GetObjectsView(ListView):
    queryset = About.objects.all()
    template_name = 'index.html'
    context_object_name = 'about_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['facts_item'] = Fact.objects.all()
        context['skills_item'] = Skills.objects.all()
        context['resume_items'] = Resume.objects.all()
        context['portfolio_items'] = Portfolio.objects.all()
        context['service_items'] = Service.objects.all()
        context['testimonials_item'] = Testimonials.objects.all()

        # STATIC MODELS
        context['about_me_items'] = AboutMe.objects.all()
        context['contact_me_items'] = ContactMe.objects.all()
        context['left_side_items'] = LeftSide.objects.all()

        # STATIC PARTITION MODELS
        context['about_part_items'] = AboutPart.objects.all()
        context['fact_part_items'] = FactPart.objects.all()
        context['skill_part_items'] = SkillPart.objects.all()
        context['resume_part_items'] = ResumePart.objects.all()
        context['portfolio_part_items'] = PortfolioPart.objects.all()
        context['service_part_items'] = ServicePart.objects.all()
        context['testimonial_part_items'] = TestimonialPart.objects.all()
        context['contact_part_items'] = ContactPart.objects.all()

        return context
