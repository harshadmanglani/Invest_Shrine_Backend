from graphene_django import DjangoObjectType
import graphene
from .models import PortfolioEnt as EntrepreneurPortfolioModel, Venture, Industry
from investors.models import Portfolio as InvestorPortfolioModel, InvestmentOptions
from register.models import User
from django.db.models import Q
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import EntrepreneurPortfolioForm, EntForm, VentureForm
from graphene import Field


class EntrepreneurPortfolio(DjangoObjectType):
    class Meta:
        model = EntrepreneurPortfolioModel
        filter_fields = ['user','first_name','last_name', 'venture']
        interfaces = (relay.Node,)
        

# class InvestorPortfolio(DjangoObjectType):
#     class Meta:
#         model = InvestorPortfolioModel
#         filter_fields = ['user','first_name','last_name','interests','investment_options','current_occupation']
#         interfaces = (relay.Node,)

class VentureModel(DjangoObjectType):
    class Meta:
        model = Venture
        filter_fields = ['venture_name', 'industry']
        interfaces = (relay.Node,)

class IndustryModel(DjangoObjectType):
    class Meta:
        model = Industry
        filter_fields = ["industry"]
        interfaces = (relay.Node,)

class InvestmentOptionsModel(DjangoObjectType):
    class Meta:
        model = InvestmentOptions

class Query(graphene.ObjectType):
  
    entrepreneurs = relay.Node.Field(EntrepreneurPortfolio)
    all_entrepreneurs = DjangoFilterConnectionField(EntrepreneurPortfolio)

    # investors = relay.Node.Field(InvestorPortfolio)
    # all_investors = DjangoFilterConnectionField(InvestorPortfolio)

    ventures = relay.Node.Field(VentureModel)   
    all_ventures = DjangoFilterConnectionField(VentureModel)

    industry_model = relay.Node.Field(IndustryModel)
    allindustries = DjangoFilterConnectionField(IndustryModel)

    investment_options = graphene.List(InvestmentOptionsModel)

    

    # def resolve_industry_model(self, info, **kwargs):
    #     return Industry.objects.all()

    def resolve_investment_options(self, info, **kwargs):
        return InvestmentOptions.objects.all()


#Mutations here :
class EntType(DjangoObjectType):
    class Meta:
        model = EntrepreneurPortfolioModel

class EntMutation(DjangoModelFormMutation):
    ent = Field(EntType)

    class Meta:
        form_class = EntForm



# mutations for venture here 
class VentureType(DjangoObjectType):
    class Meta:
        model = Venture

class VentureMutation(DjangoModelFormMutation):
    ent = Field(VentureType)

    class Meta:
        form_class = VentureForm



class myEntMutation(graphene.ObjectType):
    create_entrepreneur = EntMutation.Field()
    create_venture = VentureMutation.Field()