from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from social.models import Member, Profile,Messages
from django.utils import timezone
from django.db.models import Q
appname = 'Facemagazine'
from rest_framework import viewsets,status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from social.serializers import ProfileSerializer,MessageSerializer
from django.http import Http404

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.order_by('-id')
    serializer_class = MessageSerializer#(context={'request': request})
    #gets all messages in the social media database

def index(request):
    template = loader.get_template('social/index.html')
    context = RequestContext(request, {
            'appname': appname,
        })
    return HttpResponse(template.render(context))

def messages(request):
    if 'username' in request.session:
        username = request.session['username']
        template = loader.get_template('social/messages.html')

        if 'view' in request.GET:
            greeting= request.GET['view']
            recip= greeting[0:len(greeting)-2]#trims out the 's from the name
            #shows friends messages (value recieved fromt the get request)
            if recip == username:
                greeting="Your"
            #if it finds your username it re-directs back to your page

        else:
	        greeting="Your"
            #no value of view found it get request


		#if greeting was assigned "Your", send message to yourself
        if greeting == "Your":
            recip=username

        if 'message' in request.POST:
        #saving message to database

			#check if it is a private message
            if request.POST['messageGroup']=="True":
                isPrivateMsg=True
            else:
                isPrivateMsg=False

			#saves message to the database
            messages = Messages(message=request.POST['message'],time=timezone.now(),isPrivatemessage=isPrivateMsg,recipient=Member.objects.get(pk=recip),user=Member.objects.get(pk=username))
            messages.save()


        if greeting =="Your": #creates the delete button if you are on your on own account
		    #outputs messages which are ordered by last recieved
            storedMessages = Messages.objects.filter(recipient=recip).order_by('-time')
            delete="Delete"
        else:
            storedMessages = Messages.objects.filter(Q(recipient=recip,isPrivatemessage=False)|(Q(recipient =recip,user=username))).order_by('-time')
            #outputs public messages and private messages you sent the user
            delete=""

        if 'remove' in request.GET:
            # Makes an SQL select query to get the message using the id recieved from GET request. With this it deletes the message
            removeMessage = Messages.objects.filter(id=request.GET['remove'])
            removeMessage.delete()


        context = RequestContext(request, {
                'appname': appname,
                'username': username,
				'greeting': greeting,
				'delete': delete,
				'storedMessages': storedMessages,
                'loggedin': True

            })

        return HttpResponse(template.render(context))
    else:
        return render(request, 'social/messages.html', {
                'appname': appname,
				#message is outputted telling the user to login (same as coursework 1)
                'loggedin': False}
                )

def signup(request):
    template = loader.get_template('social/signup.html')
    context = RequestContext(request, {
            'appname': appname,
        })
    return HttpResponse(template.render(context))

def register(request):
    u = request.POST['user']
    p = request.POST['pass']
    user = Member(username=u, password=p)
    user.save()
    template = loader.get_template('social/user-registered.html')
    context = RequestContext(request, {
        'appname': appname,
        'username' : u
        })
    return HttpResponse(template.render(context))

def login(request):
    if 'username' not in request.POST:
        template = loader.get_template('social/login.html')
        context = RequestContext(request, {
                'appname': appname,
            })
        return HttpResponse(template.render(context))
    else:
        u = request.POST['username']
        p = request.POST['password']
        try:
            member = Member.objects.get(pk=u)
        except Member.DoesNotExist:
            return render(request, 'social/login.html', {
                'appname': appname,
                'username': u,
                'loggedin': False}
				#message is outputted telling the user to login (same as coursework 1)
                )
        if member.password == p:
            request.session['username'] = u;
            request.session['password'] = p;
            return render(request, 'social/login.html', {
                'appname': appname,
                'username': u,
                'loggedin': True}
                )
        else:
            return render(request, 'social/login.html', {
                'appname': appname,
                'loggedin': False}
				#message is outputted telling the user to login (same as coursework 1)
                )

