from graphene_django import DjangoObjectType
import graphene
from .models import *

class User(DjangoObjectType):
    class Meta:
        model = EntrepreneurModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return EntrepreneurModel.objects.all()

schema = graphene.Schema(query=Query)