# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from recruiting.models import Vacancy, City, Company


class VacancyAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['title']
    search_fields = ['title']


class CompanyAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['name']
    search_fields = ['name']


class CityAdmin(admin.ModelAdmin):
    list_display = list_display_links = ['name']
    search_fields = ['name']


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(City, CityAdmin)
