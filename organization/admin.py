from django.contrib import admin

from .models import (Organization, BoardMembers)

admin.site.register((Organization, BoardMembers))
