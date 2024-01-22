from cv_app.static_models.static_models import BaseModel
from django.db.models import *


# class BaseModel(Model):
#     part_name = CharField(max_length=255, null=True, blank=True)
#     part_title = CharField(max_length=255, null=True, blank=True)
#


class AboutPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Static Part"


class FactPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Fact"
        verbose_name_plural = "Fact Static Part"


class SkillPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skill Static Part"


class ResumePart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resume Static Part"


class PortfolioPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio Static Part"


class ServicePart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Service Static Part"


class TestimonialPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonial Static Part"


class ContactPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact Static Part"
