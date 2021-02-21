import io
import csv

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from .models import Contact
from .forms import ContactForm


def index(request):
    last_entries = Contact.objects.order_by('first_name')[:5]
    response = ', ' .join([f.first_name for f in last_entries])

    return HttpResponse(response + ' you are in the contacts view')


def contact(request):
    template = 'contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    
    return render(request, template, context)


@permission_required('admin.can_add_log_entry')
def contact_upload(request):
    template = 'contact_upload.html'
    
    prompt = {
        'order': 'Order of the CSV should be first_name, last_name, email, message'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File must be a csv file')
    
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string) # skip the header

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, create = Contact.objects.update_or_create(
            first_name = column[0],
            last_name = column[1],
            email = column[2],
            message = column[3]
        )
    context = {}
    
    return render(request, template, context)
