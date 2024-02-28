from rest_framework import serializers
from .models import Contact, ContactInfo, GetInTouch


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']


class GetInTouchSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetInTouch
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
