"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 
from . import views
from django.views.generic import RedirectView

# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    # Class based view
    # path('', TestView.as_view(), name='test'),
    # path('api/token/', obtain_auth_token, name='obtain')
    path('users/<int:userID>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/', views.UserDetailView.as_view(), name='user-create'),
    path('users/<int:userID>/bookings/', views.UserBookingListView.as_view(), name='user-bookings'),
    path('users/<int:userID>/feedback/', views.UserFeedbackListView.as_view(), name='user-feedback'),

    # Booking Endpoints
    path('bookings/<int:bookingID>/', views.BookingDetailView.as_view(), name='booking-detail'),
    path('bookings/', views.BookingDetailView.as_view(), name='booking-create'),
    path('tours/<int:tourID>/bookings/', views.TourBookingListView.as_view(), name='tour-bookings'),

    # Payment Endpoints
    path('payments/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:paymentID>/', views.PaymentDetailView.as_view(), name='payment-detail'),
    path('bookings/<int:bookingID>/payments/', views.BookingPaymentListView.as_view(), name='booking-payments'),

    # Feedback Endpoints
    path('feedback/', views.FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/<int:feedbackID>/', views.FeedbackDetailView.as_view(), name='feedback-detail'),

    # Tour Endpoints
    path('listtours/', views.TourListView.as_view(), name='tour-list'),
    path('listtours/<int:tourID>/', views.TourDetailView.as_view(), name='tour-detail'), # Gets a particular tour
    path('tours/', views.TourListView.as_view(), name='tour-detail'), # Post tour data to database (Post Request)
    path('', RedirectView.as_view(url='listtours/<int:tourID>/')),
]
