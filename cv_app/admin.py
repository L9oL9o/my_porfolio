from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline

from cv_app.models import *
from cv_app.static_models.info_models import *
from cv_app.static_models.partition_models import *


class AboutAdmin(ModelAdmin):
    list_display = ('job_title', 'job_desc', 'degree')


class FactAdmin(ModelAdmin):
    list_display = ('fact_count', 'fact_logo')


class SkillsAdmin(ModelAdmin):
    list_display = ('name', 'percent')


class SummaryAdmin(ModelAdmin):
    list_display = ('name', 'part', 'number', 'email')


class EducationAdmin(ModelAdmin):
    list_display = ('name', 'place_name')


class ExperienceAdmin(ModelAdmin):
    list_display = ('name', 'place_name')


class CategoryPortfolioAdmin(ModelAdmin):
    list_display = ('title', 'slug')


class PortfolioImagesItemTabular(StackedInline):
    model = PortfolioImages
    max_num = 3
    min_num = 3
    extra = 3


class PortfolioAdmin(ModelAdmin):
    list_display = ('name', 'category', 'slug')
    inlines = [
        PortfolioImagesItemTabular,
    ]


class ProjectImageAdmin(ModelAdmin):
    list_display = ('name',)

    def display_image(self, obj):
        return obj.image.url if obj.image else None

    display_image.short_description = 'Image'


class ServiceAdmin(ModelAdmin):
    list_display = ('name', 'desc')


class TestimonialsAdmin(ModelAdmin):
    list_display = ('user_name', 'user_second_name', 'user_job_name', 'user_comment')


class GetContactAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject')


admin.site.register(ContactMessage, GetContactAdmin)

admin.site.register(About, AboutAdmin),
admin.site.register(Fact, FactAdmin),
admin.site.register(Skills, SkillsAdmin),
admin.site.register(Summary, SummaryAdmin),
admin.site.register(Education, EducationAdmin),
admin.site.register(Experience, ExperienceAdmin),
admin.site.register(CategoryPortfolio, CategoryPortfolioAdmin),
admin.site.register(Portfolio, PortfolioAdmin),
admin.site.register(Service, ServiceAdmin),
# admin.site.register(Project, ProjectImageAdmin),
admin.site.register(PortfolioImages, ProjectImageAdmin),


# admin.site.register(Testimonials, TestimonialsAdmin),


# ~~~~~~~~~~~~~~~~~ INFO MODELS ~~~~~~~~~~~~~~~~~~~~~~~
class AboutMeAdmin(ModelAdmin):
    list_display = ('name', 'second_name', 'age', 'birthday')


class ContactMeAdmin(ModelAdmin):
    list_display = ('city',)


class LeftSideAdmin(ModelAdmin):
    list_display = 'twitter_link',


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(LeftSide, LeftSideAdmin)
admin.site.register(ContactMe, ContactMeAdmin)


# ~~~~~~~~~~~~~~~~~~ PARTITION PART MODELS ~~~~~~~~~~~~~~~~~~~~~~~~~~~

class AboutPartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class FactPartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class SkillPartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class ResumePartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class ResumeBlockAdmin(ModelAdmin):
    list_display = ('summary', 'education', 'experience')


class PortfolioPartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class ServicePartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class TestimonialPartAdmin(ModelAdmin):
    list_display = ('name', 'title')


class ContactPartAdmin(ModelAdmin):
    list_display = ('name', 'title')


admin.site.register(AboutPart, AboutPartAdmin),
admin.site.register(FactPart, FactPartAdmin),
admin.site.register(SkillPart, SkillPartAdmin),
admin.site.register(ResumePart, ResumePartAdmin),
admin.site.register(ResumeBlocks, ResumeBlockAdmin),
admin.site.register(PortfolioPart, PortfolioPartAdmin),
admin.site.register(ServicePart, ServicePartAdmin),
admin.site.register(TestimonialPart, TestimonialPartAdmin),
admin.site.register(ContactPart, ContactPartAdmin),

# #
# class AboutPartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to AboutPart
#
#
# class FactPartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to FactPart
#
#
# class SkillPartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to SkillPart
#
#
# class ResumePartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to ResumePart
#
#
# class PortfolioPartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to PortfolioPart
#
#
# class ServicePartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to ServicePart
#
#
# class TestimonialPartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to TestimonialPart
#
#
# class ContactPartAdmin(BaseModelAdmin):
#     list_display = ['other_field1', 'other_field2']  # Add other fields specific to ContactPart
#


# admin.site.register(AboutPart)
# admin.site.register(FactPart)
# admin.site.register(SkillPart)
# admin.site.register(ResumePart)
# admin.site.register(PortfolioPart)
# admin.site.register(ServicePart)
# admin.site.register(TestimonialPart)
# admin.site.register(ContactPart)
