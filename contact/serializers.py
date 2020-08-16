from rest_framework import serializers
from .models import ContactForm, ContactFormCategory
from .mailing import send_mail


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
            'remote_addr': request.META.get('HTTP_X_FORWARDED_FOR', '127.0.0.1'),
            'path': request.META['PATH_INFO'],
            'user_agent': request.META.get('HTTP_USER_AGENT', None),
            'category': category
        })
        contact = validated_data('contact', 'null')
        phone = validated_data('phone', None)
        message = validated_data('body', None)
        email = validated_data('email', None)
        send_mail(
            subject=f"Merhabalar, {contact} {category.name.lower()} hakkında konuşmak istiyor.",
            message=body,
            name=contact,
            email=email,
            phone=phone,
        )

        return ContactForm.objects.create(**validated_data)