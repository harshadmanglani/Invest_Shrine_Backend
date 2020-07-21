from graphene_django import DjangoObjectType
import graphene
# from .models import PortfolioEnt as EntrepreneurPortfolioModel, Venture, Industry
from .models import Portfolio as InvestorPortfolioModel, InvestmentOptions, History
from register.models import User
from django.db.models import Q
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import InvestorPortfolioForm
from graphene import Field



class InvestorPortfolio(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel
        filter_fields = ['user','first_name','last_name','interests','investment_options','current_occupation']
        interfaces = (relay.Node,)

class HistoryModel(DjangoObjectType):
    class Meta:
        model = History
        filter_fields = ['investment_history']
        interfaces =(relay.Node,)


class Query(graphene.ObjectType):

    investors = relay.Node.Field(InvestorPortfolio)
    all_investors = DjangoFilterConnectionField(InvestorPortfolio)

    history = relay.Node.Field(HistoryModel)
    inv_history = DjangoFilterConnectionField(HistoryModel)

    
#mutations here :
class InvType(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel

class InvMutation(DjangoModelFormMutation):
    inv = Field(InvType)

    class Meta:
        form_class = InvestorPortfolioForm

class myInvMutation(graphene.ObjectType):
    create_investor = InvMutation.Field()