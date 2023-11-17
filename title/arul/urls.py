from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home-page'),
    path('main.html/', views.home,name='home-page'),
    path('about.html/',views.about,name='about-page'),
    path('product.html/',views.product,name='product-page'),
    path('service.html/',views.service,name='service-page'),
    path('contact.html/',views.contact,name='contact-page'),
    path('register.html/',views.register,name='register-page'),
    path('register',views.regdata,name='register'),
    path('login.html/',views.login,name='login-page'),
    path('login',views.logdata,name='login'),
    path('offer.html/',views.offer,name='offer-page'),
    path('enquiry.html/',views.enquiry,name='enquiry-page'),
    path('user_reg',views.user_reg,name='user_reg')
]
