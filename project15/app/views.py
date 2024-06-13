from django.shortcuts import render
from .forms import*
from django.http import HttpResponse
from django.views.generic import FormView
# Create your views here.


def  school_form_byfbv(request):
    ESFO = SchoolForms()
    d={'ESFO':ESFO}
    if request.method == 'POST':
        SFDO = SchoolForms(request.POST)
        if SFDO.is_valid:
            SFDO.save()
            return HttpResponse('school_form_byfbv is Done')
        return HttpResponse('invalid data')
    return render(request ,'school_form_byfbv.html',d)


class  school_form_bycbv(FormView):
    template_name = 'school_form_bycbv.html'  # in this block is written because to send the data to the frontend
    form_class = SchoolForms

    def form_valid(self, form):
        form.save()                          # this is use to save the data  of user
        return HttpResponse('school_form_bycbv is done')