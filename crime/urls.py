from django.urls import path

from . import views

urlpatterns = [
    path('file/', views.filee, name = 'filee'),
    path('search/', views.searchh, name='searchh'),
    path('s/', views.src2),
    path('<int:id>', views.detail_page, name="detail"),

    



]