from rest_framework import serializers
from .models import Notes

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

    def validate(self, data):
        if Notes.objects.filter(title=data['title']).exists():
            raise serializers.ValidationError('Title Already Exists.')
        return super().validate(data)
    
    def create(self, validated_data):
        return super().create(validated_data)

    