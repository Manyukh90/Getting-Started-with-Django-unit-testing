from .models import Student
from rest_framework.serializers import ModelSerializer

# # serializers.py
class StudentSerializer(ModelSerializer):
     class Meta:
        model = Student
        fields = "__all__"  