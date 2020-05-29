from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import ContactForm
from .serializers import ContactFormSerializer
from hackathonturkiye.permissions import IsPOST



class ContactFormViewSet(ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer
    permission_classes = [IsAuthenticated|IsPOST]