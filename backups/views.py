from django.http import HttpResponse

def mostra_status(request):
  html = "<html><body>It is now.</body></html>"
  return HttpResponse(html)

