from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):

    sur_name = models.CharField(("Фамилия"), max_length=50)
    first_name = models.CharField(("Имя"), max_length=50)
    middle_name = models.CharField(("Отчество"), max_length=50, blank=True, null=True)
    email = models.EmailField(("E-mail"), max_length=254, blank=True, null=True)
    phone = models.CharField(("Телефон"), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = ("Личность")
        verbose_name_plural = ("Личности")

    def __str__(self):
        return f'{self.sur_name} {self.first_name} {self.middle_name}'

class Contact(models.Model):

    person = models.ForeignKey(Person, verbose_name=("Личность"), related_name="contacts", on_delete=models.CASCADE)
    description = models.TextField(("Описание"), blank=True, null=True)

    class Meta:
        verbose_name = ("Контакт")
        verbose_name_plural = ("Контакты")

    def __str__(self):
        return f'{self.person}'

class Buyer(models.Model):

    person = models.ForeignKey(Person, verbose_name=("Личность"), related_name="buyers", on_delete=models.CASCADE)
    description = models.TextField(("Описание"), blank=True, null=True)
    active = models.BooleanField(("Активен"))

    class Meta:
        verbose_name = ("Покупатель")
        verbose_name_plural = ("Покупатели")

    def __str__(self):
        return f'{self.person} {self.active}'

class Role(models.Model):

    name = models.CharField(("Название"), max_length=50)
    slug = models.SlugField(("Slug"))

    class Meta:
        verbose_name = ("Роль")
        verbose_name_plural = ("Роли")

    def __str__(self):
        return f'{self.name}'

class Employee(models.Model):

    person = models.ForeignKey(Person, verbose_name=("Личность"), related_name="employees", on_delete=models.CASCADE)
    account =  models.OneToOneField(User, verbose_name=("Пользователь"), related_name="employees", on_delete=models.CASCADE)
    role = models.ForeignKey(Role, verbose_name=("Роль"), related_name="employees", on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = ("Работник")
        verbose_name_plural = ("Работники")

    def __str__(self):
        return f'{self.person}'

class CompanyType(models.Model):

    name = models.CharField(("Название"), max_length=50)

    class Meta:
        verbose_name = ("Тип компании")
        verbose_name_plural = ("Типы компаний")

    def __str__(self):
        return f'{self.name}'

class Revenue(models.Model):

    current = models.DecimalField(("Текущий"), max_digits=10, decimal_places=2)
    min_value = models.DecimalField(("Минимальный"), max_digits=10, decimal_places=2, blank=True, null=True)
    max_value = models.DecimalField(("Максимальный"), max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = ("Доход")
        verbose_name_plural = ("Доходы")

    def __str__(self):
        return f'{self.current}'

class Status(models.Model):

    stage_number = models.DecimalField(("Номер этапа"), max_digits=5, decimal_places=2)
    name = models.CharField(("Название"), max_length=50)
    description = models.TextField(("Описание"), blank=True, null=True)

    class Meta:
        verbose_name = ("Статус")
        verbose_name_plural = ("Статусы")

    def __str__(self):
        return f'{self.stage_number} - {self.name}'
        
class CompanyStatus(models.Model):

    current_status = models.ForeignKey(Status, verbose_name=("Текущий статус сделки"), related_name="current_companies_statuses", on_delete=models.CASCADE, blank=True)
    high_status = models.ForeignKey(Status, verbose_name=("Наивысший статус сделки"), related_name="high_companies_statuses", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = ("Статус сделки")
        verbose_name_plural = ("Статусы сделок")

    def __str__(self):
        return f'{self.current_status}; {self.high_status}'

class ActionType(models.Model):

    name = models.CharField(("Название"), max_length=50)
    description = models.TextField(("Описание"), blank=True, null=True)

    class Meta:
        verbose_name = ("Тип действия")
        verbose_name_plural = ("Типы действий")

    def __str__(self):
        return f'{self.name}'

class BusinessModel(models.Model):

    name = models.CharField(("Название"), max_length=50)
    description = models.TextField(("Описание"), blank=True, null=True)

    class Meta:
        verbose_name = ("Бизнес модель")
        verbose_name_plural = ("Бизнес модели")

    def __str__(self):
        return f'{self.name}'

class IndustryCategory(models.Model):

    name = models.CharField(("Название"), max_length=50)
    description = models.TextField(("Описание"), blank=True, null=True)

    class Meta:
        verbose_name = ("Категория промышленности")
        verbose_name_plural = ("Категории промышленности")

    def __str__(self):
        return f'{self.name}'

class Company(models.Model):

    legal_name = models.CharField(("Юридическое имя"), max_length=100)
    abbr_name = models.CharField(("Аббревиатура"), max_length=100)
    phone = models.CharField(("Телефон"), max_length=20, blank=True, null=True)
    contacts = models.ManyToManyField(Contact, verbose_name=("Контакты"), related_name="contact_companies")
    address = models.CharField(("Адрес"), max_length=100, blank=True, null=True)
    city = models.CharField(("Город"), max_length=50)
    district = models.CharField(("Район"), max_length=50, blank=True, null=True) 
    postcode = models.IntegerField(("Индекс"), blank=True, null=True)
    company_type = models.ForeignKey(CompanyType, verbose_name=("Тип компании"), related_name="companies", on_delete=models.SET_NULL, blank=True, null=True)
    parent = models.ForeignKey('self', verbose_name=("Родительская компания"), related_name="companies", on_delete=models.SET_NULL, blank=True, null=True)
    employees_number = models.IntegerField(("Количество сотрудников"), blank=True, null=True)
    description = models.TextField(("Описание"), blank=True, null=True)
    revenue = models.OneToOneField(Revenue, verbose_name=("Доход"), related_name="companies", on_delete=models.PROTECT, blank=True, null=True)
    stock_value = models.DecimalField(("Стоимость акций"), max_digits=10, decimal_places=2)
    owner = models.ForeignKey(Contact, verbose_name=("Владелец"), related_name="owned_companies", on_delete=models.PROTECT, blank=True, null=True)
    company_status = models.ForeignKey(CompanyStatus, verbose_name=("Статус сделки"), related_name="companies", on_delete=models.PROTECT, blank=True, null=True)
    logo = models.CharField(("Логотип"), max_length=200)
    web = models.CharField(("Web-сайт"), max_length = 200, blank=True, null=True)
    business_models = models.ManyToManyField(BusinessModel, verbose_name=("Бизнес модели"))
    industry_categories = models.ManyToManyField(IndustryCategory, verbose_name=("Категории промышленности"))
    buyers = models.ManyToManyField(Buyer, verbose_name=("Потенциальные покупатели"), related_name="buyer_companies", blank=True)
    active_buyer = models.ForeignKey(Buyer, verbose_name=("Активный покупатель"), related_name="active_buyer_companies", on_delete=models.SET_NULL, blank=True, null=True)
    foundation_date = models.DateField(("Дата основания компании"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = ("Компания")
        verbose_name_plural = ("Компании")

    def __str__(self):
        return f'{self.legal_name}'

class Research(models.Model):

    research_date = models.DateField(("Дата"), auto_now=False, auto_now_add=True)
    researcher = models.ForeignKey(Employee, verbose_name=("Работник"), related_name="researches", on_delete=models.SET_NULL, null=True)
    reasearch_note = models.TextField(("Заметка"), blank=True, null=True)
    company = models.ForeignKey(Company, verbose_name=("Компания"), related_name="company_researches", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Исследование")
        verbose_name_plural = ("Исследования")

    def __str__(self):
        return f'{self.research_date} {self.researcher}'

class Photo(models.Model):

    company = models.ForeignKey(Company, verbose_name=("Компания"), related_name="photo", on_delete=models.CASCADE)
    image = models.CharField(("Изображение"), max_length=250)
    
    class Meta:
        verbose_name = ("Фотография")
        verbose_name_plural = ("Фотографии")

    def __str__(self):
        return f'{self.company}'

class Action(models.Model):

    action_type = models.ForeignKey(ActionType, verbose_name=("Тип действия"), related_name="actions", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, verbose_name=("Компания"), related_name="actions", on_delete=models.CASCADE)
    date = models.DateField(("Дата"), auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Действие")
        verbose_name_plural = ("Действия")

    def __str__(self):
        return f'{self.action_type} {self.company}'


