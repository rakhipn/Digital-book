from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('genrepage/<itemcatg>/', views.genrepage, name="genrepage"),
    path('singleproduct/<int:dataid>', views.singleproduct, name="singleproduct"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('savecart/', views.savecart, name="savecart"),
    path('deletecart/<int:dataid>', views.deletecart, name="deletecart"),
    path('savecartdetails/', views.savecartdetails, name="savecartdetails"),
    path('signuppage/', views.signuppage, name="signuppage"),
    path('savesignup/', views.savesignup, name="savesignup"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/', views.userlogout, name="userlogout")

]
