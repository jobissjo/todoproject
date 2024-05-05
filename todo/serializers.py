from rest_framework import serializers
from .models import ToDo


class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['task','description', 'status', 'complete_date', 'user_id']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if hasattr(instance, 'id'):
            data['id'] = instance.id
            data['created_at'] = instance.created_at.date()
        return data
    
    def create(self, validated_data):
        # Exclude created_at from validated data
        validated_data.pop('created_at', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Exclude created_at from validated data
        validated_data.pop('created_at', None)
        return super().update(instance, validated_data)