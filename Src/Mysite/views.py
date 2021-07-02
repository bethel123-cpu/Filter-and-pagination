from django.shortcuts import render

from django.core.paginator import Paginator

# Create your views here.
from .models import patients
from .filters import patientsfilter


def show_all_patients_page(request):

    context = {}

    filtered_patients = patientsfilter(
        request.GET,
        queryset=patients.objects.all()

    )

    context['filtered_patients'] = filtered_patients

    paginated_filtered_patients = Paginator(filtered_patients.qs, 5)
    page_number = request.GET.get('page')
    patients_page_obj = paginated_filtered_patients.get_page(page_number)

    context['patients_page_obj'] = patients_page_obj

    return render(request, 'myapp/show_all_patients_page.html', context=context)
