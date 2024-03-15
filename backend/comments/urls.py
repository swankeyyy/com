from django.urls import path
from . import views

urlpatterns = [
    path('addcomment/<int:pk>', views.AddComment.as_view(), name="add_comment"),
    path('deletecomment/<int:pk>', views.DeleteComment.as_view(), name="delete_comment"),
]