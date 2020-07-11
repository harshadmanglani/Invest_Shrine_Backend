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
        filter_fields = ['user','first_name','last_name','interests','investment_options','current_occupation']
        interfaces = (relay.Node,)

#input object here:
# class EntInput(graphene.InputObjectType):
#     user = graphene.String(required = True)
#     first_name = graphene.String(required = True)
#     last_name = graphene.String(required = True)
#     linkedin_profile = graphene.String(required = False)
#     exec_summary = graphene.String(required = False)
#     venture_name = graphene.String(required = False)
#     startup_summary = graphene.String(required = False)
#     industry = graphene.String(required = False)
#     prototype = graphene.String(required = False)
#     investment = graphene.Int(required = False)
#     investment_options = graphene.String(required = False)



#mutations here:
class CreateEntrepreneur(graphene.Mutation):
    ent = graphene.Field(EntrepreneurPortfolio)

    class Arguments:
        user = graphene.String(required = False)
        first_name = graphene.String(required = False)
        last_name = graphene.String(required = False)
        linkedin_profile = graphene.String(required = False)
        exec_summary = graphene.String(required = False)
        venture_name = graphene.String(required = False)
        startup_summary = graphene.String(required = False)
        industry = graphene.String(required = False)
        prototype = graphene.String(required = False)
        investment = graphene.Int(required = False)
        investment_options = graphene.String(required = False)
        # ent_data = EntInput(Field)

    def mutate(self, info, user = None, first_name = None, last_name = None, linkedin_profile = None, exec_summary = None, venture_name = None,
     startup_summary = None, industry = None, prototype = None, investment = None, investment_options = None) :

        ent = EntrepreneurPortfolioModel(user=user, first_name=first_name, last_name =last_name, linkedin_profile = linkedin_profile,
                exec_summary = exec_summary, venture_name =venture_name, startup_summary=startup_summary,
                prototype=prototype, investment = investment)
        ent.save()
        ent.industry.set(industry)
        ent.investment_options.set(investment_options)
        ent.save()

        return CreateEntrepreneur(ent = ent)

class Mutation(graphene.ObjectType):
    create_ent = CreateEntrepreneur.Field()

class Query(graphene.ObjectType):
  
    entrepreneurs = relay.Node.Field(EntrepreneurPortfolio)
    all_entrepreneurs = DjangoFilterConnectionField(EntrepreneurPortfolio)

    investors = relay.Node.Field(InvestorPortfolio)
    all_investors = DjangoFilterConnectionField(InvestorPortfolio)

    
