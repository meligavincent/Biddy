import yaml
from django.core.management.base import BaseCommand
from django.apps import apps

class Command(BaseCommand):
    help = 'Load data from a YAML file into the database'

    def add_arguments(self, parser):
        parser.add_argument('yaml_file', type=str, help='The path to the YAML file')

    def handle(self, *args, **kwargs):
        yaml_file = kwargs['yaml_file']

        with open(yaml_file, 'r') as file:
            data = yaml.safe_load(file)

        for entry in data:
            model = apps.get_model(entry['model'])
            fields = entry['fields']
            pk = entry.get('pk')
            if pk:
                obj, created = model.objects.update_or_create(pk=pk, defaults=fields)
            else:
                obj, created = model.objects.get_or_create(**fields)

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from YAML'))
