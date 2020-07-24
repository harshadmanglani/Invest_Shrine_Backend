import graphene
import graphql_jwt

import entrepreneurs.schema
import investors.schema
import register.schema

class Query(entrepreneurs.schema.Query,investors.schema.Query, register.schema.Query,graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()

class Mutation(entrepreneurs.schema.myEntMutation,investors.schema.myInvMutation, register.schema.myUserMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation =  Mutation)
