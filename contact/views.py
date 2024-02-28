from rest_framework import generics
from .models import Contact, ContactInfo, GetInTouch
from .serializers import ContactSerializer, ContactInfoSerializer, GetInTouchSerializer


class ContactAPIView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactInfoAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer


class GetInTouchAPIView(generics.ListAPIView):
    queryset = GetInTouch.objects.all()[:1]
    serializer_class = GetInTouchSerializer
