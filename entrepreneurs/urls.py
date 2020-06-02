from django.urls import path,include
from . import views
from graphene_django.views import GraphQLView

urlpatterns = [
    path('portfolio/', views.portfolio, name = "entrepreneur_portfolio"),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]
