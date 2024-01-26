from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

#   sensor_data/?username=sahil&api_key=5df155f4-9161-44b9-8ff5-9c821709e1bf&nodename=node_dadar&Depth_1=69&Depth_2=73&Depth_3=60&temperature=89&humidity=45


#   sensor_data/?user_name=atharva&api_key=n36q1nw1-hjp9-1b7k-x0a2-ec98msacb6r4&heartPulse=89&dhtTemp=32&dhtHum=73&gyroX=60&gyroY=89&gyroZ=45&acceleroX=60&acceleroY=89&acceleroZ=45

# http://127.0.0.1:8000/sensor_data/?user_name=atharva&api_key=qx3w49r3-kifh-ix9z-04lr-mz1y4bpl8rer&heartPulse=95&dhtTemp=31&dhtHum=79&gyroX=60&gyroY=89&gyroZ=45&acceleroX=60&acceleroY=89&acceleroZ=45

# https://2421d8dd-7f48-42df-a3ff-fcf3762b1b67-00-1xu9mw62re307.worf.replit.dev/sensor_data/?user_name=atharva&api_key=qx3w49r3-kifh-ix9z-04lr-mz1y4bpl8rer&heartPulse=95&dhtTemp=31&dhtHum=79&gyroX=60&gyroY=89&gyroZ=45&acceleroX=60&acceleroY=89&acceleroZ=45

    path('sensor_data/', views.sensor_data, name='sensor_data'),

# http://127.0.0.1:8000/sensor_latest_data/?user_name=atharva&api_key=qx3w49r3-kifh-ix9z-04lr-mz1y4bpl8rer
# https://2421d8dd-7f48-42df-a3ff-fcf3762b1b67-00-1xu9mw62re307.worf.replit.dev/sensor_latest_data/?user_name=atharva&api_key=qx3w49r3-kifh-ix9z-04lr-mz1y4bpl8rer
# 
    path('sensor_latest_data/', views.sensor_latest_data, name='sensor_latest_data'),

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
