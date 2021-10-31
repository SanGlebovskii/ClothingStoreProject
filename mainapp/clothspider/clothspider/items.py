import scrapy
from scrapy_djangoitem import DjangoItem

from mainapp.models import Shoes


class ShoesSpiderItem(DjangoItem):
    django_model = Shoes
