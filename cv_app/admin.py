from django.contrib import admin
from cv_app.models import *
from cv_app.static_models.static_models import *

admin.site.register(About),
admin.site.register(Fact),
admin.site.register(Skills),
admin.site.register(Resume),
admin.site.register(Portfolio),
admin.site.register(Service),
admin.site.register(Testimonials),
admin.site.register(ContactMessage),

# STATIC MODELS
admin.site.register(AboutMe),
admin.site.register(ContactMe),
admin.site.register(LeftSide),

