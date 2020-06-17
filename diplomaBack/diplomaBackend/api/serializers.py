from rest_framework import serializers
from ..models import (
    Company, Person, Contact,
    Buyer, Role, Employee,
    CompanyType, Revenue, 
    Status, CompanyStatus,
    ActionType, BusinessModel,
    IndustryCategory, Research,
    Photo, Action
)

class CompanyReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        depth = 2

class CompanyWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class PersonReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        depth = 1

class PersonWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ContactReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        depth = 1

class ContactWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class BuyerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'
        depth = 1

class BuyerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

class RoleReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        depth = 1

class RoleWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class EmployeeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        depth = 1

class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class CompanyTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'
        depth = 1

class CompanyTypeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyType
        fields = '__all__'

class RevenueReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'
        depth = 1

class RevenueWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'

class StatusReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        depth = 1

class StatusWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class CompanyStatusReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStatus
        fields = '__all__'
        depth = 1

class CompanyStatusWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyStatus
        fields = '__all__'

class ActionTypeReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = '__all__'
        depth = 1

class ActionTypeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionType
        fields = '__all__'

class BusinessModelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = '__all__'
        depth = 1

class BusinessModelWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessModel
        fields = '__all__'

class IndustryCategoryReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCategory
        fields = '__all__'
        depth = 1

class IndustryCategoryWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCategory
        fields = '__all__'

class ResearchReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'
        depth = 1

class ResearchWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Research
        fields = '__all__'

class PhotoReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        depth = 1

class PhotoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'

class ActionReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'
        depth = 1

class ActionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'