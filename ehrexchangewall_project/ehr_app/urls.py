from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),

    # path("upload_file/", views.upload_file, name="upload_file"),
    path('upload_files/', views.upload_files, name='upload_files'),

    path("dataset_view/<str:myslug>", views.dataset_view, name="dataset_view"),
    # /dataset_view/ehr-dataset-1/

    path('all_ehr_datasets/', views.all_ehr_datasets, name='all_ehr_datasets'),


    
    path("privacypolicy/", views.privacypolicy, name="privacypolicy"),
    path("upload_ehr/", views.upload_ehr, name="upload_ehr"),
    path("support/", views.support, name="support"),


    path('user_login/',      views.user_login,     name='user_login'),
    path('user_logout/',     views.user_logout,    name='user_logout'),
    path('user_register/',   views.user_register,  name='user_register'),

    # path('apikeyGen/', views.your_view_function, name='your_view_function'),








    # path("business", views.business, name="Business"),
    # path("about/", views.about, name="AboutUs"),
    # path("contact/", views.contact, name="ContactUs"),
    # # path("products/<int:myid>", views.productView, name="ProductView"),
    # path("products/<str:myslug>", views.productView, name="ProductView"),

]