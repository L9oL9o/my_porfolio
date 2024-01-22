from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import *


class BaseModel(Model):
    part_name = CharField(max_length=255, null=True, blank=True)
    part_title = CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class AboutMe(Model):
    my_name = CharField(max_length=255)
    my_second_name = CharField(max_length=255)
    my_age = IntegerField(default=18, validators=[MinValueValidator(1), MaxValueValidator(150)])
    my_birthday = DateField()
    about_avatar_img = ImageField(upload_to='static/images/static_images/about_avatar_img')
    background_img = ImageField(upload_to='static/images/static_images/background_img')

    def __str__(self):
        return f" {self.my_name} {self.my_second_name} {self.my_age}"

    class Meta:
        # verbose_name = "About Me"
        verbose_name_plural = "About Me Static"


class ContactMe(Model):
    location_name = CharField(max_length=200)
    email = EmailField()
    call = CharField(max_length=200)
    location_coordinate = CharField(max_length=200)

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name_plural = "Contact Me Static"


class LeftSide(Model):
    #   Left side part
    left_side_name = CharField(max_length=55)
    left_side_my_img = ImageField(upload_to='static/images/static_images/left_side_images/')
    twitter_link = URLField(null=True, blank=True)
    facebook_link = URLField(null=True, blank=True)
    instagram_link = URLField(null=True, blank=True)
    skype_link = URLField(null=True, blank=True)
    linkedin_link = URLField(null=True, blank=True)

    def __str__(self):
        return self.left_side_name

    class Meta:
        # verbose_name = "Static"
        verbose_name_plural = "Left Side Static"
