from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus, Booking, Payment, Review
from .forms import BookingForm, ReviewForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    return render(request, 'tickets/home.html')

def search_results(request):
    if request.method == 'GET':
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        buses = Bus.objects.filter(source=source, destination=destination)
        return render(request, 'tickets/search_results.html', {'buses': buses})

def bus_details(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    return render(request, 'tickets/bus_details.html', {'bus': bus})

@login_required
def book_bus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.bus = bus
            booking.save()
            return redirect('payment', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'tickets/book_bus.html', {'form': form, 'bus': bus})

@login_required
def payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        amount = booking.bus.price
        # Here you would integrate payment processing logic
        payment = Payment.objects.create(booking=booking, amount=amount, status='Success')
        return redirect('payment_success', payment_id=payment.id)
    return render(request, 'tickets/payment.html', {'booking': booking})

@login_required
def payment_success(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    return render(request, 'tickets/payment_success.html', {'payment': payment})

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'tickets/my_bookings.html', {'bookings': bookings})

@login_required
def booking_details(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'tickets/booking_details.html', {'booking': booking})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'tickets/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'tickets/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'tickets/profile.html')

def about(request):
    return render(request, 'tickets/about.html')

def terms(request):
    return render(request, 'tickets/terms.html')

def privacy(request):
    return render(request, 'tickets/privacy.html')

def help_view(request):
    return render(request, 'tickets/help.html')

def faqs(request):
    return render(request, 'tickets/faqs.html')

def settings(request):
    return render(request, 'tickets/settings.html')

@login_required
def review_bus(request, bus_id):
    bus = get_object_or_404(Bus, id=bus_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.bus = bus
            review.user = request.user
            review.save()
            return redirect('bus_details', bus_id=bus.id)
    else:
        form = ReviewForm()
    return render(request, 'tickets/review_bus.html', {'form': form, 'bus': bus})

