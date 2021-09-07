from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PollForm
from .models import Poll
# Create your views here.
def index(request):
    polls=Poll.objects.all()
    context={
        'polls':polls
    }
    return render(request,"index.html",context)

def create(request):
    post=Poll.objects.all()
    if request.method=='POST':
        form=PollForm(request.POST)
        if form.is_valid():
            print("ok")
            form.save()
            return redirect("index")
    else:
        form=PollForm()
    context={'post':post,'form':form}
    return render(request,'create.html',context)

def vote(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)

    if request.method=='POST':
        selected=request.POST['poll']
        print(selected)
        if selected == 'option1':
            poll.opt1_count+=1
        elif selected == 'option2':
            poll.opt2_count += 1
        elif selected == 'option3':
            poll.opt3_count += 1
        else:
            return HttpResponse(400,'Invalid Form Option')
        poll.save()
        return redirect('index')
    context = {
        'poll': poll,
    }
    return render(request,"vote.html",context)

def results(request,poll_id):
    poll=Poll.objects.get(pk=poll_id)

    context={'poll':poll}
    return render(request,"results.html",context)


