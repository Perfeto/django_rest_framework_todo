from django.contrib import admin

# Register your models here.
from testapp.models import ToDoTask


@admin.register(ToDoTask)
class ToDoTaskAdmin(admin.ModelAdmin):
    model = ToDoTask
    list_display = ('id', 'title', 'description', 'change_date', 'owner', 'status',)
    ordering = ('change_date',)
    search_fields = ('id', 'title', 'description', 'owner__username', 'status',)
