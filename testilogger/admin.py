from django.contrib import admin
from .models import TestCase

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'executed_at')
    list_filter = ('status', 'executed_at')
    search_fields = ('title', 'description')
    ordering = ('-executed_at',)

