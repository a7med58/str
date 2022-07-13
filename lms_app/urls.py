from django.urls import path
from .  import views



urlpatterns = [
    path('',views.index, name='index'),
    path('book',views.book, name='book'),
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('dash',views.dash, name='dash'),


]