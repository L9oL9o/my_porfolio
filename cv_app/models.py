from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import *
from mptt.models import MPTTModel

from cv_app.static_models.info_models import AboutMe, ContactMe


class About(Model):
    DEGREE_CHOICES = [
        ("No degree", "No degree"),
        ("Bachelor's", "Bachelor's"),
        ("Master's", "Master's"),
        ("Doctor's", "Doctor's"),
    ]
    JOB_TYPE = [
        ("Full Time", "Full Time"),
        ("Part Time", "Part Time"),
        ("Freelance", "Freelance"),
        ("Remote", "Remote"),
        ("Other", "Other"),
    ]

    job_title = CharField(max_length=255, null=True, blank=True)
    job_desc = CharField(max_length=255, null=True, blank=True)
    website = URLField()
    degree = CharField(max_length=255, choices=DEGREE_CHOICES, null=True, blank=True)
    job_type = CharField(max_length=255, choices=JOB_TYPE, null=True, blank=True)
    about = CharField(max_length=255, null=True, blank=True)
    detail_description = TextField(null=True, blank=True)


    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name_plural = "About Model"


class Fact(Model):
    fact_count = IntegerField(null=True, blank=True)
    fact_short_text = CharField(max_length=255, null=True, blank=True)
    fact_logo = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.fact_short_text

    class Meta:
        verbose_name_plural = "Fact Model"


class Skills(Model):
    name = CharField(max_length=55, null=True, blank=True)
    percent = IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill Model"


class Summary(Model):
    name = ForeignKey(AboutMe, CASCADE, related_name='summary_name', null=True, blank=True)
    part = CharField(max_length=55, null=True, blank=True)
    desc = TextField(null=True, blank=True)
    place = ForeignKey(ContactMe, CASCADE, related_name='summary_place', null=True, blank=True)
    number = ForeignKey(ContactMe, CASCADE, related_name='summary_number', null=True, blank=True)
    email = ForeignKey(ContactMe, CASCADE, related_name='summary_email', null=True, blank=True)

    def __str__(self):
        return self.part

    class Meta:
        verbose_name_plural = "Summary Model"


class Education(Model):
    name = CharField(max_length=100, null=True, blank=True)
    year = DateField(null=True, blank=True)
    end_year = DateField(null=True, blank=True)
    place_name = CharField(max_length=100, null=True, blank=True)
    desc = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Education Model"


class Experience(Model):
    name = CharField(max_length=55, null=True, blank=True)
    start_year = DateField(null=True, blank=True)
    end_year = DateField(null=True, blank=True)
    place_name = CharField(max_length=55, null=True, blank=True)
    experience_desc = RichTextUploadingField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Experience Model"


class CategoryPortfolio(Model):
    title = CharField(max_length=55, null=True, blank=True)
    slug = SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Portfolio Category Model"


class Portfolio(Model):
    name = CharField(max_length=55, null=True, blank=True)
    client = CharField(max_length=55, null=True, blank=True)
    date = DateField(null=True, blank=True)
    url = URLField(blank=True, null=True)
    title = CharField(max_length=255, null=True, blank=True)
    description = TextField(null=True, blank=True)
    img = ImageField(upload_to='static/images/portfolio_images/', null=True, blank=True)
    category = ForeignKey(CategoryPortfolio, on_delete=CASCADE, null=True, blank=True)
    slug = SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"Project name = {self.name}"

    class Meta:
        verbose_name_plural = "Portfolio Model"


# class Project(Model):
#     portfolio = ForeignKey(Portfolio, CASCADE, related_name='portfolio_projects', null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.name} {self.title} {self.client}'
#
#     class Meta:
#         verbose_name_plural = "Project Detail Model"


class PortfolioImages(Model):
    slug = ForeignKey(Portfolio, CASCADE, related_name='portfolio_images', null=True, blank=True)
    name = CharField(max_length=55, null=True, blank=True)
    image = ImageField(upload_to="static/images/project_detail_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} "

    class Meta:
        verbose_name_plural = "Project Images Model"


class Service(Model):
    name = CharField(max_length=255, null=True, blank=True)
    desc = CharField(max_length=255, null=True, blank=True)
    logo = CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Service Model"


class Testimonials(Model):
    user_comment = CharField(max_length=255, null=True, blank=True)
    user_img = ImageField(upload_to="static/images/testimonials", null=True, blank=True)
    user_name = CharField(max_length=55, null=True, blank=True)
    user_second_name = CharField(max_length=55, null=True, blank=True)
    user_job_name = CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return f" {self.user_name} {self.user_second_name}"

    class Meta:
        verbose_name_plural = "Testimonial Model"


class GetContactMessage(Model):
    name = CharField(max_length=255, null=True, blank=True)
    email = EmailField(null=True, blank=True)
    subject = CharField(max_length=255, null=True, blank=True)
    message = TextField(null=True, blank=True)

    def __str__(self):
        return f"Name {self.name} Email {self.email}"

    class Meta:
        verbose_name_plural = "1Get Contact Model"
