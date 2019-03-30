from django.core.management.base import BaseCommand
from api.factories.factory import ExpansionFactory


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--expansions',
            default=200,
            type=int,
            help='The number of fake expansions to create.')

    def handle(self, *args, **options):
        for _ in range(options['expansions']):
            ExpansionFactory.create()
