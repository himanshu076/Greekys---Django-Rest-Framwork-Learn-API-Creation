from rest_framework import fields, serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name Should be start with R')

    name = serializers.CharField(validators=[start_with_r])
    class Meta:
        model = Student
        fields= ['name', 'roll', 'city']

    # Field level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # Object Level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'veeru' and ct.lower() != 'ranchi':
            raise serializers.ValidationError('City must be Ranchi')
        return data

    