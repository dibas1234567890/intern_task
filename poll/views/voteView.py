from django.shortcuts import render, get_object_or_404, redirect
from poll.models import Poll, Choice
from poll.forms import addChoiceForm

from poll.forms.VoteForm import VoteForm 

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    if request.method == 'POST':
        form = VoteForm(poll, request.POST)
        if form.is_valid():
            selected_choice = form.cleaned_data['choice'] 
            for choice in selected_choice:
                choice.votes += 1 
                choice.save()

          
            return render(request, 'vote.html', { 'poll':'Success, Vote Again?' ,'form': form} )
    else:
        form = VoteForm(poll)
    return render(request, 'vote.html', { 'poll':poll, 'form':form})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    votes = Choice.objects.filter(choice__poll=poll)
    return render(request, 'results.html', {'poll': poll, 'votes': votes})

def add_options(request, id):
    poll_id = id
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        form = addChoiceForm.Choices(request.POST, poll=poll, )
        if form.is_valid():
            new_choice = form.save(commit=False)
            new_choice.poll = poll
            new_choice.save()
            return redirect('polls:results', poll_id=poll.id)
    else:
        form = addChoiceForm.Choices(request.POST, poll=poll)
    return render(request, 'add_options.html', {'poll': poll, 'form': form})


