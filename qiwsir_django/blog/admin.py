from django.contrib import admin
from .models import BlogArticles


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")  # 列表页展示字段
    list_filter = ("publish", "author")  # 过滤器
    search_fields = ("title", "body")  # 搜索框
    raw_id_fields = ("author",)  # 详情页 外键
    date_hierarchy = "publish"  # 列表页 时间
    ordering = ['-publish', 'author']  # 列表页 默认排序


admin.site.register(BlogArticles, BlogArticlesAdmin)
