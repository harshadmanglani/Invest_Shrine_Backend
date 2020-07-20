import graphene

import entrepreneurs.schema
import investors.schema



class Query(entrepreneurs.schema.Query,investors.schema.Query, graphene.ObjectType):
    pass

class Mutation(entrepreneurs.schema.myEntMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation =  Mutation)