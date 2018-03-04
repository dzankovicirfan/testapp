# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.viewsets import ModelViewSet

import django_filters.rest_framework
from rest_framework.permissions import IsAdminUser

from .models import Vacancy
from .serializers import VacancySerializer


class VacancyView(ModelViewSet):
    queryset = Vacancy.objects.is_active()
    serializer_class = VacancySerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_field = ('location', 'company')
    permisssion_classes = (IsAdminUser,)
