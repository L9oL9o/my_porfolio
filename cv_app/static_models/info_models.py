from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Model, CharField, IntegerField, DateField, ImageField, URLField, EmailField


class AboutMe(Model):
    # Full info about myself
    name = CharField(max_length=255)
    second_name = CharField(max_length=255)
    age = IntegerField(default=18, validators=[MinValueValidator(1), MaxValueValidator(150)])
    birthday = DateField()
    # the image bottom for the left side
    about_part_img = ImageField(upload_to='static/images/info_models/about_me/avatar_photo/')
    # the image bottom for background part
    background_img = ImageField(upload_to='static/images/info_models/about_me/background_photo/')

    def __str__(self):
        return f" {self.name} {self.second_name} {self.age}"

    class Meta:
        verbose_name_plural = "About Me INFO"


class ContactMe(Model):
    # Full info about how to contact me
    address = CharField(max_length=255)
    city = CharField(max_length=55)
    email = EmailField()
    country_code = CharField(max_length=55)
    phone_number = CharField(max_length=200)
    location_coordinate = URLField()

    def __str__(self):
        return f" {self.address} {self.phone_number} {self.email}"

    class Meta:
        verbose_name_plural = "Contact Me INFO"


class LeftSide(Model):
    #   Left side block
    left_side_my_img = ImageField(upload_to='static/images/info_models/left_block_images/')
    twitter_link = URLField(null=True, blank=True)
    facebook_link = URLField(null=True, blank=True)
    instagram_link = URLField(null=True, blank=True)
    skype_link = URLField(null=True, blank=True)
    linkedin_link = URLField(null=True, blank=True)

    def __str__(self):
        return self.twitter_link

    class Meta:
        verbose_name_plural = "Left Side INFO"
