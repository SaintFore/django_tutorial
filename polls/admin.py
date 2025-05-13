from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently") # 添加列表显示的字段
    list_filter = ["pub_date"] # 添加过滤器
    search_fields = ["question_text"] # 添加搜索栏


admin.site.register(Question, QuestionAdmin)
