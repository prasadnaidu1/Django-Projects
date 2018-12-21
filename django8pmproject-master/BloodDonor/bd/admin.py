from django.contrib import admin

from .models import State
from .models import City
from .models import DonorRegister
from .models import OrigranizationRegister

admin.site.register(State)
admin.site.register(City)
admin.site.register(DonorRegister)
admin.site.register(OrigranizationRegister)
