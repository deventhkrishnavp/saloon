"""
Seed script: creates default SiteSettings, Services, and Reviews
Run with: python manage.py shell < seed_data.py
"""
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groomstudio.settings')
django.setup()

from salon.models import Service, Review, SiteSettings

# Site settings
s = SiteSettings.get_settings()
s.phone = '+91 98765 43210'
s.whatsapp = '919876543210'
s.email = 'groomstudio@email.com'
s.address = 'Ashikinte Kada, Kerala, India'
s.hours_weekday = '9:00 AM – 9:00 PM'
s.hours_weekend = '8:00 AM – 10:00 PM'
s.total_clients = 500
s.years_experience = 5
s.save()
print("✓ SiteSettings saved")

# Services
services = [
    ('Haircut', 'Classic to modern — fade, undercut, textured crop, or your own style. Personalised to your face shape.', 150, 'fa-scissors', True, 1),
    ('Beard Trim & Shape', 'Sharp beard shaping, lineup, and fade for a clean polished look every time.', 100, 'fa-user', True, 2),
    ('Facial Treatment', 'Deep-cleansing facials using premium skincare products for fresh, glowing skin.', 300, 'fa-spa', True, 3),
    ('Hair Color', 'Vibrant color, highlights, or balayage by professional colourists.', 500, 'fa-magic', True, 4),
    ('Scalp Treatment', 'Nourishing scalp massages to promote hair growth and eliminate dandruff.', 250, 'fa-droplet', True, 5),
    ('Hair Spa', 'Complete hair spa to strengthen, add shine, and restore moisture.', 400, 'fa-star', True, 6),
    ('De-Tan Treatment', 'Remove sun tan and revive your natural skin tone effectively.', 200, 'fa-hand-sparkles', False, 7),
    ('Hair Straightening', 'Smoothening and keratin treatments for frizz-free manageable hair.', 800, 'fa-wind', False, 8),
    ("Kids Haircut", 'Fun, friendly haircuts for the little ones!', 100, 'fa-child', False, 9),
]
Service.objects.all().delete()
for name, desc, price, icon, featured, order in services:
    Service.objects.create(name=name, description=desc, price=price, icon=icon, is_featured=featured, order=order)
print(f"✓ {len(services)} Services created")

# Reviews
reviews = [
    ('Arun Kumar', 'Regular Customer', 5, "Best haircut I've ever had! Very professional and clean atmosphere. The barber understood exactly what I wanted. Highly recommend Groom Studio!"),
    ('Rahul Menon', 'Loyal Client', 5, 'Amazing beard shaping and fade. The staff are super friendly and the place is very neat. Perfect salon for men in Ashikinte Kada!'),
    ('Siddharth V', 'Happy Client', 5, 'Great value for money! The hair color turned out better than I expected. Will definitely come back again and again.'),
    ('Vibin Nair', 'Regular Customer', 5, 'Very skilled barbers. The scalp massage was so relaxing! The salon feels premium without being expensive. Love this place!'),
    ('Prasanth Joy', 'Loyal Client', 5, 'Clean, fast, and spot on every single time. Groom Studio has been my go-to salon for years. Cannot recommend enough!'),
    ('Mohammed Ashiq', 'Family Customer', 5, 'Excellent service and a very warm welcome. The kids haircut section is great too — my son loved it!'),
    ('Anand Pillai', 'Happy Client', 5, 'Top-notch haircut and beard trim. The place is immaculately clean. Pricing is very fair for the quality you get.'),
    ('Jithin Raju', 'Loyal Client', 5, 'Friendly staff, great ambiance and an awesome fade. I drive all the way from Ernakulam just for a haircut here — worth every km!'),
]
Review.objects.all().delete()
for name, role, rating, text in reviews:
    Review.objects.create(name=name, role=role, rating=rating, text=text, is_active=True)
print(f"✓ {len(reviews)} Reviews created")
print("\n✅ Seed data complete!")
