# /social/serializers.py
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Messages,Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('text',)
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        message = ('id','message','time','recipient','user',)


'''
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='Message-name')

    class Meta:
        model = Messages
        fields = ('url','id','highlight','message','time','recipient','user',)


    message = models.CharField(max_length=160)
    time= models.DateTimeField(null=False)
    isPrivatemessage = models.BooleanField(default=False,null=False)
    recipient = models.ForeignKey(Member, related_name = "recipient", null=False)
    user = models.ForeignKey(Member, related_name = "user", null=False)
'''
