from django.urls import path,include
from cbvapp import views

urlpatterns=[
    path('',views.AllCompanies.as_view()),
    path('<int:pk>/',views.CompanieDetails.as_view())
]