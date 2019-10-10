import people.person.schema
import graphene

from graphene_django.debug import DjangoDebug


class Query(
    people.person.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutations(
    people.person.schema.Mutations,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query, mutation=Mutations)