from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.utils import timezone
from pytz import timezone as pytz_timezone

class ClassListView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                cls = FitnessClass.objects.get(pk=pk)
            except FitnessClass.DoesNotExist:
                return Response({"error": "Class not found."}, status=404)
            serializer = FitnessClassSerializer(cls, context={'request': request})
            return Response(serializer.data)

        queryset = FitnessClass.objects.filter(active=True).order_by('start_time')
        serializer = FitnessClassSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class BookingCreateView(APIView):
    def post(self, request):
        class_id = request.data.get("class_id")
        client_name = request.data.get("client_name")
        client_email = request.data.get("client_email")

        if not all([class_id, client_name, client_email]):
            print("inisdeeeee")
            return Response({"error": "Missing required fields."}, status=400)

        try:
            fitness_class = FitnessClass.objects.get(pk=class_id)
        except FitnessClass.DoesNotExist:
            return Response({"error": "Fitness class not found."}, status=404)

        if fitness_class.available_slots <= 0:
            return Response({"error": "No slots available."}, status=400)

        Booking.objects.create(
            fitness_class=fitness_class,
            client_name=client_name,
            client_email=client_email
        )

        fitness_class.available_slots -= 1
        fitness_class.save()

        return Response({"message": "Booking successful."}, status=201)

class BookingListView(APIView):
    def get(self, request):
        print("request.query_params",request.query_params)
        email = request.query_params.get("client_email")
        if not email:
            return Response({"error": "Email is required"}, status=400)

        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
