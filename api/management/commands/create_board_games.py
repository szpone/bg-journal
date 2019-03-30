from django.core.management.base import BaseCommand
from api.factories.factory import BoardGameFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--board_games',
            default=200,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['board_games']):
            BoardGameFactory.create()
