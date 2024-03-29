from graphene_django import DjangoObjectType
import graphene
# from .models import PortfolioEnt as EntrepreneurPortfolioModel, Venture, Industry
from .models import Portfolio as InvestorPortfolioModel, History, WatchList
from register.models import User
from django.db.models import Q
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from .forms import InvestorPortfolioForm, WatchListForm
from graphene import Field



class InvestorPortfolio(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel
        filter_fields = ['user','first_name','last_name','interests','current_occupation','location', 'num_investments']
        interfaces = (relay.Node,)

class HistoryModel(DjangoObjectType):
    class Meta:
        model = History
        filter_fields = ['investment_history']
        interfaces =(relay.Node,)

class WatchListModel(DjangoObjectType):
    class Meta:
        model = WatchList
        filter_fields = ['investor','ventures']
        interfaces = (relay.Node,)

class Query(graphene.ObjectType):

    investors = relay.Node.Field(InvestorPortfolio)
    all_investors = DjangoFilterConnectionField(InvestorPortfolio)

    history = relay.Node.Field(HistoryModel)
    inv_history = DjangoFilterConnectionField(HistoryModel)

    watchlist = relay.Node.Field(WatchListModel)
    inv_watchlist = DjangoFilterConnectionField(WatchListModel)

#mutations here :
class InvType(DjangoObjectType):
    class Meta:
        model = InvestorPortfolioModel

class InvMutation(DjangoModelFormMutation):
    inv = Field(InvType)

    class Meta:
        form_class = InvestorPortfolioForm

#mutation for Watchlist here
class WatchListType(DjangoObjectType):
    class Meta:
        model = WatchList

class AddtoWatchList(graphene.Mutation): #for every venture being added to watch list
    watchlist = graphene.Field(WatchListType)

    class Arguments :
        investor = graphene.ID(required = True)
        venture = graphene.ID(required = True)

    def mutate(self, info, investor, venture, **kwargs):
        wl_obj = WatchList.objects.get(investor= investor)
        wl_obj.ventures.add(venture)
        wl_obj.save()

        return AddtoWatchList(watchlist = wl_obj)

class DeletefromWatchList(graphene.Mutation): #for every venture being added to watch list
    watchlist = graphene.Field(WatchListType)

    class Arguments :
        investor = graphene.ID(required = True)
        venture = graphene.ID(required = True)

    def mutate(self, info, investor, venture, **kwargs):
        wl_obj = WatchList.objects.get(investor= investor)
        wl_obj.ventures.remove(venture)
        wl_obj.save()

        return AddtoWatchList(watchlist = wl_obj)

#ends here
# djangomodelform mutation 
class WatchListMutation(DjangoModelFormMutation):
    watchlistobj = Field(WatchListType)

    class Meta:
        form_class = WatchListForm

class myInvMutation(graphene.ObjectType):
    create_investor = InvMutation.Field()
    add_to_watchlist = AddtoWatchList.Field() # to add ventures to already existing field in watchlist. 
    alter_watchlist = WatchListMutation.Field()  #to add investors. 
    remove_from_watchlist = DeletefromWatchList.Field() # remove ventures from already existing investor field in watchlist. 