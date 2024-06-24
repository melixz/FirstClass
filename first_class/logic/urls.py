from django.urls import path, include

from . import views

urlpatterns = [
    # path('', index_view, name='index'),
    # path('feedback', FeedbackView.as_view(), name='feedback'),
    path('', views.feedback, name='index'),

]
