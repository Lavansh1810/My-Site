from django.contrib import admin

from mainapp.models import Education, FontAwsIcon, Message, MyInfo, Project, Skills, Social, Testimonial, Work
from import_export.admin import ImportExportModelAdmin

@admin.register(Skills)
class SkillsAdmin(ImportExportModelAdmin):
    pass

@admin.register(MyInfo)
class MyInfoAdmin(ImportExportModelAdmin):
    pass

@admin.register(Social)
class SocialAdmin(ImportExportModelAdmin):
    pass

@admin.register(FontAwsIcon)
class FontAwsIconAdmin(ImportExportModelAdmin):
    pass

@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin):
    pass

@admin.register(Work)
class WorkAdmin(ImportExportModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(ImportExportModelAdmin):
    pass