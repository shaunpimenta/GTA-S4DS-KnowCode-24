from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

#   sensor_data/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar&Depth_1=69&Depth_2=73&Depth_3=60&temperature=89&humidity=45


    path('sensor_data/', views.sensor_data, name='sensor_data'),


    # path("upload_file/", views.upload_file, name="upload_file"),


    # path("showresult/<int:myid>", views.showresult, name="showresult"),


    path('user_login/',      views.user_login,     name='user_login'),
    path('user_logout/',     views.user_logout,    name='user_logout'),
    path('user_register/',   views.user_register,  name='user_register'),



    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),
]
