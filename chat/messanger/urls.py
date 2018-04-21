from django.urls import path, re_path
from . import views

urlpatterns = [
    path('view/', views.chat_list),
    path('view/users', views.user_list),
    re_path(r'^view/(?P<message_id>[0-9]+)/$', views.detail),

]