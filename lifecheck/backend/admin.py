from django.contrib import admin
from .models import Patient,symptom,disease,Contact

admin.site.register(Patient)
admin.site.register(symptom)
admin.site.register(disease)
admin.site.register(Contact)
