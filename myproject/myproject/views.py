from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drfapp.models import User, Tour, Booking, Payment, Feedback
from rest_framework import status
from django.shortcuts import get_object_or_404
from drfapp.serializers import (
    UserSerializer,
    TourSerializer,
    BookingSerializer,
    PaymentSerializer,
    FeedbackSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes


class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Create a new user
            user = serializer.save()
            
            # Generate a new authentication token
            token, created = Token.objects.get_or_create(user=user)

            # Return user and token details in the response
            return Response({
                'user': UserSerializer(user).data,
                'token': token.key,
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class UserDetailView(APIView):
    def get(self, request, userID):
        user = get_object_or_404(User, user_id=userID)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, userID):
        user = get_object_or_404(User, user_id=userID)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, userID):
        user = get_object_or_404(User, user_id=userID)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class UserBookingListView(APIView):
    def get(self, request, userID):
        bookings = Booking.objects.filter(user__user_id=userID)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class UserFeedbackListView(APIView):
    def get(self, request, userID):
        feedback = Feedback.objects.filter(user__user_id=userID)
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class BookingDetailView(APIView):
    def get(self, request, bookingID):
        booking = get_object_or_404(Booking, booking_id=bookingID)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def put(self, request, bookingID):
        booking = get_object_or_404(Booking, booking_id=bookingID)
        serializer = BookingSerializer(booking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, bookingID):
        booking = get_object_or_404(Booking, booking_id=bookingID)
        booking.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TourBookingListView(APIView):
    def get(self, request, tourID):
        bookings = Booking.objects.filter(tour__tour_id=tourID)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PaymentCreateView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class PaymentDetailView(APIView):
    def get(self, request, paymentID):
        payment = get_object_or_404(Payment, payment_id=paymentID)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class BookingPaymentListView(APIView):
    def get(self, request, bookingID):
        payments = Payment.objects.filter(booking__booking_id=bookingID)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class FeedbackCreateView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class FeedbackDetailView(APIView):
    def get(self, request, feedbackID):
        feedback = get_object_or_404(Feedback, feedback_id=feedbackID)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    def put(self, request, feedbackID):
        feedback = get_object_or_404(Feedback, feedback_id=feedbackID)
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, feedbackID):
        feedback = get_object_or_404(Feedback, feedback_id=feedbackID)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TourListView(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class TourDetailView(APIView):
    def get(self, request, tourID):
        tour = get_object_or_404(Tour, tour_id=tourID)
        serializer = TourSerializer(tour)
        return Response(serializer.data)

    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tourID):
        tour = get_object_or_404(Tour, tour_id=tourID)
        serializer = TourSerializer(tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tourID):
        tour = get_object_or_404(Tour, tour_id=tourID)
        tour.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#from drfapp.serializers import StudentSerializer 
# from drfapp.models import Student

# class TestView(APIView):

#     permission_classes = (IsAuthenticated,)
#     def get(self, request, *args, **kwargs):
#         qs = Student.objects.all()
#         serializer  = StudentSerializer(qs, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer  = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error)
