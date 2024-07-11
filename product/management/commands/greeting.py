from django.core.management.base import BaseCommand, CommandParser

class Command(BaseCommand):
    help = 'I greet you'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument(
            'name',
            type=str,
            help='Your name to say hello'
        )

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        print(f'Hello {name}')