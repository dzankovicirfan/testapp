# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import re
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError

from recruiting.models import Vacancy


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
            # print(item.prettify())
            title = item.find('h4').contents[0]
            company = item.find('div', {'class': 'tr-overflow-ellipsis'}).find('span').contents[0]
            image = item.find('img')
            image = image['src'] if image else None
            right_div = item.find(
                'div',
                {'class': 'tr-grid__item tr-sm-w-1/2 tr-lg-w-1/3 tr-hidden-xs-down'}
            )
            right_div = right_div.find_all('li', {'class': 'tr-list__item'})
            start_date = self.format_date(right_div[0].contents[-1].strip())
            end_date = self.format_date(right_div[2].contents[-1].strip())
            location = right_div[1].contents[-1].strip()
            data = {
                'title': title,
                'location': location,
                'start_at': start_date,
                'ends_at': end_date,
                'image_list': image,
                'company': company
            }
            print(location)

            # start_date = right_div[]
            # title = item.find('a')
            # print(start_date)           # company = item.find('span', {'class': 'tr-text+ tr-text+--none-responsive tr-front-family-display'})
            # print(block)
            # print(company)

        self.stdout.write(self.style.SUCCESS('Successfully parsed data.'))

    def format_date(self, string):
        try:
            return datetime.strptime(string, '%d.%m.%Y').date()
        except ValueError:
            if bool(re.search(r'\d', string)):
                num_months = string.split()[0]

                return num_months

        return None
