from django.urls import path

from . import views

app_name = 'contactList'
urlpatterns = [
	#ex: /contactList/
    path('', views.ContactList.as_view(), name='index'),
    path('contacts/', views.ContactList.as_view(), name='contacts'),
    path('mailer/', views.ContactCreate.as_view(), name='contact_create'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),
    path('thanks/', views.thanks, name='thanks'),
]
