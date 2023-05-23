from  django.shortcuts import render

mapa={}
def game(request):
    casilla = request.GET.get("casilla")


    if casilla in mapa:
        return render(request,'game.html', {"valooor":mapa})

    mapa[casilla]=""


    var = (len(mapa))
    
    if var%2==0:

        mapa[casilla]="x"
    else:

        mapa[casilla]="O"    

    valooor = mapa[casilla]

    if   (mapa.get("1")=="x"and mapa.get("2")=="x" and mapa.get("3")=="x")|(mapa.get("1") == "O" and mapa.get("2") == "O" and mapa.get("3") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})
    elif (mapa.get("4")=="x"and mapa.get("5")=="x" and mapa.get("6")=="x")|(mapa.get("4") == "O" and mapa.get("5") == "O" and mapa.get("6") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})

    elif (mapa.get("7")=="x"and mapa.get("8")=="x" and mapa.get("9")=="x")|(mapa.get("7") == "O" and mapa.get("8") == "O" and mapa.get("9") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})

    elif (mapa.get("1")=="x"and mapa.get("4")=="x" and mapa.get("7")=="x")|(mapa.get("1") == "O" and mapa.get("4") == "O" and mapa.get("7") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})

    elif (mapa.get("2")=="x"and mapa.get("5")=="x" and mapa.get("8")=="x")|(mapa.get("2") == "O" and mapa.get("5") == "O" and mapa.get("8") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})

    elif (mapa.get("3")=="x"and mapa.get("6")=="x" and mapa.get("9")=="x")|(mapa.get("3") == "O" and mapa.get("6") == "O" and mapa.get("9") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})

    elif (mapa.get("1")=="x"and mapa.get("5")=="x" and mapa.get("9")=="x")|(mapa.get("1") == "O" and mapa.get("5") == "O" and mapa.get("9") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})
    elif (mapa.get("3")=="x"and mapa.get("5")=="x" and mapa.get("7")=="x")|(mapa.get("3") == "O" and mapa.get("5") == "O" and mapa.get("7") == "O"):
        return render(request,'ganaste.html',{"valooor":valooor})

    return render(request,'game.html', {"valooor":mapa})

def reset(request):
    mapa.clear()
    return render(request,'game.html', {})
