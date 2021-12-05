import xlrd
from django.core.management.base import BaseCommand
from lopez.models import Movie

SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

class Command(BaseCommand):
    help = (
        "Imports movies from a local XLS file."
        "Expects title, URL and release year."
    )
    def add_arguments(self, parser):
        parser.add_argument(
            'file_path',
            nargs=1,
            type=str
        )
    def handle(self, *args, **options):
        verbosity = options.get('verbosity', NORMAL)
        file_path = options['file_path'][0]

        wb = xlrd.open_workbook(file_path)
        sh = wb.sheet_by_index(0)

        if verbosity >= NORMAL:
            self.stdout.write('=== Movies imported ===')
        for rownum in range(sh.nrows):
            if rownum == 0:
                continue
            (title, url, release_year) = sh.row_values(rownum)
            movie, created = Movie.objects.get_or_create(
                title=title, url=url, release_year=release_year
            )
            if verbosity >= NORMAL:
                self.stdout.write(f'{rownum}. {movie.title}')

