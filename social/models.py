from django.db import models

class Profile(models.Model):
    text = models.CharField(max_length=4096)

    def __str__(self):
        if self.member:
            return self.member.username + ": " + self.text
            return self.text


class Member(models.Model):
    username = models.CharField(max_length=16,primary_key=True)
    password = models.CharField(max_length=16)
    profile = models.OneToOneField(Profile, null=True)
    following = models.ManyToManyField("self", symmetrical=False)
    #messages = models.ManyToManyField(Messages)
	#messages = models.ForeignKey(Messages)

    def __str__(self):
        return self.username
class Messages(models.Model):
    #recipient = models.OneToOneField('Member')
    message = models.CharField(max_length=320)
    #stores a message no longer than 160 characters
    time= models.DateTimeField(null=False)
    isPrivatemessage = models.BooleanField(null=False)
    #null argument simply forces the message to either a public or private argument
    recipient = models.ForeignKey(Member, related_name = "recipient")
    user = models.ForeignKey(Member, related_name = "user")
    
