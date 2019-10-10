import graphene
from graphene_django.types import DjangoObjectType
from graphene_file_upload.scalars import Upload

from .models import Person, Address


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class AddressType(DjangoObjectType):
    class Meta:
        model = Address


class Query(object):
    person = graphene.Field(
        PersonType,
        id=graphene.Int(),
        avatar=Upload(),
        first_name=graphene.String(),
        last_name=graphene.String(),
        address=graphene.String(AddressType),
        personal_image=Upload()
    )
    all_persons = graphene.List(PersonType)

    address = graphene.Field(
        AddressType,
        id=graphene.Int(),
        number=graphene.String(),
        street=graphene.String(),
        city=graphene.String(),
        postcode=graphene.String(),
    )
    all_addresses = graphene.List(AddressType)

    def resolve_all_persons(self, context):
        return Person.objects.all()

    def resolve_all_addresses(self, context):
        # We can easily optimize query count in the resolve method
        return Address.objects.select_related("person").all()

    def resolve_person(self, context, id=None, firstName=None, lastName=None):
        if id is not None:
            return Person.objects.get(pk=id)

        if firstName is not None:
            return Person.objects.get(first_name=firstName)

        if lastName is not None:
            return Person.objects.get(first_name=firstName)

        return None

    def resolve_address(self, context, id=None, postCode=None):
        if id is not None:
            return Address.objects.get(pk=id)

        if postCode is not None:
            return Address.objects.get(postcode=postCode)

        return None


class AddressInput(graphene.InputObjectType):
    number = graphene.String(required=True)
    street = graphene.String(required=True)
    city = graphene.String(required=True)
    postcode = graphene.String(required=True)


class CreatePerson(graphene.Mutation):
    class Arguments:
        avtr = Upload(required=False)
        fname = graphene.String(required=True)
        lname = graphene.String(required=True)
        addr = graphene.Argument(AddressInput, required=False)
        pimage = Upload(required=False)


    person = graphene.Field(PersonType)

    def mutate(self, info, avtr, fname, lname, addr, pimage):
        person = Person(
            avatar=avtr,
            firstName=fname,
            lastName=lname,
            address=addr,
            personalImage=pimage
        )
        return CreatePerson(person=person)

class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()