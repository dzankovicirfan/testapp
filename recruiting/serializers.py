# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers

from recruiting.models import Vacancy, Company, City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    location = CitySerializer(read_only=True)

    class Meta:
        model = Company
        fields = ('name', 'location')


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)

    class Meta:
        model = Vacancy
        fields = ('id','is_active', 'title', 'location', 'starts_at', 'duration', 'description', 'image_list', 'company')
