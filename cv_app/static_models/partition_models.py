from django.db.models import *


class BaseModel(Model):
    name = CharField(max_length=255, null=True, blank=True)
    title = CharField(max_length=255, null=True, blank=True)

    class Meta:
        abstract = True


class AboutPart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About Static Part"


class FactPart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Fact Static Part"


class SkillPart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skill Static Part"


class ResumePart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Resume Static Part"


class ResumeBlocks(Model):
    summary = CharField(max_length=55, null=True, blank=True)
    education = CharField(max_length=55, null=True, blank=True)
    experience = CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name_plural = "Resume Block Static Parts"


class PortfolioPart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Portfolio Static Part"


class ServicePart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Service Static Part"


class TestimonialPart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Testimonial Static Part"


class ContactPart(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Static Part"
