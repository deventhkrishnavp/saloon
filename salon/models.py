from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Service(models.Model):
    ICON_CHOICES = [
        ('fa-scissors', 'Scissors'),
        ('fa-user', 'User'),
        ('fa-spa', 'Spa'),
        ('fa-star', 'Star'),
        ('fa-cut', 'Cut'),
        ('fa-magic', 'Magic'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    icon = models.CharField(max_length=50, default='fa-scissors')
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('haircut', 'Haircut'),
        ('beard', 'Beard'),
        ('color', 'Color'),
        ('facial', 'Facial'),
        ('other', 'Other'),
    ]
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='haircut')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.caption or f"Gallery Item {self.pk}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, default='Customer')
    rating = models.PositiveIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    text = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.rating}★"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%d %b %Y')}"


class SiteSettings(models.Model):
    address = models.TextField(default='Ashikinte Kada, Kerala, India')
    phone = models.CharField(max_length=20, default='+91 98765 43210')
    whatsapp = models.CharField(max_length=20, default='919876543210')
    email = models.EmailField(default='groomstudio@email.com')
    hours_weekday = models.CharField(max_length=50, default='9:00 AM - 9:00 PM')
    hours_weekend = models.CharField(max_length=50, default='8:00 AM - 10:00 PM')
    about_text = models.TextField(
        default='Groom Studio is a premium men\'s salon in Ashikinte Kada, offering top-quality haircuts, beard trims, and grooming services. We combine skill, style, and a welcoming atmosphere to make you look and feel your best.'
    )
    about_image = models.ImageField(upload_to='about/', null=True, blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    total_clients = models.PositiveIntegerField(default=500)
    years_experience = models.PositiveIntegerField(default=5)
    google_map_embed = models.TextField(
        blank=True,
        default='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3928.5!2d76.25!3d10.15!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMTDCsDA5JzAwLjAiTiA3NsKwMTUnMDAuMCJF!5e0!3m2!1sen!2sin!4v1234567890'
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'

    def save(self, *args, **kwargs):
        # Singleton: only one instance allowed
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_settings(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
