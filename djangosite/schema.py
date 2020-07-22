import graphene

import entrepreneurs.schema
import investors.schema
import register.schema
import graphql_jwt



class Query(entrepreneurs.schema.Query,investors.schema.Query, register.schema.Query, graphene.ObjectType):
    pass

class Mutation(entrepreneurs.schema.myEntMutation,investors.schema.myInvMutation, register.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation =  Mutation)