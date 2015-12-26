from social.models import Messages
from .serializers import MessageSerializer

from django.http import Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
class MessageList(APIView):
    #gets all messages in the social media database

    def get(self,request,format=None):
        queryset = Messages.objects.all().order_by('-id')
        serializedMessages = MessageSerializer(queryset,many=True,context={'request': request})
        return Response(serializedMessages.data)
class singleMessage(APIView):
    #renderer_classes = (JSONRenderer, )

    def getSingeMessage(self,pk):
        try:
            return Messages.objects.get(pk=pk)
        except Messages.DoesNotExist:
            raise Http404("id not found")

    def get(self,request,pk,format=None):
        queryset = self.getSingeMessage(pk=pk)
        serializedMessages = MessageSerializer(queryset,many=False,context={'request': request})
        return Response(serializedMessages.data)

class PrivateMessagesList(APIView):

    def get(self,request,format=None):
        queryset = Messages.objects.filter(isPrivatemessage=True).order_by('-id')
        serializedMessages = MessageSerializer(queryset,context={'request': request},many=True )
        return Response(serializedMessages.data)

class PublicMessagesList(APIView):

    def get(self,request,format=None):
        queryset = Messages.objects.filter(isPrivatemessage=False).order_by('-id')
        serializedMessages = MessageSerializer(queryset,many=True)
        return Response(serializedMessages.data)
