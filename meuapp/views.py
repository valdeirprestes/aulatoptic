from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Helloworld")
def soma(request, num1 , num2):
    return HttpResponse(f" A soma de {num1} mais {num2} é {num1 + num2}")
def potencia(request, base , expoente):
    return HttpResponse(f" A potencia com base {base} e expoente {expoente} é {base ** expoente}")
def potencia10(request,  expoente):
    return HttpResponse(f" A potencia com base 10 e expoente {expoente} é {10 ** expoente}")
def meutemplate(request):
    titulo ="Pagina teste template"
    lista = ["CSS", "Javascript", "HTML"]
    return render(request, "exemplo/index.html", {"lista":lista,"titulo":titulo})
