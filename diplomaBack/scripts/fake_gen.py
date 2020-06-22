import os
import django
import random
from faker import Faker
from diplomaBackend.models import (Person, Revenue, Company, Contact,
                                    CompanyType, IndustryCategory,
                                    BusinessModel, CompanyStatus, Status)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'diplomaBackend.settings')
django.setup()

# FAKE POP SCRIPT
fakegen = Faker(['en_US'])
fakegen_eu = Faker(['en_US'])

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

def gen_company_type():
    c_type = CompanyType.objects.create(
        name=fakegen_eu.company_suffix()
    )
    c_type.save()

    return c_type

def gen_industry_category():
    ind_cat = IndustryCategory.objects.create(
        name=fakegen_eu.company_suffix(),
        description=fakegen.paragraphs()[0],
    )
    ind_cat.save()

    return ind_cat

def gen_business_model():
    b_m = BusinessModel.objects.create(
        name=fakegen_eu.company_suffix(),
        description=fakegen.paragraphs()[0],
    )
    b_m.save()

    return b_m

def gen_status():
    s = Status(
        stage_number=fakegen.random_int(min=0, max=10),
        name=fakegen_eu.company_suffix(),
        description=fakegen.paragraphs()[0],
    )
    s.save()

    return s

def gen_company_status():
    c_s = CompanyStatus.objects.create(
        current_status=gen_status(),
        high_status=gen_status(),
    )
    c_s.save()

    return c_s

def gen_company():
    owner = gen_contact(gen_person())
    contact1 = gen_contact(gen_person())
    contact2 = gen_contact(gen_person())
    revenue = gen_revenue()

    company_type = gen_company_type()
    ind_category = gen_industry_category()
    business_model = gen_business_model()
    company_status = gen_company_status()

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

    return company

def populate(n=5):
    for entry in range(n):
        company = gen_company()
        print(company)

def run():
    print('GENERATING STARTED')
    populate(20)
    print('GENERATING FINISHED')