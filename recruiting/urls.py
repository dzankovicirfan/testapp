# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from rest_framework import routers

from recruiting.views import VacancyView

router = routers.DefaultRouter()
router.register(r'vacancies', VacancyView)

urlpatterns = [
    url(r'^', include(router.urls)),
]
