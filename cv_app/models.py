from django.db.models import *

from cv_app.static_models.static_models import AboutMe, ContactMe


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

    job_title = CharField(max_length=255)
    job_decs = CharField(max_length=255)
    website = URLField()
    phone_code = CharField(max_length=55)
    phone_number = CharField(max_length=55)
    city_name = CharField(max_length=255)
    degree = CharField(max_length=255, choices=DEGREE_CHOICES)
    email_field = EmailField()
    job_type = CharField(max_length=255, choices=JOB_TYPE)
    about_job = CharField(max_length=255)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Model"


class Fact(Model):
    fact_cont = IntegerField()
    fact_short_text = CharField(max_length=255)
    fact_logo = CharField(max_length=255)

    def __str__(self):
        return self.fact_short_text

    class Meta:
        verbose_name = "Fact"
        verbose_name_plural = "Fact Model"


class Skills(Model):
    skill_name = CharField(max_length=55)
    skill_percent = IntegerField()

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skill Model"


class Resume(Model):
    pass


class CategoryPortfolio(Model):
    title = CharField(max_length=55)
    slug = SlugField(unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Portfolio Category"


class Portfolio(Model):
    project_name = CharField(max_length=55, null=True, blank=True)
    portfolio_link = URLField(blank=True, null=True)
    portfolio_img = ImageField(upload_to='static/images/portfolio')
    portfolio_category = ForeignKey(CategoryPortfolio, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Project name = {self.project_name} Category = {self.portfolio_category.title}"

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio Model"


class Service(Model):
    service_name = CharField(max_length=255)
    service_desc = CharField(max_length=255)
    service_logo = CharField(max_length=255)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Service Model"


class Testimonials(Model):
    user_comment = CharField(max_length=255)
    user_img = ImageField(upload_to="static/images/testimonials")
    user_name = CharField(max_length=55)
    user_second_name = CharField(max_length=55)
    user_job_name = CharField(max_length=55)

    def __str__(self):
        return f" {self.user_name} {self.user_second_name}"

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial Model"


class ContactMessage(Model):
    name = CharField(max_length=255)
    email = EmailField()
    subject = CharField(max_length=255)
    message = TextField()

    def __str__(self):
        return f"Name {self.name} Email {self.email}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact Model"


# class Summary(Model):
#     name = ForeignKey(AboutMe, on_delete=CASCADE)
#     summary_desc = TextField()
#     sum_place = ForeignKey(ContactMe.location_name, on_delete=CASCADE)
#     sum_number = ForeignKey(ContactMe.call, on_delete=CASCADE)
#
#
#
#
# class Education(Model):
#     part_name = CharField(max_length=55)
#     edu_name = CharField(max_length=100)
#     edu_year = DateTimeField()
#     edu_end_year = DateTimeField(auto_now=True, null=True, blank=True)
#     edu_place_name = CharField(max_length=100)
#     edu_desc = CharField(max_length=255)
