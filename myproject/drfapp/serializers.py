from rest_framework import serializers
from .models import User, Tour, Booking, Payment, Feedback
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'username', 'email', 'profile_data')

class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = ('tour_id', 'destination_name', 'description', 'duration', 'price')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id', 'user', 'tour', 'booking_date', 'status')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id', 'booking', 'payment_amount', 'payment_date')

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('feedback_id', 'user', 'tour', 'rating', 'comments')
