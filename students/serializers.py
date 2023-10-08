from students.models import Student

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    """ Класс сериализатор для студента """

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name", "avatar", "email", "phone", "is_active", "modul",)


class StudentSmallSerializer(serializers.ModelSerializer):
    """ Класс сериализатора который показывает краткую информацию о студенте """

    class Meta:
        model = Student
        fields = ("id", "first_name", "last_name")
