from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /counties/
    url(r'^kenya/$', views.counties_list, name='counties_list'),
    # ex: /counties/5/
    url(r'^kenya/(?P<counties_id>[0-9]+)/$', views.counties_detail, name='counties_detail'),
    url(r'^kenya/(?P<counties_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    # ex: /recommendation - get recommendations for the logged user
    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
]