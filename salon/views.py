from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Service, GalleryItem, Review, SiteSettings
from .forms import BookingForm, ContactForm


def get_site_settings():
    return SiteSettings.get_settings()


def home(request):
    settings = get_site_settings()
    featured_services = Service.objects.filter(is_featured=True)[:6]
    reviews = Review.objects.filter(is_active=True)[:8]
    gallery_preview = GalleryItem.objects.all()[:6]

    booking_form = BookingForm()
    if request.method == 'POST' and 'booking_submit' in request.POST:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Your appointment has been booked! We will confirm shortly.')
            return redirect('home')

    context = {
        'settings': settings,
        'featured_services': featured_services,
        'reviews': reviews,
        'gallery_preview': gallery_preview,
        'booking_form': booking_form,
    }
    return render(request, 'salon/home.html', context)


def about(request):
    settings = get_site_settings()
    context = {'settings': settings}
    return render(request, 'salon/about.html', context)


def services(request):
    settings = get_site_settings()
    all_services = Service.objects.all()
    booking_form = BookingForm()

    if request.method == 'POST' and 'booking_submit' in request.POST:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            messages.success(request, 'Appointment booked successfully!')
            return redirect('services')

    context = {
        'settings': settings,
        'all_services': all_services,
        'booking_form': booking_form,
    }
    return render(request, 'salon/services.html', context)


def gallery(request):
    settings = get_site_settings()
    items = GalleryItem.objects.all()
    categories = GalleryItem.objects.values_list('category', flat=True).distinct()
    selected = request.GET.get('category', '')
    if selected:
        items = items.filter(category=selected)

    context = {
        'settings': settings,
        'items': items,
        'categories': categories,
        'selected_category': selected,
    }
    return render(request, 'salon/gallery.html', context)


def reviews(request):
    settings = get_site_settings()
    all_reviews = Review.objects.filter(is_active=True)
    context = {'settings': settings, 'all_reviews': all_reviews}
    return render(request, 'salon/reviews.html', context)


def contact(request):
    settings = get_site_settings()
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            return redirect('contact')

    context = {'settings': settings, 'form': form}
    return render(request, 'salon/contact.html', context)


def booking_success(request):
    return render(request, 'salon/booking_success.html')
