from rest_framework import serializers

from core.models import Tag
from core.models import Tag, Ingredient,Recipe

class TagSerializer(serializers.ModelSerializer):
    """docstring for TagSerializer."""

    class Meta:
        model = Tag
        fields = ('id','name')
        read_only_fields =('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id','name')
        read_only_fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags', 'time_minutes', 'price',
            'link',
        )
        read_only_fields = ('id',)

class RecipeDetailSerializer(RecipeSerializer):
    """docstring for R."""
    ingredients = IngredientSerializer(many=True,read_only=True)
    tags = TagSerializer(many=True,read_only=True)

class RecipeImageSerializer(serializers.ModelSerializer):
    """serializer for uploading imges to recipe"""
    class Meta:
        model =Recipe
        fields =('id','image')
        read_only_fields = ('id',)
