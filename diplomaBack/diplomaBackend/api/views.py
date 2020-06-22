from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from .serializers import (
    CompanyReadSerializer, CompanyWriteSerializer,
    PersonReadSerializer, PersonWriteSerializer,
    ContactReadSerializer, ContactWriteSerializer,
    BuyerReadSerializer, BuyerWriteSerializer,
    RoleReadSerializer, RoleWriteSerializer,
    EmployeeReadSerializer, EmployeeWriteSerializer,
    CompanyTypeReadSerializer, CompanyTypeWriteSerializer,
    RevenueReadSerializer, RevenueWriteSerializer,
    StatusReadSerializer, StatusWriteSerializer,
    CompanyStatusReadSerializer, CompanyStatusWriteSerializer,
    ActionTypeReadSerializer, ActionTypeWriteSerializer,
    BusinessModelReadSerializer, BusinessModelWriteSerializer,
    IndustryCategoryReadSerializer, IndustryCategoryWriteSerializer,
    ResearchReadSerializer, ResearchWriteSerializer,
    PhotoReadSerializer, PhotoWriteSerializer,
    ActionReadSerializer, ActionWriteSerializer
)
from ..models import (
    Company, Person, Contact,
    Buyer, Role, Employee,
    CompanyType, Revenue, 
    Status, CompanyStatus,
    ActionType, BusinessModel,
    IndustryCategory, Research,
    Photo, Action
)
from django_filters import rest_framework as filters

class RoleFilter(filters.FilterSet):
    class Meta:
        model = Role
        fields = ('name', 'slug')

class CompanyFilter(filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            'legal_name': ['icontains'],
            'abbr_name': ['icontains'],
            'phone': ['icontains'],
            'employees_number': ['lte', 'gte', 'exact'],
            'contacts__person__sur_name': ['icontains'],
            'contacts__person__first_name': ['icontains'],
            'contacts__person__email': ['icontains'],
            'contacts__person__phone': ['icontains'],
            'address': ['icontains'],
            'city': ['icontains'],
            'district': ['icontains'],
            'postcode': ['exact'],
            'company_type__name': ['icontains'],
            'parent__legal_name': ['icontains'],
            'parent__abbr_name': ['icontains'],
            'parent__address': ['icontains'],
            'parent__city': ['icontains'],
            'parent__description': ['icontains'],
            'parent__employees_number': ['lte', 'gte', 'exact'],
            'parent__stock_value': ['lte', 'gte', ],
            'parent__web': ['icontains'],
            'parent__foundation_date': ['lte', 'gte', 'exact'],
            'employees_number': ['lte', 'gte', 'exact'],
            'description': ['icontains'],
            'revenue__current': ['lte', 'gte', 'exact'],
            'revenue__min_value': ['lte', 'gte', 'exact'],
            'revenue__max_value': ['lte', 'gte', 'exact'],
            'stock_value': ['lte', 'gte', ],
            'owner__person__sur_name': ['icontains'],
            'owner__person__first_name': ['icontains'],
            'owner__person__email': ['icontains'],
            'owner__person__phone': ['icontains'],
            'company_status__current_status__stage_number': ['lte', 'gte', 'exact'],
            'company_status__current_status__name': ['icontains'],
            'web': ['icontains'],
            'business_models__name': ['icontains'],
            'industry_categories__name': ['icontains'],
            'foundation_date':  ['lte', 'gte', 'exact']
        }

# Company
class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyReadSerializer
    filterset_class = CompanyFilter
    paginate_by = 1



class CompanyDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Company.objects.all()
    serializer_class = CompanyReadSerializer


class CompanyDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Company.objects.all()
    serializer_class = CompanyReadSerializer


class CompanyCreateView(CreateAPIView):
    serializer_class = CompanyWriteSerializer


class CompanyUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Company.objects.all()
    serializer_class = CompanyWriteSerializer


# Person
class PersonListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonReadSerializer


class PersonDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Person.objects.all()
    serializer_class = PersonReadSerializer


class PersonDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Person.objects.all()
    serializer_class = PersonReadSerializer


class PersonCreateView(CreateAPIView):
    serializer_class = PersonWriteSerializer


class PersonUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Person.objects.all()
    serializer_class = PersonWriteSerializer


# Contact
class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactReadSerializer


class ContactDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactReadSerializer


class ContactDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactReadSerializer


class ContactCreateView(CreateAPIView):
    serializer_class = ContactWriteSerializer


class ContactUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Contact.objects.all()
    serializer_class = ContactWriteSerializer


