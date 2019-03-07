from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'contactList'
urlpatterns = [
	#ex: /contactList/
    path('', views.ContactCreate.as_view(), name='index'),
    path('contacts/', views.ContactList.as_view(), name='contacts'),
    path('mailer/', views.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
    path('thanks/', views.thanks, name='thanks'),
    path('login/', auth_views.LoginView.as_view(template_name='contactList/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='contactList/logout.html', next_page ='contactList:contact_create'), name='logout'),
]
