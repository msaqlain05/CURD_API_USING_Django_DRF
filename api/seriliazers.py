from rest_framework import serializers
from api.models import Student

#  this class is serializer class which is convert python data to json and json into python data
class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name','fname','Class','roll_no')
