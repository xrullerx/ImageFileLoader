from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/', views.imageList, name='image_list'),
]