# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class VacancyQuerySet(models.QuerySet):
    def is_active(self):
        return self.filter(is_active=True)


class VacancyManager(models.Manager):
    def get_queryset(self):
        return VacancyQuerySet(self.model, using=self._db)

    def is_active(self):
        return self.get_queryset().is_active()
