from project.models import Contact
from rest_framework import serializers
from project.models import courses,Contact

class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model= courses
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields='__all__'