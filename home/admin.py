from django.contrib import admin
from home.models import Book,Author,Genre,Student



# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    #fields=[('name','purchase_date'),('genre','author')]
    #list_filter=('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter)) #nesting should be done with a parameter when that parameter belong to some other table
       #filter 
    list_filter=('name','purchase_date','book_author')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # search_fields=('student_name','book_took')
    pass