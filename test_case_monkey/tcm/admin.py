from django.contrib import admin

from . import models


class TestScenarioTemplateAttributeInline(admin.TabularInline):
    model = models.TestScenarioTemplateAttribute


class TestScenarioTemplateAdmin(admin.ModelAdmin):
    inlines = (TestScenarioTemplateAttributeInline, )


class TestScenarioAttributeInline(admin.TabularInline):
    model = models.TestScenarioAttribute


class TestScenarioAdmin(admin.ModelAdmin):
    inlines = (TestScenarioAttributeInline, )


admin.site.register(models.Organisation)
admin.site.register(models.Project)
admin.site.register(models.TestRun)
admin.site.register(models.TestScenarioTemplate, TestScenarioTemplateAdmin)
admin.site.register(models.TestScenario, TestScenarioAdmin)
# admin.site.register(models.TestScenarioTemplateAttribute)
# admin.site.register(models.TestScenarioAttribute)
admin.site.register(models.TestCaseTemplate)
admin.site.register(models.TestCase)
admin.site.register(models.Bug)
