from django.contrib import admin

# Register your models here.
from .models import Phase, Project, Task

class ProjectList(admin.ModelAdmin):
    list_display = ('project_name', 'manager', 'start_date', 'end_date')

class PhaseList(admin.ModelAdmin):
    list_display = ('project', 'phase_title', 'description', 'start_date', 'end_date')

admin.site.site_header = 'Construction Monitoring'
admin.site.register(Project, ProjectList)
admin.site.register(Phase, PhaseList)
admin.site.register(Task)

