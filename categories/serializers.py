from rest_framework import serializers

from categories.models import Category
from educational_modules.models import Modules
from educational_modules.serializers import ModulesSmallSerializer


class CategoriesSerializer(serializers.ModelSerializer):
    """ Класс сериализатор категорий """
    count_modules = serializers.SerializerMethodField()
    modules = ModulesSmallSerializer(source='modules_set', read_only=True, many=True)

    def get_count_modules(self, obj):
        return Modules.objects.filter(id_category=obj).count()

    class Meta:
        model = Category
        fields = ("id", "title", "description", "photo", "count_modules", 'modules')