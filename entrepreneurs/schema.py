from graphene_django import DjangoObjectType
import graphene
from .models import PortfolioEnt as EntrepreneurPortfolioModel, Venture, Industry
from investors.models import Portfolio as InvestorPortfolioModel
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
        filter_fields = ['user','first_name','last_name', 'venture', 'location']
        interfaces = (relay.Node,)
        

class VentureModel(DjangoObjectType):
    class Meta:
        model = Venture
        filter_fields = ['venture_name', 'industry','location','venture_id']
        interfaces = (relay.Node,)

class IndustryModel(DjangoObjectType):
    class Meta:
        model = Industry
        filter_fields = ["industry"]
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
  
    entrepreneurs = relay.Node.Field(EntrepreneurPortfolio)
    all_entrepreneurs = DjangoFilterConnectionField(EntrepreneurPortfolio)

    ventures = relay.Node.Field(VentureModel)   
    all_ventures = DjangoFilterConnectionField(VentureModel)

    industry_model = relay.Node.Field(IndustryModel)
    allindustries = DjangoFilterConnectionField(IndustryModel)



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