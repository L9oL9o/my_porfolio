from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import *


class About(Model):
    part_name = CharField(max_length=255)
    part_title = CharField(max_length=255)
    PHONE_CHOICES = [
        ("Uzb ", "+998"),
        ("Usa", "+1"),
        ("Ru", "+7"),
        ("Eng", "+44"),
        ("Fr", "+33"),
        ("Ca", "+1"),
    ]
    DEGREE_CHOICES = [
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
    phone_code = CharField(max_length=55, choices=PHONE_CHOICES)
    phone_number = CharField(max_length=55)
    city = CharField(max_length=255)
    age = IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(150)])
    degree = CharField(max_length=255, choices=DEGREE_CHOICES)
    email_field = EmailField()
    job_type = CharField(max_length=255, choices=JOB_TYPE)
    about_job = CharField(max_length=255)

    def __str__(self):
        return self.job_name

    class Meta:
        verbose_name = "About"


class Fact(Model):
    part_name = CharField(max_length=255)
    part_title = CharField(max_length=255)
    img = ImageField(upload_to='images/fact')
    count = IntegerField()
    short_text = CharField(max_length=255)

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Fact"



# class Skills(Model):
#     part_name = CharField(max_length=255)
#     part_title = CharField(max_length=255)
#
#     skill_name = CharField(max_length=255)
#     skill_duration = DateTimeField(null=True, blank=True)
#     skill_place = CharField(max_length=255)
#     skill_detail = JSONField()



