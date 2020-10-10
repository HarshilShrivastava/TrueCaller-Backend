from .views import SearchContact, markSpam, detailView
from django.urls import path

urlpatterns = [
    path('Search/', SearchContact.as_view()),
    path('mark/<int:id>', markSpam, ),
    path('Detail/<int:id>', detailView),

]
