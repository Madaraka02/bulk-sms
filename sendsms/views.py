from django.shortcuts import render,redirect
from .models import *
from .forms import *
from .sendsms import send
from .resources import MessageResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse
import phonenumbers

# Create your views here.
def home(request):
    # myMessyourstring = ''.join(('L','yourstring','LL'))
    # form = MessageForm()
    if request.method == 'POST':
        # form = MessageForm(request.POST,request.FILES)
        # if form.is_valid():
        #     mess = form.save()
        # mess = request.FILES['myMess']
        mess = request.POST['myMess']
        message_resource = MessageResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request, 'Wrong format')
            return render(request, 'home.html')
        imported_data = dataset.load(new_person.read(), format='xlsx')
        for data in  imported_data:
            value = Message(
                data[0],
                data[1],
                str(data[2]),
            )
            
            value.information=mess
            value.save()
            print(value.information)
            
        
        persons = Message.objects.all()  
        for person in persons:
            phonen = str(person.phone_number)
            text = person.information
            phone_num = ''.join(('+',phonen))
            send(phone_num, text)
            print(type(phone_num),phone_num) 

            messages.success(request, "Data was added and message was  send successfully")
            return redirect('home')

    return render(request, 'home.html')    



# import phonenumbers
# x = phonenumbers.parse("+442083661177", None)

def message(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
            info=form.cleaned_data['information']


            
            persons = Message.objects.all()  
            for person in persons:
                phonen = str(person.phone_number)
                phone_num = ''.join(('+',phonen))
                send(phone_num, info)

                messages.success(request, "Message transmitted successfully")
                return redirect('message')

    return render(request, 'message.html', {'form':form})              