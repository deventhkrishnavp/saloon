from django.contrib import admin
from .models import Service, GalleryItem, Review, Booking, ContactMessage, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_featured', 'order']
    list_editable = ['price', 'is_featured', 'order']
    search_fields = ['name']


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['caption', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_active', 'created_at']
    list_editable = ['is_active']
    list_filter = ['rating', 'is_active']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'date', 'time', 'status', 'created_at']
    list_editable = ['status']
    list_filter = ['status', 'date']
    search_fields = ['name', 'phone', 'email']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact', {'fields': ('address', 'phone', 'whatsapp', 'email')}),
        ('Hours', {'fields': ('hours_weekday', 'hours_weekend')}),
        ('About', {'fields': ('about_text', 'about_image')}),
        ('Social', {'fields': ('facebook_url', 'instagram_url')}),
        ('Stats', {'fields': ('total_clients', 'years_experience')}),
        ('Map', {'fields': ('google_map_embed',)}),
    )
