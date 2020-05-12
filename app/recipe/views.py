from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient,Recipe

from recipe import serializers
# Create your views here.

class BaseRecipeAttrViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    "base viewset for user owned recipe attributes"
    authentication_classes =(TokenAuthentication,)
    permission_classes= (IsAuthenticated,)

    def get_queryset(self):
        """return objectsforcurrent user authentcated only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self,serializer):
        """create new inedient to prevent AssertionError: 405 != 400"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
    """docstring for TagViewSet.manage tags in db"""
    queryset =Tag.objects.all()
    serializer_class =serializers.TagSerializer

class IngredientViewSet(BaseRecipeAttrViewSet):
    """Manage ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

# class TagViewSet(viewsets.GenericViewSet,
#                  mixins.ListModelMixin,
#                  mixins.CreateModelMixin):
#     """docstring for TagViewSet.manage tags in db"""
#     authentication_classes =(TokenAuthentication,)
#     permission_classes= (IsAuthenticated,)
#     queryset =Tag.objects.all()
#     serializer_class =serializers.TagSerializer
#
#     def get_queryset(self):
#         """return objectsforcurrent user authentcated only"""
#         return self.queryset.filter(user=self.request.user).order_by('-name')
#
#     def perform_create(self,serializer):
#         """create new inedient to prevent AssertionError: 405 != 400"""
#         serializer.save(user=self.request.user)
#
#
# class IngredientViewSet(viewsets.GenericViewSet,
#                         mixins.ListModelMixin,
#                         mixins.CreateModelMixin):
#     """Manage ingredients in the database"""
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Ingredient.objects.all()
#     serializer_class = serializers.IngredientSerializer
#
#     def get_queryset(self):
#         """Return objects for the current authenticated user only"""
#         return self.queryset.filter(user=self.request.user).order_by('-name')
#
#     def perform_create(self,serializer):
#         """create new  ingredfient"""
#         serializer.save(user=self.request.user)
