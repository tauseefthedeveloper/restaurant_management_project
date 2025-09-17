from rest_framework import serializers
from .models import MenuCategory

class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        mode = ModelCategory
        fields =['id','name']