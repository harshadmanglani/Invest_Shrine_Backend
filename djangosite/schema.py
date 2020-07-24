import graphene
import graphql_jwt

import entrepreneurs.schema
import investors.schema



class Query(entrepreneurs.schema.Query,investors.schema.Query, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
<<<<<<< HEAD

=======
>>>>>>> e3996a2e18e62d32a20fda3e05de0b09c5e4b628

class Mutation(entrepreneurs.schema.myEntMutation,investors.schema.myInvMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation =  Mutation)
