# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

from recruiting.models import Vacancy
from recruiting.serializers import VacancySerializer


class VacancyView(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_field = ('location', 'company')
