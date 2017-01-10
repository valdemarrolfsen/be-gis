from django.contrib import admin
from .models import Tutorial, Step, Objective, Result


# Register your models here.

@admin.register(Tutorial)
class TutorialAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'step_count']


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ['type', 'case']


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'tutorial']