def logout(request):
    if 'username' in request.session:
        u = request.session['username']
        request.session.flush()
        template = loader.get_template('social/logout.html')
        context = RequestContext(request, {
                'appname': appname,
				'loggedin': False
            })
        return HttpResponse(template.render(context))


def member(request, view_user):
    if 'username' in request.session:
        username = request.session['username']
        member = Member.objects.get(pk=view_user)

        if view_user == username:
            greeting = "Your"
        else:
            greeting = view_user + "'s"

        if member.profile:
            text = member.profile.text
        else:
            text = ""
        return render(request, 'social/member.html', {
            'appname': appname,
            'username': username,
            'greeting': greeting,
            'profile': text,
            'loggedin': True}
            )
    else:
        return render(request, 'social/friends.html', {
            'appname': appname,
            'loggedin': False}
			#message is outputted telling the user to login (same as coursework 1)
            )
def friends(request):
    if 'username' in request.session:
        username = request.session['username']
        member_obj = Member.objects.get(pk=username)
        # list of people I'm following
        following = member_obj.following.all()
        # list of people that are following me
        followers = Member.objects.filter(following__username=username)
        # render reponse
        return render(request, 'social/friends.html', {
            'appname': appname,
            'username': username,
            'members': members,
            'following': following,
            'followers': followers,
            'loggedin': True}
            )
    else:
        return render(request, 'social/friends.html', {
            'appname': appname,
            'loggedin': False}
			#message is outputted telling the user to login (same as coursework 1)
            )

def members(request):
    if 'username' in request.session:
        username = request.session['username']
        member_obj = Member.objects.get(pk=username)
        # follow new friend
        if 'add' in request.GET:
            friend = request.GET['add']
            friend_obj = Member.objects.get(pk=friend)
            member_obj.following.add(friend_obj)
            member_obj.save()
        # unfollow a friend
        if 'remove' in request.GET:
            friend = request.GET['remove']
            friend_obj = Member.objects.get(pk=friend)
            member_obj.following.remove(friend_obj)
            member_obj.save()
        # view user profile
        if 'view' in request.GET:
            return member(request, request.GET['view'])
        else:
            # list of all other members
            members = Member.objects.exclude(pk=username)
            # list of people I'm following
            following = member_obj.following.all()
            # list of people that are following me
            followers = Member.objects.filter(following__username=username)
            # render reponse
            return render(request, 'social/members.html', {
                'appname': appname,
                'username': username,
                'members': members,
                'following': following,
                'followers': followers,
                'loggedin': True}
                )
    else:
        return render(request, 'social/members.html', {
                'appname': appname,
                'loggedin': False}
				#shows error message on the page if the user is not logged in
                )

def profile(request):
    if 'username' in request.session:
        u = request.session['username']
        member = Member.objects.get(pk=u)
        if 'text' in request.POST:
            text = request.POST['text']
            if member.profile:
                member.profile.text = text
                member.profile.save()
            else:
                profile = Profile(text=text)
                profile.save()
                member.profile = profile
            member.save()
        else:
            if member.profile:
                text = member.profile.text
            else:
                text = ""
        return render(request, 'social/profile.html', {
            'appname': appname,
            'username': u,
            'text' : text,
            'loggedin': True}
            )
    else:
        return render(request, 'social/profile.html', {
			#message is outputted telling the user to login (same as coursework 1)
            'appname': appname,
            'loggedin': False}
            )

def checkuser(request):
    if 'user' in request.POST:
        u = request.POST['user']
        try:
            member = Member.objects.get(pk=u)
        except Member.DoesNotExist:
            member = None
        if member is not None:
            return HttpResponse("<span class='taken'>&nbsp;&#x2718; This username is taken</span>")
        else:
            return HttpResponse("<span class='available'>&nbsp;&#x2714; This username is available</span>")
