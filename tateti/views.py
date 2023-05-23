from  django.shortcuts import render

mapa={}
def game(request):
    casilla = request.GET.get("casilla")

    # if casilla == None:
    if casilla in mapa:
        return render(request,'game.html', {"caca":mapa})

        
    mapa[casilla]=""

    print(len(mapa)) 
    var = (len(mapa))
    
    if var%2==0:
        # print(var)
        mapa[casilla]="x"
    else:
        # print(print())
        mapa[casilla]="O"    

    # print(casilla)
    print(mapa)
     
    # request.session[casilla] = "O"


    return render(request,'game.html', {"caca":mapa})

def reset(request):
    mapa.clear()
    return render(request,'game.html', {})
