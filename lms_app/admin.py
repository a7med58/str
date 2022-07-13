from django.contrib import admin
from .models import  Category,Book,Dept,Status
from .models import Staff,Grade_Staff,Status_Staff
from .models import  Student,Category_Student,Grade_Student

# Register your models here.

    
    
class BookAdmin (admin.ModelAdmin):
    list_display = ['title','author','category','depart', 'stat','modarg' ]
    list_filter = ['category','thidate','depart', 'stat' ]
    search_fields = ['title' ]
    list_display_links = ['title' ]
    list_editable = ['author','category','depart', 'stat','modarg' ]

class StudentAdmin (admin.ModelAdmin):
    list_display = ['name','phone','email', 'date_of_hiring']
    list_display_links = ['name' ]
    list_filter = ['category_student','grade_student']
    list_editable = ['phone','email', 'date_of_hiring']

class StaffAdmin (admin.ModelAdmin):
    list_display = ['name','phone','email', 'date_of_hiring']
    list_display_links = ['name' ]
    list_filter = ['status_staff','grade_staff','depart']
    list_editable = ['phone','email', 'date_of_hiring']
    
    
admin.site.register(Book,BookAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Staff,StaffAdmin)  
admin.site.register(Category)
admin.site.register(Status)
admin.site.register(Dept)
admin.site.register(Category_Student)  
admin.site.register(Grade_Student)  
admin.site.register(Grade_Staff)     
admin.site.register(Status_Staff)     


admin.site.site_header = "أدارة مستودع الرسائل"   
admin.site.site_title = "مستودع الرسائل"         
      