# Buyer
class BuyerListView(ListAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerReadSerializer


class BuyerDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Buyer.objects.all()
    serializer_class = BuyerReadSerializer


class BuyerDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Buyer.objects.all()
    serializer_class = BuyerReadSerializer


class BuyerCreateView(CreateAPIView):
    serializer_class = BuyerWriteSerializer


class BuyerUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Buyer.objects.all()
    serializer_class = BuyerWriteSerializer

 
# Role
class RoleListView(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleReadSerializer
    filterset_class = RoleFilter


class RoleDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Role.objects.all()
    serializer_class = RoleReadSerializer


class RoleDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Role.objects.all()
    serializer_class = RoleReadSerializer


class RoleCreateView(CreateAPIView):
    serializer_class = RoleWriteSerializer


class RoleUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Role.objects.all()
    serializer_class = RoleWriteSerializer

 
# Employee
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeReadSerializer


class EmployeeDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Employee.objects.all()
    serializer_class = EmployeeReadSerializer


class EmployeeDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Employee.objects.all()
    serializer_class = EmployeeReadSerializer


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeWriteSerializer


class EmployeeUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Employee.objects.all()
    serializer_class = EmployeeWriteSerializer

 
# CompanyType
class CompanyTypeListView(ListAPIView):
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeReadSerializer


class CompanyTypeDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeReadSerializer


class CompanyTypeDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeReadSerializer


class CompanyTypeCreateView(CreateAPIView):
    serializer_class = CompanyTypeWriteSerializer


class CompanyTypeUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = CompanyType.objects.all()
    serializer_class = CompanyTypeWriteSerializer

 
# Revenue
class RevenueListView(ListAPIView):
    queryset = Revenue.objects.all()
    serializer_class = RevenueReadSerializer


class RevenueDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Revenue.objects.all()
    serializer_class = RevenueReadSerializer


class RevenueDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Revenue.objects.all()
    serializer_class = RevenueReadSerializer


class RevenueCreateView(CreateAPIView):
    serializer_class = RevenueWriteSerializer


class RevenueUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Revenue.objects.all()
    serializer_class = RevenueWriteSerializer

 
# Status
class StatusListView(ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusReadSerializer


class StatusDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Status.objects.all()
    serializer_class = StatusReadSerializer


class StatusDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Status.objects.all()
    serializer_class = StatusReadSerializer


class StatusCreateView(CreateAPIView):
    serializer_class = StatusWriteSerializer


class StatusUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Status.objects.all()
    serializer_class = StatusWriteSerializer

 
# CompanyStatus
class CompanyStatusListView(ListAPIView):
    queryset = CompanyStatus.objects.all()
    serializer_class = CompanyStatusReadSerializer


class CompanyStatusDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = CompanyStatus.objects.all()
    serializer_class = CompanyStatusReadSerializer


class CompanyStatusDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = CompanyStatus.objects.all()
    serializer_class = CompanyStatusReadSerializer


class CompanyStatusCreateView(CreateAPIView):
    serializer_class = CompanyStatusWriteSerializer


class CompanyStatusUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = CompanyStatus.objects.all()
    serializer_class = CompanyStatusWriteSerializer

 
# ActionType
class ActionTypeListView(ListAPIView):
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeReadSerializer


class ActionTypeDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeReadSerializer


class ActionTypeDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeReadSerializer


class ActionTypeCreateView(CreateAPIView):
    serializer_class = ActionTypeWriteSerializer


class ActionTypeUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = ActionType.objects.all()
    serializer_class = ActionTypeWriteSerializer

 
# BusinessModel
class BusinessModelListView(ListAPIView):
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessModelReadSerializer


class BusinessModelDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessModelReadSerializer


class BusinessModelDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessModelReadSerializer


class BusinessModelCreateView(CreateAPIView):
    serializer_class = BusinessModelWriteSerializer


class BusinessModelUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = BusinessModel.objects.all()
    serializer_class = BusinessModelWriteSerializer

 
# IndustryCategory
class IndustryCategoryListView(ListAPIView):
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategoryReadSerializer


class IndustryCategoryDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategoryReadSerializer


class IndustryCategoryDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategoryReadSerializer


class IndustryCategoryCreateView(CreateAPIView):
    serializer_class = IndustryCategoryWriteSerializer


class IndustryCategoryUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategoryWriteSerializer

 
# Research
class ResearchListView(ListAPIView):
    queryset = Research.objects.all()
    serializer_class = ResearchReadSerializer


class ResearchDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Research.objects.all()
    serializer_class = ResearchReadSerializer


class ResearchDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Research.objects.all()
    serializer_class = ResearchReadSerializer


class ResearchCreateView(CreateAPIView):
    serializer_class = ResearchWriteSerializer


class ResearchUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Research.objects.all()
    serializer_class = ResearchWriteSerializer

 
# Photo
class PhotoListView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoReadSerializer


class PhotoDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Photo.objects.all()
    serializer_class = PhotoReadSerializer


class PhotoDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Photo.objects.all()
    serializer_class = PhotoReadSerializer


class PhotoCreateView(CreateAPIView):
    serializer_class = PhotoWriteSerializer


class PhotoUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Photo.objects.all()
    serializer_class = PhotoWriteSerializer

 
# Action
class ActionListView(ListAPIView):
    queryset = Action.objects.all()
    serializer_class = ActionReadSerializer


class ActionDetailView(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Action.objects.all()
    serializer_class = ActionReadSerializer


class ActionDeleteView(DestroyAPIView):
    lookup_field = 'pk'
    queryset = Action.objects.all()
    serializer_class = ActionReadSerializer


class ActionCreateView(CreateAPIView):
    serializer_class = ActionWriteSerializer


class ActionUpdateView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    queryset = Action.objects.all()
    serializer_class = ActionWriteSerializer

 