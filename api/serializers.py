from rest_framework import serializers
from workers.models import Workers

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workers
        fields = '__all__'
