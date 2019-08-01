from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserCreateListView,UserSigninView,UserDetailView

urlpatterns = [
    url(r'^signup/$', UserCreateListView.as_view()),
    url(r'^signin/$', UserSigninView.as_view()),
    url(r'^user/(?P<pk>[0-9]+)/$', UserDetailView.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)