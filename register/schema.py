from graphene_django import DjangoObjectType
import graphene

from .models import User

class UserModel(DjangoObjectType):
    class Meta:
        model = User


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserModel)

    class Arguments:
        username = graphene.String(required= True)
        password = graphene.String(required= True)
        email = graphene.String(required= True)
        category = graphene.String(required= False)
        
    def mutate(self, info, username, password, email, category):
        user = User(username = username,
        email = email, 
        category = category,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user =user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

class Query(graphene.ObjectType):
    me = graphene.Field(UserModel)
    user_model = graphene.List(UserModel)

    def resolve_user_model(self, info):
        return User.objects.all()

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        return user
