# author - Smit Bhavsar
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    

def remove_punctuation(text):
    PUNCTUATIONS = '''!"#$%&'()*+,-./:;<=>?@[\]^_{|}~'''
    return "".join(char for char in text if char not in PUNCTUATIONS)


def convert_to_uppercase(text):
    return text.upper()


def analyze(request):
    text = request.POST.get("text", "")
    remove_punc = request.POST.get("removepunc", "off")
    full_caps = request.POST.get("fullcaps", "off")

    if not text:
        return HttpResponse("<h1>Error: No text provided</h1>")

    analyzed_text = text
    purposes = []

    if remove_punc == "on":
        analyzed_text = remove_punctuation(analyzed_text)
        purposes.append("Removed Punctuations")

    if full_caps == "on":
        analyzed_text = convert_to_uppercase(analyzed_text)
        purposes.append("Converted to Uppercase")

    if not purposes:
        return HttpResponse("<h1>Error: No option selected</h1>")

    context = {
        "Purpose": ", ".join(purposes),
        "analyzed_text": analyzed_text
    }

    return render(request, "analyze.html", context)
