# from typing_extensions import Required
from django.db.models import query
import graphene

from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from graphene_django import fields
from .models import Company_Details

class CompaniesType(DjangoObjectType):
    class Meta:
        model= Company_Details
        fields= '__all__'
        # fields= ("id", "name", "address", "owner_info", "employee_size")


class Query(graphene.ObjectType):
    all_companies = graphene.List(CompaniesType)
    company = graphene.Field(CompaniesType, id= graphene.Int())

    def resolve_all_companies(self, info, **kwargs):
        return Company_Details.objects.all()

    def resolve_company(self, info, id):
        return Company_Details.objects.get(pk=id)



class CompanyInput(graphene.InputObjectType):
    id= graphene.ID()
    name = graphene.String()
    address = graphene.String()
    owner_info = graphene.String()
    employee_size = graphene.Int()


class CreateCompany(graphene.Mutation):
    class Arguments:
        company_data = CompanyInput(required=True)

    company = graphene.Field(CompaniesType)

    @classmethod
    def mutate(cls,root, info, company_data=None):
        company_instance = Company_Details(
            name= company_data.name,
            address = company_data.address,
            owner_info = company_data.owner_info,
            employee_size = company_data.employee_size
        )
        company_instance.save()
        return CreateCompany(company = company_instance)



class UpdateCompany(graphene.Mutation):
    class Arguments:
        company_data = CompanyInput(required=True)

    company = graphene.Field(CompaniesType)

    @classmethod
    def mutate(cls,root, info, company_data=None):
        company_instance = Company_Details.objects.get(pk= company_data.id)

        if company_instance:
            company_instance.name = company_data.name
            company_instance.address = company_data.address
            company_instance.owner_info = company_data.owner_info
            company_instance.employee_size = company_data.employee_size
            company_instance.save()

            return UpdateCompany(company = company_instance)
        return UpdateCompany(company= None)
        

class DeleteCompany(graphene.Mutation):
    class Arguments:
        id=graphene.ID()

    company = graphene.Field(CompaniesType)

    @classmethod
    def mutate(cls,root, info,id):
        company_instance = Company_Details.objects.get(pk=id)
        company_instance.delete()

        # return DeleteCompany(company= company_instance)
        return


class SearchCompany(graphene.Mutation):
    class Arguments:
        id=graphene.ID()
    
    company = graphene.Field(CompaniesType)

    @staticmethod
    def mutate(root, info ,id):
        company_instance = Company_Details.objects.get(pk=id)

        if company_instance:
            # company_instance.name = company_data.name
            # company_instance.address = company_data.address
            # company_instance.owner_info = company_data.owner_info
            # company_instance.employee_size = company_data.employee_size
            # company_instance.save()

            return SearchCompany(company = company_instance)

        return SearchCompany(company= None)

class Mutation(graphene.ObjectType):
    create_company = CreateCompany.Field()
    update_company = UpdateCompany.Field()
    delete_company = DeleteCompany.Field()
    search_company = SearchCompany.Field()


schema = graphene.Schema(query = Query, mutation=Mutation)