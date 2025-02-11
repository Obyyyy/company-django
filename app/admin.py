from django.contrib import admin
from django.http import HttpRequest
from app.models import GeneralInfo

# Register your models here.

@admin.register(GeneralInfo)
class GeneralInfoAdmin(admin.ModelAdmin):
  # Untuk menampilkan kolom yang ada di tabel GeneralInfo di dashboard
  list_display = [
    'company_name',
    'location',
    'email',
    'phone',
    'open_hours',
  ]

  # Untuk menghapus izin menambah data, mengubah data, dan menghapus data
  # def has_add_permission(self, request: HttpRequest) -> bool:
  #   # return super().has_add_permission(request)
  #   return False
  
  # def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
  #   # return super().has_change_permission(request, obj)
  #   return False
  
  # def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
  #   # return super().has_delete_permission(request, obj)
  #   return False

  # Menentukan kolom yang tidak bisa diubah
  readonly_fields = [
    'email',
  ]