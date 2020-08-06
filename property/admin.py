from django.contrib import admin

from .models import Flat, Complaint, Owner



@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'flat_owner__full_name__contains')
    readonly_fields = ('created_at',)
    list_display = ('address', 'price', 'new_building',
                    'construction_year')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat', 'user')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ('full_name', 'phonenumber', 'phone_pure')
    search_fields = ('full_name', 'phonenumber', 'phone_pure')
