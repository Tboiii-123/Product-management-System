from django.urls import path

from . import views
urlpatterns = [
    path('',views.index ,name='welcome'),
    path('login/',views.login_user , name='login' ),
    path('register/',views.register_user, name='register'),
    path('logout/',views.logout_user, name='logout'),
    path('view/',views.view, name ='view'),
    
    path('datalist/',views.data_list , name='data_list'),

    path('datalist/<item>',views.update , name='update'),

    path('searched_product/',views.searched_product, name='searched_product'),
]
