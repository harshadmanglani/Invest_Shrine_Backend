import graphene
import graphql_jwt

import entrepreneurs.schema
import investors.schema



class Query(entrepreneurs.schema.Query,investors.schema.Query, graphene.ObjectType):
    pass

class Mutation(entrepreneurs.schema.myEntMutation,investors.schema.myInvMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation =  Mutation)