from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from .models import Car, Booking
from .forms import UserRegisterForm, BookingForm

# Home View
def home(request):
    return render(request, 'rentals/home.html')

# Car List View
def car_list(request):
    cars = Car.objects.filter(availability=True)
    return render(request, 'rentals/car_list.html', {'cars': cars})

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('rentals:login')  # Use namespaced URL
    else:
        form = UserCreationForm()
    return render(request, 'rentals/register.html', {'form': form})

# Custom Authentication Views
class CustomLoginView(LoginView):
    template_name = 'rentals/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'rentals/logout.html'

# Booking View
def book_car(request):
    cars = Car.objects.filter(availability=True)
    
    if request.method == "POST":
        car_id = request.POST.get("car")
        pickup_date = request.POST.get("pickup_date")
        return_date = request.POST.get("return_date")
        customer_name = request.POST.get("customer_name")
        contact = request.POST.get("contact")

        # Get the selected car object
        car = get_object_or_404(Car, id=car_id)

        # Create a new booking
        booking = Booking.objects.create(
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
            customer_name=customer_name,
            contact=contact,
        )

        messages.success(request, f"Booking confirmed for {car.name} from {pickup_date} to {return_date}.")
        return redirect('rentals:car_list')  # Redirect to car list after booking

    return render(request, "rentals/book.html", {"cars": cars})

# Static Page Views
def about(request):
    return render(request, 'rentals/about.html')

def contact_us(request):
    return render(request, 'rentals/contact_us.html')

def our_cars_view(request):
    cars = Car.objects.all()  # Fetch all cars from the database
    return render(request, 'rentals/our_cars.html', {'cars': cars})

from django.shortcuts import render, get_object_or_404, redirect
from rentals.models import Car, Booking
from .forms import BookingForm

def book_now_view(request, car_id=None):
    cars = Car.objects.all()  # Fetch all available cars
    
    selected_car = None
    if car_id:  # If a car is pre-selected
        selected_car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.car = Car.objects.get(id=request.POST['car'])  # Assign selected car
            booking.save()
            return redirect('rentals:our_cars')  # Redirect after successful booking
    else:
        form = BookingForm()

    return render(request, 'rentals/book_now.html', {'cars': cars, 'selected_car': selected_car, 'form': form})

def book_car(request):
    cars = Car.objects.filter(availability=True)  # Fetch available cars
    if request.method == "POST":
        car_id = request.POST.get("car")
        pickup_date = request.POST.get("pickup_date")
        return_date = request.POST.get("return_date")
        customer_name = request.POST.get("customer_name")
        contact = request.POST.get("contact")

        # Get the selected car object
        car = Car.objects.get(id=car_id)

        # Create a new booking
        booking = Booking.objects.create(
            car=car,
            pickup_date=pickup_date,
            return_date=return_date,
            customer_name=customer_name,
            contact=contact,
        )

        return HttpResponse(f"Booking confirmed for {car.name} from {pickup_date} to {return_date}.")

    return render(request, "rentals/book.html", {"cars": cars})  # Ensure template path is correct


def car_list(request):
    cars = Car.objects.filter(availability=True)
    return render(request, 'rentals/car_list.html', {'cars': cars})