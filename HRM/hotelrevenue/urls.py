# bookings/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('check-in-guest/', views.check_in_guest, name='check_in_guest'),
    path('booking-success/', views.booking_success, name='booking_success'),

    # Add more URL patterns as needed
]
