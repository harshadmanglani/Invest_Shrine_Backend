from graphene_django import DjangoObjectType
import graphene
from .models import PortfolioEnt as EntrepreneurPortfolioModel
from investors.models import Portfolio as InvestorPortfolioModel

class EntrepreneurPortfolio(DjangoObjectType):
    class Meta:
        model = EntrepreneurPortfolioModel

class InvestorPortfolio(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel


class Query(graphene.ObjectType):
    entrepreneur_portfolio = graphene.List(EntrepreneurPortfolio)
    investor_portfolio = graphene.List(InvestorPortfolio)

    def resolve_entrepreneur_portfolio(self, context):
        return EntrepreneurPortfolioModel.objects.all()
    
    def resolve_investor_portfolio(self, context):
        return InvestorPortfolioModel.objects.all()

schema = graphene.Schema(query=Query)