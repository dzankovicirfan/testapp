# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from recruiting.models import Vacancy, Company


class Command(BaseCommand):
    help = 'Parsing vacancies'

    def handle(self, *args, **kwargs):

        url = "https://www.trainee.de/traineestellen/"

        r = requests.get(url)

        soup = BeautifulSoup(r.content, "html.parser")
        content = soup.find('div', {'id': 'jobs'})
        ul = content.find('ul', {'class': 'tr-list'})
        items = ul.find_all('li', {'class': 'tr-list__item'}, recursive=False)[:20]
        for item in items:
            title = item.find('h4').contents[0]
            company = item.find('div', {'class': 'tr-overflow-ellipsis'}).find('span').contents[0]

            image = item.find('img')
            image = image['src'] if image else None

            right_div = item.find(
                'div',
                {'class': 'tr-grid__item tr-sm-w-1/2 tr-lg-w-1/3 tr-hidden-xs-down'}
            )
            right_div = right_div.find_all('li', {'class': 'tr-list__item'})

            start_date = right_div[0].contents[-1].strip()
            duration = right_div[2].contents[-1].strip()

            location = right_div[1].contents[-1].strip()

            description_a = 'https://www.trainee.de' + item.find('a', href=True)['href']
            description_url = requests.get(description_a) 
            description_soup = BeautifulSoup(description_url.content, "html.parser")
            description_content = description_soup.find('div', {'class': 'tr-content tr-box tr-box--default tr-text+ tr-mrgb'}).text
            
            data = {
                'title': title,
                'location': location,
                'starts_at': start_date,
                'duration': duration,
                'description': description_content,
                'image_list': image,
                'company': company
            }
            try:
                company = Company.objects.get(name=company)
            except Company.DoesNotExist:             
                company_create = Company.objects.create(
                    name=company)

            vacancy_create = Vacancy.objects.create(
                is_active=True,
                title=title,
                location=location, 
                starts_at=start_date,
                duration=duration,
                description=description_content,
                company=company_create
            )


        self.stdout.write(self.style.SUCCESS('Successfully parsed data.'))