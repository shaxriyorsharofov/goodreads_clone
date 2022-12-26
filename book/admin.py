from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')
    list_filter = ['title']
    list_display = ('title',  'isbn')

admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor)
admin.site.register(BookReview)
admin.site.register(Author)
