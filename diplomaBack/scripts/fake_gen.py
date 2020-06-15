import os
import django
import random
from faker import Faker
from diplomaBackend.models import (Person, Revenue, Company, Contact,
                                    CompanyType, IndustryCategory,
                                    BusinessModel, CompanyStatus)

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

    return r

def gen_contact(person):
    contact = Contact.objects.create(
        person=person
    )
    contact.save()

    return contact


def populate(n=5):
    for entry in range(n):
        owner = gen_contact(gen_person())
        contact1 = gen_contact(gen_person())
        contact2 = gen_contact(gen_person())
        revenue = gen_revenue()

        company_type = CompanyType.objects.get(pk=1)
        ind_category = IndustryCategory.objects.get(pk=1)
        business_model = BusinessModel.objects.get(pk=fakegen.random_int(min=1, max=3))
        company_status = CompanyStatus.objects.get(pk=1)

        legal_name = fakegen.company()
        abbr_name = f'{legal_name[0]}{legal_name[1]}'.upper()
        phone = fakegen.phone_number()
        address = fakegen.address()
        city = fakegen.city()
        postcode = fakegen.postcode()
        employees_number = fakegen.random_int(min=10, max=300)
        description = fakegen.paragraphs()[0]
        stocks_cost = fakegen.random_int(min=10, max=500)
        web = fakegen.free_email_domain()
        logo = fakegen.image_url()
        foundation_date = fakegen.date()

        company = Company.objects.create(
            legal_name=legal_name,
            abbr_name=abbr_name,
            phone=phone,
            owner=owner,
            revenue=revenue,
            address=address,
            city=city,
            postcode=postcode,
            employees_number=employees_number,
            description=description,
            stock_value=stocks_cost,
            web=web,
            logo=logo,
            foundation_date=foundation_date,
            company_type=company_type,
            company_status=company_status
        )

        company.contacts.add(contact1, contact2)
        company.business_models.add(business_model)
        company.industry_categories.add(ind_category)
        company.save()

        print(company)

def run():
    print('GENERATING STARTED')
    populate(100)
    print('GENERATING FINISHED')