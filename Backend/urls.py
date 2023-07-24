from django.urls import path
from Backend import views

urlpatterns = [
    path('indexpage/', views.indexpage, name="indexpage"),
    path('categorypage/', views.categorypage, name="categorypage"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('displaycategory/', views.displaycategory, name="displaycategory"),
    path('editcategory/<int:dataid>', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:dataid>', views.deletecategory, name="deletecategory"),
    path('productpage/', views.productpage, name="productpage"),
    path('productsave/', views.productsave, name="productsave"),
    path('productdisplay/', views.productdisplay, name="productdisplay"),
    path('editproduct/<int:dataid>', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>', views.updateproduct, name="updateproduct"),
    path('deleteproduct/<int:dataid>', views.deleteproduct, name="deleteproduct"),
    path('displaycart/', views.displaycart, name="displaycart"),
    path('cartcustomerdisplay/', views.cartcustomerdisplay, name="cartcustomerdisplay")
]
