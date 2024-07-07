from django.shortcuts import render
from django.views import View
from poll.forms.createPoll_form import pollForm
#from poll.forms.VoteForm import VoteForm

from django.shortcuts import redirect 
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from poll.forms.optionsForm import optionForm
from poll.models import Poll
class pollView(View):

    def activePolls(request):
        all_polls = Poll.objects.all()
        paginator = Paginator(all_polls,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'activepolls.html', { 'all': all_polls, 'page_obj':page_obj}) 
        
    @login_required
    def createPoll(request): 
        form = pollForm(request.POST)
        context = {"form":form}
        if form.is_valid():
            
            poll = form.save()
            return redirect('createchoices' + '/' + str(poll.id))
        return render(request, 'createpoll.html', context)
    
    @login_required
    def createOptions(request, id): 
        form = optionForm(request.POST)
        context = {"form":form}
        if form.is_valid():
            context = {'form': "success"} 
            form.save()
            return render(request, 'activepolls.html', context)
        return render(request, 'createpoll.html', context)
    
    
    
