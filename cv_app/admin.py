from aiogram.types import Contact
from django.contrib.admin import ModelAdmin
from django.contrib import admin
from cv_app.models import *
from cv_app.static_models.static_models import *
from cv_app.static_models.partition_models import *


class AboutAdmin(ModelAdmin):
    list_display = ('job_title', 'job_decs', 'city_name', 'degree')
    # fieldsets = [
    #     ("Basic Model", {"fields": ["job_title", "job_title111"]})
    # ]


class FactAdmin(ModelAdmin):
    list_display = ('fact_cont',)


class SkillsAdmin(ModelAdmin):
    list_display = ('skill_name', 'skill_percent')


# class ResumeAdmin(ModelAdmin):
#     # list_display = ('skill_name', 'skill_percent',)
#     pass


class CategoryPortfolioAdmin(ModelAdmin):
    list_display = ('title', 'slug')


class PortfolioAdmin(ModelAdmin):
    list_display = ('project_name',)


class ServiceAdmin(ModelAdmin):
    list_display = ('service_name', 'service_desc')


class TestimonialsAdmin(ModelAdmin):
    list_display = ('user_name', 'user_second_name', 'user_job_name', 'user_comment')


admin.site.register(About, AboutAdmin),
admin.site.register(Fact, FactAdmin),
admin.site.register(Skills, SkillsAdmin),
admin.site.register(CategoryPortfolio, CategoryPortfolioAdmin),
admin.site.register(Portfolio, PortfolioAdmin),
admin.site.register(Service, ServiceAdmin),
admin.site.register(Testimonials, TestimonialsAdmin),


# ~~~~~~~~~~~~~~~~~ STATIC MODELS ~~~~~~~~~~~~~~~~~~~~~~~
class AboutMeAdmin(ModelAdmin):
    list_display = ('my_name', 'my_second_name', 'my_age', 'my_birthday')


class LeftSideAdmin(ModelAdmin):
    list_display = 'left_side_name',


class ContactAdmin(ModelAdmin):
    list_display = ('location_name',)


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(LeftSide, LeftSideAdmin)
admin.site.register(ContactMe, ContactAdmin)

# admin.site.register(ContactMe, ContactMessage)
# admin.site.register(Resume, ResumeAdmin),

# class ContactMessage(ModelAdmin):
#     list_display = ('user_comment', 'service_desc')


# ~~~~~~~~~~~~~~~~~~ PARTITION PART MODELS ~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# class AboutPartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class FactPartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class SkillPartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class ResumePartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class PortfolioPartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class ServicePartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class TestimonialPartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# class ContactPartAdmin(ModelAdmin):
#     list_display = ('part_name', 'part_title')
#
#
# admin.site.register(AboutPart, AboutAdmin),
# admin.site.register(FactPart, FactAdmin),
# admin.site.register(SkillPart, SkillsAdmin),
# admin.site.register(ResumePart, PortfolioAdmin),
# admin.site.register(PortfolioPart, ServiceAdmin),
# admin.site.register(ServicePart, TestimonialsAdmin),
# admin.site.register(TestimonialPart, TestimonialsAdmin),
# admin.site.register(ContactPart, TestimonialsAdmin),


# class BaseModelAdmin(admin.ModelAdmin):
#     list_display = ['part_name', 'part_title']  # Add other fields as needed
#
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
#
# # Register the admin classes with the corresponding models


admin.site.register(AboutPart)
admin.site.register(FactPart)
admin.site.register(SkillPart)
admin.site.register(ResumePart)
admin.site.register(PortfolioPart)
admin.site.register(ServicePart)
admin.site.register(TestimonialPart)
admin.site.register(ContactPart)
