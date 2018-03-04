# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from .managers import VacancyManager


class City(models.Model):
    name = models.CharField('Name', max_length=100)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return str(self.name)


class Company(models.Model):
    name = models.CharField('Name', max_length=100)
    loacation = models.ForeignKey(
        City, related_name='companies', on_delete=models.CASCADE,
        blank=True, null=True
    )

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'

    def __str__(self):
        return str(self.name)


class Vacancy(models.Model):
    is_active = models.BooleanField('Active', default=False)
    title = models.CharField('Title', max_length=100, blank=True, null=True)
    location = models.CharField(
        'Location', max_length=400, null=True, blank=True
    )
    starts_at = models.CharField(
        'Starts', blank=True, null=True, max_length=40
    )
    duration = models.CharField(
        'Duration(months)', blank=True, null=True, max_length=40
    )
    description = models.TextField(
        'Description', null=True, blank=True, default=None
    )
    image_list = models.ImageField(
        upload_to='media/vacancies/', blank=True, null=True
    )
    company = models.ForeignKey(
        Company, related_name='vacancies', on_delete=models.CASCADE,
        blank=True, null=True
    )

    objects = VacancyManager()

    class Meta:
        verbose_name = 'vacancy'
        verbose_name_plural = 'vacancies'

    def __str__(self):
        return str(self.title)
