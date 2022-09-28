from django.contrib import admin

from . import models

admin.site.register(models.Survey)
admin.site.register(models.Question)
admin.site.register(models.Option)
admin.site.register(models.FormSurvey)
admin.site.register(models.Response)
