import os
import django
import random
from faker import Faker
from diplomaBackend.models import Person, Revenue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplomaBackend.settings')
django.setup()

# FAKE POP SCRIPT
fakegen = Faker(['ru_RU'])

def gen_person():
    p = Person.objects.create()
    p.first_name = fakegen.first_name()
    p.sur_name = fakegen.last_name()
    p.email = f'{fakegen.first_name()}{fakegen.first_name()}@gmail.com'
    p.phone = fakegen.phone_number()
    p.save()

    return p

def gen_revenue():
    r = Revenue.objects.create(
        current=fakegen.random_int(min=2, max=1550000),
        min_value=fakegen.random_int(min=2, max=1550000),
        max_value=fakegen.random_int(min=2, max=1550000)
    )
   
    r.save()


def populate(n=5):
    for entry in range(n):
        owner = gen_person()
        revenue = gen_revenue()

        legal_name = fakegen.company()
        abbr_name = f'{legal_name[0]}{legal_name[1]}'
        phone = fakegen.phone_number()

        print(revenue)
        print(legal_name, abbr_name, phone)

def run():
    print('GENERATING STARTED')
    populate(5)
    print('GENERATING FINISHED')