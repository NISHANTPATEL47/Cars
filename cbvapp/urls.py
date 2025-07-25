from django.urls import path,include
from cbvapp import views

urlpatterns=[
    path('',views.AllCompanies.as_view(),name='list'),
    path('<int:pk>/',views.CompanieDetails.as_view(),name='detail'),
    path('create/',views.AddNewCompany.as_view(),name='create'),
    path('update/<int:pk>/',views.CompanyUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',views.CompanyDelete.as_view(),name='delete'),
    
]