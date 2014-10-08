from django.shortcuts import render
from django.http import HttpResponse
import pilot_detail_view
import statprof
# Create your views here.
from analizer.pilots_view import list_pilots

def index(request):
    return render(request,"analizer/index.html",{"error_message1":"",
                                                 }) 
    return HttpResponse("you in index")
def corp_detail(request,corp_id):
    return render(request,"analizer/index.html",{"error_message":
                                                     "Unsupported: ",
                                                     })
def pilot_detail(request,pilot_id):
    return pilot_detail_view.pilot_detail(request,pilot_id)
    statprof.start()
    try:
        return pilot_detail_view.pilot_detail(request,pilot_id)
    finally:
        statprof.stop()
        statprof.display()
    return pilot_detail_view.pilot_detail(request,pilot_id)
    return render(request,"analizer/index.html",{"error_message":
                                                     "Unsupported: ",
                                                     })
def list_names(request):
    send_button=request.POST["send_button"]
    if send_button=="pilots":
        return list_pilots(request)
        return HttpResponse(" Yon in pilots list stub")
    else:
        return render(request,"analizer/index.html",{"error_message":
                                                     "Unsupported: "+send_button,
                                                     })
    return HttpResponse("you in list "+send_button)