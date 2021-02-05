from django.contrib import admin

from core.models import ActivityLog, Todo, Receita


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('receita', 'introducao', 'ingredientes', 'preparo', 'foto', 'autor')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Receita, ReceitaAdmin)
