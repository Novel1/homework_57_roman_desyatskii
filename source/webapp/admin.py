from django.contrib import admin

from webapp.models import Task, Status, Type


# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'created_at')
    list_filter = ('id', 'summary', 'description', 'created_at')
    search_fields = ('summary', 'description')
    fields = ('summary', 'description', 'type', 'status', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


admin.site.register(Type, TypeAdmin)