from rest_framework import serializers
from .models import Student

class  StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True) #read_only_01
    class Meta:
        model = Student
        fields= ['name', 'roll', 'city']
        # read_only_fields= ['name', 'roll'] #read_only_02
        extra_kwargs = {'name': {'read_only': True}} #read_only_03

