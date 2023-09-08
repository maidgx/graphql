import graphene
from graphene_django import DjangoObjectType

from simpleGraph.simpleCal.models import Number

class NumberType(DjangoObjectType):
    class Meta:
        model = Number
        fields = ("id", "value")

class Query(graphene.ObjectType):
    all_numbers = graphene.List(NumberType)
    
    sum_number = graphene.Field(NumberType, num1=graphene.Int(), num2=graphene.Int())

    sub_number = graphene.Field(NumberType, num1=graphene.Int(), num2=graphene.Int())

    multiple_number = graphene.Field(NumberType, num1=graphene.Int(), num2=graphene.Int())

    divide_number = graphene.Field(NumberType, num1=graphene.Int(), num2=graphene.Int())


    def resolve_all_numbers(root, info):
        return Number.objects.all()

    def resolve_sum_number(root, info, num1, num2):
        num1 = Number.objects.get(value=num1).value
        num2 = Number.objects.get(value=num2).value
        new = num1 + num2
        return Number(id=200,value=new)

    def resolve_sub_number(root, info, num1, num2):
        num1 = Number.objects.get(value=num1).value
        num2 = Number.objects.get(value=num2).value
        new = num1 - num2
        return Number(id=200,value=new)

    def resolve_multiple_number(root, info, num1, num2):
        num1 = Number.objects.get(value=num1).value
        num2 = Number.objects.get(value=num2).value
        new = num1 * num2
        return Number(id=200,value=new)

    def resolve_divide_number(root, info, num1, num2):
        num1 = Number.objects.get(value=num1).value
        num2 = Number.objects.get(value=num2).value
        new = num1 // num2
        return Number(id=200,value=new)
    
schema = graphene.Schema(query=Query)
