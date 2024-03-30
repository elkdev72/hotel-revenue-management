from django.shortcuts import render,redirect

# Create your views here.
from .models import Room, Booking, Guest
from .forms import BookingForm, GuestForm

def book_room(request, room_id):
    room = Room.objects.get(pk=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            guest = form.save()
            check_in_date = form.cleaned_data['check_in_date']
            check_out_date = form.cleaned_data['check_out_date']
            total_amount = room.price_per_night * (check_out_date - check_in_date).days
            booking = Booking.objects.create(room=room, guest=guest, check_in_date=check_in_date, check_out_date=check_out_date, total_amount=total_amount)
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'room': room, 'form': form})


def booking_success(request):
    return render(request, 'booking_success.html')  # Replace 'booking_success.html' with your template name
def check_in_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save()
            return redirect('check_in_success')
    else:
        form = GuestForm()
    return render(request, 'check_in_guest.html', {'form': form})