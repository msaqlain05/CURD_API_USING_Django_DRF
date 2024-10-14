from django.contrib import admin

# Register your models here.
from api.models import Student

# here register model in admin page
@admin.register(Student)

class Studentdata(admin.ModelAdmin):
    list_display=('id','name','fname','Class','roll_no')
    