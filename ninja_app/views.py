from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# Create your views here.
def index(request):
    if 'my_list' not in request.session:
        request.session['my_list'] = []
    if 'contador' not in request.session:
        request.session['contador'] = 0
    mensaje = request.session['my_list']
    count = request.session['contador']
    print(mensaje)
    contexto = {
        'mensajes': mensaje,
        'count': count
    }
    return render(request, 'index.html', contexto)

def farm(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    gold = random.randint(10, 20)
    request.session['contador'] += int(gold) 
    mensajes = f"Earned {gold} from the farm! "
    mensaje = mensajes + time
    request.session['my_list'].append(mensaje)
    request.session.save()
    return redirect('/')

def cave(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    gold = random.randint(5, 10)
    request.session['contador'] += gold 
    mensajes = f"Earned {gold} from the cave! "
    mensaje = mensajes + time
    request.session['my_list'].append(mensaje)
    request.session.save()
    return redirect('/')

def house(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    gold = random.randint(2, 5)
    request.session['contador'] += gold 
    mensajes = f"Earned {gold} from the house! " 
    mensaje = mensajes + time
    request.session['my_list'].append(mensaje)
    request.session.save()
    return redirect('/')

def casino(request):
    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    gold = random.randint(0, 50)
    request.session['contador'] -= gold 
    mensajes = f"Earned {gold} from the casino! " 
    mensaje = mensajes + time
    request.session['my_list'].append(mensaje)
    request.session.save()
    return redirect('/')

def reset(request):
    del request.session['my_list']
    del request.session['contador']
    return redirect('/')
    