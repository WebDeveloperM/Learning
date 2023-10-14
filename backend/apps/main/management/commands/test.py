from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "for test"

    def add_arguments(self, parser):
        pass
        # parser.add_argument("--time", action="append", type=str)

    def handle(self, *args, **options):
        pass
