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

            # Handle ForeignKey fields
            for field_name, value in fields.items():
                if isinstance(value, dict) and 'model' in value and 'pk' in value:
                    foreign_model = apps.get_model(value['model'])
                    foreign_obj = foreign_model.objects.get(pk=value['pk'])
                    fields[field_name] = foreign_obj

            pk = entry.get('pk')
            if pk:
                obj, created = model.objects.update_or_create(pk=pk, defaults=fields)
            else:
                obj, created = model.objects.get_or_create(**fields)

        self.stdout.write(self.style.SUCCESS('Successfully loaded data from YAML'))
