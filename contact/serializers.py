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
            'category',
            'body',
            'email',
            'contact',
            'phone'
        ]
    def create(self, validated_data):
        request = self.context['request']
        category_name = validated_data['category']['name']
        try:
            category = ContactFormCategory.objects.get(name=category_name)
        except:
            category = ContactFormCategory(name=category_name)
            category.save()

        validated_data.update({
            'remote_addr': request.META['REMOTE_ADDR'],
            'path': request.META['PATH_INFO'],
            'user_agent': request.META.get('HTTP_USER_AGENT', None),
            'category': category
        })
        return ContactForm.objects.create(**validated_data)