from django.shortcuts import render
from django.views.generic import ListView

from cv_app.models import *
from cv_app.static_models.info_models import *
from cv_app.static_models.partition_models import *
from root.settings import MEDIA_URL


class GetObjectsView(ListView):
    queryset = About.objects.all()
    # template_name = ('portfolio-details.html', 'portfolio-details.html')
    template_name = 'index.html'
    context_object_name = 'about_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['facts_item'] = Fact.objects.all()
        context['skills_item'] = Skills.objects.all()
        context['summary_items'] = Summary.objects.all()
        context['education_items'] = Education.objects.all()
        context['experience_items'] = Experience.objects.all()
        context['category_portfolio_items'] = CategoryPortfolio.objects.all()
        context['portfolio_items'] = Portfolio.objects.values('category__slug', 'slug', 'img')
        context['service_items'] = Service.objects.all()
        context['testimonials_item'] = Testimonials.objects.all()
        context['full_url'] = self.request.build_absolute_uri(MEDIA_URL)

        # STATIC MODELS
        context['about_me_items'] = AboutMe.objects.all()
        context['contact_me_items'] = ContactMe.objects.all()
        context['left_side_items'] = LeftSide.objects.all()

        # STATIC PARTITION MODELS
        context['about_part_items'] = AboutPart.objects.all()
        context['fact_part_items'] = FactPart.objects.all()
        context['skill_part_items'] = SkillPart.objects.all()
        context['resume_part_items'] = ResumePart.objects.all()
        context['resume_block_items'] = ResumeBlocks.objects.all()
        context['portfolio_part_items'] = PortfolioPart.objects.all()
        context['service_part_items'] = ServicePart.objects.all()
        context['testimonial_part_items'] = TestimonialPart.objects.all()
        context['contact_part_items'] = ContactPart.objects.all()

        return context


def get_project_details(request, slug):
    portfolio = Portfolio.objects.get(slug=slug)
    context = {
        'project_details_item': [portfolio],
        'project_details_images_item': portfolio.portfolio_images.all()
    }

    return render(request, 'portfolio-details.html', context)


def contact_view(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Валидация данных (вы можете добавить свою логику валидации)
        if not name or not email or not subject or not message:
            return render(request, 'index.html', {'error_message': 'All fields are required'})

        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

        return render(request, 'success_page.html')

    return render(request, 'index.html')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ________________________________________________|
# THIS METOD WILL BE USED, BUT NOW IT DIDN'T WORK |
# ------------------------------------------------|
# def contact_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'success_page.html')  # Создайте страницу успешного отправления формы
#     else:
#         form = ContactForm()
#
#     return render(request, 'index.html', {'form': form})
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
