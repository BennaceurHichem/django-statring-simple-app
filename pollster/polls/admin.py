from django.contrib import admin

# Register your models here.
from .models import Question,Choice




admin.site.site_header = "App Admin Header "
admin.site.site_title = "App Admin Title "
admin.site.index_header = "Welcome App Admin  "



class ChoiceInline(admin.TabularInline):
    model = Choice
    #hw many extra fields do we want 
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information',{'fields':['publish_date'],'classes':['collapse']})
                ]

    inlines =  [ChoiceInline]



#add admin functionalities 
#adding these two made these two tables appear in the admin panel
admin.site.register(Question,QuestionAdmin)
#register mean that we guves a specific independant page 
#for this regist=red model in the admin model  
#admin.site.register(Choice)

