from  django.shortcuts import render


def game(request):
    casilla = request.GET.get("casilla")

    
    request.session[casilla] = "O"


    return render(request,'game.html', {"caca":request.session})

def reset(request):
    request.session.clear()
    return render(request,'game.html', {})
