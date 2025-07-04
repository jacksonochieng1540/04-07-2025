from django.contrib import admin

# Register your models here.
from.models import User,DoctorProfile,PatientProfile,VitalSigns
admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(VitalSigns)
admin.site.register(User)