from cv_app.static_models.static_models import BaseModel


class AboutPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"


class FactPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Fact"
        verbose_name_plural = "Facts"


class SkillPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"


class ResumePart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"


class PortfolioPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"


class ServicePart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class TestimonialPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class ContactPart(BaseModel):

    def __str__(self):
        return self.part_name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
