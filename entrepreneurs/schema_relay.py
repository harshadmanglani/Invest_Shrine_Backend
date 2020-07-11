from graphene_django import DjangoObjectType
import graphene
from .models import PortfolioEnt as EntrepreneurPortfolioModel
from investors.models import Portfolio as InvestorPortfolioModel
from register.models import User
from django.db.models import Q
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

class EntrepreneurPortfolio(DjangoObjectType):
    class Meta:
        model = EntrepreneurPortfolioModel
        filter_fields = ['user','first_name','last_name','venture_name','industry','investment_options']
        interfaces = (relay.Node,)
        

class InvestorPortfolio(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel



class RelayQuery(graphene.ObjectType):

    # entrepreneur_portfolio = graphene.List(EntrepreneurPortfolio)
    # investor_portfolio = graphene.List(InvestorPortfolio)
    
    entrepreneurs = relay.Node.Field(EntrepreneurPortfolio)
    all_entrepreneurs = DjangoFilterConnectionField(EntrepreneurPortfolio)

    # def resolve_entrepreneur_portfolio(self, ):
    #     return EntrepreneurPortfolioModel.objects.all()
    
    # def resolve_investor_portfolio(self, context):
    #     return InvestorPortfolioModel.objects.all()

    

# schema = graphene.Schema(query=Query)