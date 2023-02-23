from django.contrib import admin

# Register your models here.
from . models import Patinet
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['fname','lname','phone','email']

admin.site.register(Patinet,PostAdmin)