#this is created by me --Danish Jamal

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyse(request):
  djtext=request.GET.get('text','default');
  removepunct=request.GET.get('removepunct','off');
  capatilize=request.GET.get('capatilize','off');
  newlineremove=request.GET.get('newlineremove','off');
  extraspaceremove=request.GET.get('extraspaceremove','off');
  analyzed=""
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  if (removepunct=="on"):
     for char in djtext:
         if char not in punctuations:
             analyzed=analyzed+char;

     dict={"purpose":"Remove Punctuation","analyzed_text":analyzed}
     return render(request,'analyse.html',dict);
  elif(capatilize=="on"):
      for char in djtext:
               analyzed=analyzed+char.upper();
      dict={"purpose":"capitalize","analyzed_text":analyzed}
      return render(request,'analyse.html',dict);
  elif (newlineremove=="on"):
       for char in djtext:
              if char!="/n":
               analyzed=analyzed+char;
       dict={"purpose":"New Line Remove","analyzed_text":analyzed}
       return render(request,'analyse.html',dict)
  elif (extraspaceremove=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        dict = {'purpose': 'Extra Space', 'analyzed_text': analyzed}
        return render(request, 'analyse.html', dict)

  else:
      return HttpResponse("ERROR--404")
