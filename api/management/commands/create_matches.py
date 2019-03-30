from django.core.management.base import BaseCommand
from api.factories.factory import MatchFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--matches',
            default=200,
            type=int,
            help='The number of fake matches to create.')

    def handle(self, *args, **options):
        for _ in range(options['matches']):
            MatchFactory.create()
