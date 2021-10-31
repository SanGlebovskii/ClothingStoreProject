from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from clothspider.clothspider import settings as my_settings

from clothspider.clothspider.spiders.shoes import ShoesSpider


class Command(BaseCommand):
    help = 'Release spider'

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)

        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(ShoesSpider)
        process.start()
