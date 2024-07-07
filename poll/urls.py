from django.urls import path

from poll.views import pollView, voteView
from . import views

urlpatterns = [
    path('vote/<int:poll_id>/', voteView.vote, name='vote'),
    path('<int:poll_id>/results/', voteView.results, name='results'),
    path('', pollView.pollView.activePolls, name='polls'),
    path('newpolls', pollView.pollView.createPoll, name='newpoll'),
    path('addchoices/<int:id>', voteView.add_options, name='addoptions'),
    path('createchoices/<int:id>', pollView.pollView.createOptions, name='createoptions'),
    
]
