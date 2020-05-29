from rest_framework import serializers
from .models import ContactForm, ContactFormCategory


class ContactFormCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormCategory
        fields = ['name']


class ContactFormSerializer(serializers.ModelSerializer):
    category = ContactFormCategorySerializer(many=False, read_only=False)
    class Meta:
        model = ContactForm
        fields = [
            'title',
            'category',
            'body',
            'email',
            'contact',
            'phone'
        ]
    def create(self, validated_data):
        request = self.context['request']        
        category_name = validated_data['category']['name']
        category = ContactFormCategory.objects.get(name=category_name)

        validated_data.update({
            'remote_addr': request.META['REMOTE_ADDR'],
            'path': request.META['PATH_INFO'],
            'user_agent': request.META['HTTP_USER_AGENT'],
            'category': category
        })
        return ContactForm.objects.create(**validated_data)