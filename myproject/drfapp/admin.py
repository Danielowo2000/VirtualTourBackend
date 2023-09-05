from django.contrib import admin
from .models import User, Tour, Booking, Payment, Feedback

# Register your models here.
admin.site.register(User)
admin.site.register(Tour)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Feedback)