import graphene

import entrepreneurs.schema




class Query(entrepreneurs.schema.Query, graphene.ObjectType):
    pass

class Mutation(entrepreneurs.schema.Mutation, entrepreneurs.schema.myEntMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation =  Mutation)