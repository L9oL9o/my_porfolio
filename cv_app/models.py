from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import *


class Base(Model):
    part_name = CharField(max_length=255, null=True, blank=True)
    part_title = CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class StaticObjects(Model):
    #   Left side part
    my_name = CharField(max_length=255)
    my_second_name = CharField(max_length=255)
    avatar_img = ImageField(upload_to='static/images/static_images/')
    background_img = ImageField(upload_to='static/images/static_images')
    twitter_link = URLField(null=True, blank=True)
    facebook_link = URLField(null=True, blank=True)
    instagram_link = URLField(null=True, blank=True)
    skype_link = URLField(null=True, blank=True)
    linkedin_link = URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.my_name} {self.my_second_name}"

    class Meta:
        verbose_name = "Static"
        verbose_name_plural = "Statics"


class Contact(Base):
    location = CharField(max_length=255)
    email = EmailField()
    phone_number = CharField(max_length=55)

    def __str__(self):
        return {self.phone_number}

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class About(Base):
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

    img = ImageField(upload_to='static/images/about')
    job_name = CharField(max_length=255)
    job_about = CharField(max_length=255)
    birth_date = DateField()
    website = URLField()
    phone_code = CharField(max_length=55)
    phone_number = CharField(max_length=55)
    city = CharField(max_length=255)
    age = IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(150)])
    degree = CharField(max_length=255, choices=DEGREE_CHOICES)
    email_field = EmailField()
    job_type = CharField(max_length=255, choices=JOB_TYPE)
    about_job = CharField(max_length=255)
    # my_name = CharField(max_length=55)
    # my_second_name = CharField(max_length=55)

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"


class Fact(Base):
    img = ImageField(upload_to='images/fact')
    count = IntegerField()
    short_text = CharField(max_length=255)

    def __str__(self):
        return self.short_text

    class Meta:
        verbose_name = "Fact"
        verbose_name_plural = "Facts"


class Portfolio(Base):
    project_name = CharField(max_length=255, null=True, blank=True)
    project_img = ImageField(upload_to='images/portfolio')
    project_link = URLField(blank=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class Service(Base):
    img = ImageField(upload_to='static/images/services')
    service_name = CharField(max_length=255)
    service_desc = CharField(max_length=255)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Testimonials(Base):
    user_comment = CharField(max_length=255)
    user_img = ImageField(upload_to="static/images/testimonials")
    user_name = CharField(max_length=55)
    user_sec_name = CharField(max_length=55)
    user_job_name = CharField(max_length=55)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


# class Skills(Model):
#     part_name = CharField(max_length=255)
#     part_title = CharField(max_length=255)
#
#     skill_name = CharField(max_length=255)
#     skill_duration = DateTimeField(null=True, blank=True)
#     skill_place = CharField(max_length=255)
#     skill_detail = JSONField()
