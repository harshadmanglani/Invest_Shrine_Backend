from graphene_django import DjangoObjectType
import graphene
from .models import *
from investors.models import * 

class EntrepreneurPortfolio(DjangoObjectType):
    class Meta:
        model = EntrepreneurPortfolioModel

class InvestorPortfolioModel(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel


class Query(graphene.ObjectType):
    entrepreneur_portfolio = graphene.List(EntrepreneurPortfolioModel)
    investor_portfolio = graphene.List(InvestorPortfolioModel)

    def resolve_entrepreneur_portfolio(self, info):
        return EntrepreneurPortfolioModel.objects.all()
    
    def resolve_investor_portfolio(self, info):
        return InvestorPortfolioModel.objects.all()

schema = graphene.Schema(query=Query)