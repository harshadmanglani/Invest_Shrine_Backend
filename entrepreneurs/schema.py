from graphene_django import DjangoObjectType
import graphene
from .models import *

class Entrepreneur(DjangoObjectType):
    class Meta:
        model = EntrepreneurModel

class EntrepreneurPortfolio(DjangoObjectType):
    class Meta:
        model = EntrepreneurPortfolioModel

class Query(graphene.ObjectType):
    entrepreneur = graphene.List(Entrepreneur)
    entrepreneur_portfolio = graphene.List(EntrepreneurPortfolio)

    def resolve_entrepreneur(self, info):
        return EntrepreneurModel.objects.all()

    def resolve_entrepreneur_portfolio(self, info):
        return EntrepreneurPortfolioModel.objects.all()

schema = graphene.Schema(query=Query)