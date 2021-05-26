from django.urls import path
from . import views

urlpatterns = [ 
    path('courses', views.coursesList.as_view()),
    path('courses/<int:pk>', views.coursesUpdateList.as_view()),
    path('contact', views.ContactList.as_view()),
    path('contact/<int:pk>', views.contactUpdateList.as_view()),
]