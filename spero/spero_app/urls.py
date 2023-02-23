from django.urls import path
from . import views

urlpatterns = [
  path('',views.home),
  path('add/',views.add,name='add'),
  path('delete/<int:id>',views.delete),
  path('update/<int:id>',views.update),
]