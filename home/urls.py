from django.urls import path
from.views import(
    Blog,
    createBlog,
    deleteBlog,
)
urlpatterns = [

    path('', Blog),
    path('create/', createBlog),
    path('delete/<int:id>', deleteBlog)
]

