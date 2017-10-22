#장고의 메소드와 blog 애플리케이션에서 사용할 모든 views를 불러오고 있다.
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'), #post_list라는 이름의 view가 ^$ URL에 할당되었습니다
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
