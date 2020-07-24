from graphene_django import DjangoObjectType
import graphene

from .models import User
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene import Field
from .forms import NewUserForm


class UserModel(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = ['username', 'email','category']
        interfaces = (relay.Node,)


class Query(graphene.ObjectType):
    users = relay.Node.Field(UserModel)
    all_users = DjangoFilterConnectionField(UserModel)

    # def resolve_all_users(self, info):

    #     # context will reference to the Django request
    #     all_users = DjangoFilterConnectionField(UserModel)

    #     print(info.context.user)
    #     if not info.context.user.is_authenticated:
    #         return User.objects.none()
    #     else:
    #         # return all_users#User.objects.all()#filter(user=info.context.user)


#mutation here:
class UserType(DjangoObjectType):
    class Meta:
        model = User

class UserMutation(DjangoModelFormMutation):
    user = Field(UserType)
    
    class Meta:
        form_class = NewUserForm


class myUserMutation(graphene.ObjectType):
    create_user = UserMutation.Field()




# class CreateUser(graphene.Mutation):
#     user = graphene.Field(UserModel)

#     class Arguments:
#         username = graphene.String(required= True)
#         password = graphene.String(required= True)
#         email = graphene.String(required= True)
#         category = graphene.String(required= False)
        
#     def mutate(self, info, username, password, email, category):
#         user = User(username = username,
#         email = email, 
#         category = category,
#         )
#         user.set_password(password)
#         user.save()

#         return CreateUser(user =user)


# class Mutation(graphene.ObjectType):
#     create_user = CreateUser.Field()

# class Query(graphene.ObjectType):
#     me = graphene.Field(UserModel)
#     user_model = graphene.List(UserModel)

#     def resolve_user_model(self, info):
#         return User.objects.all()

#     def resolve_me(self, info):
#         user = info.context.user
#         if user.is_anonymous:
#             raise Exception('Not logged in!')

#         return user
