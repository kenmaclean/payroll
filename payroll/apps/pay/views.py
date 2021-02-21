import io
import csv
import datetime

from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

from .models import Archive_file


def index(request):
    last_entries = Archive_file.objects.order_by('file_name')[:5]
    response = ', ' .join([f.file_name for f in last_entries])
    return HttpResponse(response)

def detail(request, file_id):
    response = f'The file id = {file_id}'
    return HttpResponse(response)

def results(request, file_id):
    response = f'The file resultsd id = {file_id}'
    return HttpResponse(response)

def employee(request, employee_id):
    response = f'The employee id = {employee_id}'
    return HttpResponse(response)


@permission_required('admin.can_add_log_entry')
def pay_upload(request):
    template = 'pay_upload.html'
    
    prompt = {
        'order': 'Order of the CSV should be date, hours worked, employee id, job group'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    csv_file_name = csv_file.name
    print(f'file name = {csv_file_name}')
    fn = csv_file_name.split('-')
    print(f'file name split = {csv_file_name}')
    fn2 = fn[2].split('.')
    file_id = fn2[0]
    print(f'file number = {file_id}')

    # once you have the file name as string extract the file id from it, file name should be this format 
    # time-report-42.csv.... we want 42.

    # need to handle date format in file as well
    
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'File must be a csv file')
    
    data_set = csv_file.read().decode('UTF-8')

    io_string = io.StringIO(data_set)
    next(io_string) # skip the header
    i = 0

    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        record_date = datetime.datetime.strptime(column[0], "%d/%m/%Y").strftime("%Y-%m-%d")
        print(f'{csv_file_name} {file_id} {record_date} {column[1]} {column[2]} {column[3]}')
        
        _, create = Archive_file.objects.update_or_create(
            file_name = csv_file_name,
            file_id = file_id,
            record_date = record_date,
            hours_worked = column[1],
            employee_id = column[2],
            job_group = column[3]
        )
    context = {} # get rid of this later
    
    return render(request, template, context)
