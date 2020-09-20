from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.product_form,name='product_insert'), # get and post req. for insert operation
    path('<int:id>/', views.product_form,name='product_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.product_delete,name='product_delete'),
    path('list/',views.product_list,name='product_list') # get req. to retrieve and display all records
]