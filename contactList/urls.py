from django.urls import path

from . import views

app_name = 'contactList'
urlpatterns = [
	#ex: /contactList/
    path('', views.IndexView.as_view(), name='index'),
    path('contacts/', views.IndexView.as_view(), name='contacts'),
    path('mailer/', views.FormView.as_view(), name='mailer'),

]
