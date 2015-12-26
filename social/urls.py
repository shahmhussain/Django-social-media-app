from django.conf.urls import include,patterns, url
from social import views,api
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


router = DefaultRouter()
#router.register(r'profiles', views.ProfileViewSet)
router.register(r'Messages', views.MessageViewSet)
#router.register(r'PublicMessages', views.PublicMessagesViewSet)
#router.register(r'PrivateMessages', views.PrivateMessagesViewSet)


urlpatterns = patterns('',
    # main page
    url(r'^$', views.index),
    # signup page
    url(r'^signup/$', views.signup),
    # register new user
    url(r'^register/$', views.register),
    # login page
    url(r'^login/$', views.login),
    # logout page
    url(r'^logout/$', views.logout),
    # members page
    url(r'^members/$', views.members),
    # friends page
    url(r'^friends/$', views.friends),
    # user profile edit page
    url(r'^profile/$', views.profile),
    # Ajax: check if user exists
    url(r'^checkuser/$', views.checkuser),
    # messages page
    url(r'^messages/$', views.messages),
	#
	#api list

    url(r'^api/', include(router.urls)),

    #api list
    #views used in the django rest api
    #url(r'^api/messages/', api.MessageList.as_view()),
    #url(r'^api/PrivateMessages/(?P<pk>[0-9]+)/$',api.PrivateMessage.as_view()),
    url(r'^api/Message/(?P<pk>[0-9]+)/$',api.singleMessage.as_view(), name='routeOption'),
    url(r'^api/privateMessages/', api.PrivateMessagesList.as_view()),
    url(r'^api/publicMessages/', api.PublicMessagesList.as_view()),

    #url(r'^api/' views.
	#url(r'^api/', views.MessageViewSet.getAllMessages)

)
