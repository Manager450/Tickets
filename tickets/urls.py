from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('bus/<int:bus_id>/', views.bus_details, name='bus_details'),
    path('book/<int:bus_id>/', views.book_bus, name='book_bus'),
    path('payment/<int:booking_id>/', views.payment, name='payment'),
    path('payment_success/<int:payment_id>/', views.payment_success, name='payment_success'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),
    path('booking/<int:booking_id>/', views.booking_details, name='booking_details'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('help/', views.help_view, name='help'),
    path('faqs/', views.faqs, name='faqs'),
    path('review/<int:bus_id>/', views.review_bus, name='review_bus'),
]
