import io
import csv
import json
import datetime

from datetime import date
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, Http404

from .models import Archive_file
from .controller import generateReportJSON, checkIfPreviouslyProcessed

def all(request):
    
    response = generateReportJSON(-1)
    
    return HttpResponse(response, content_type="application/json")


def detail(request, file_id):
    
    if int(file_id) < 1:
        file_id = -1
    
    response = generateReportJSON(file_id)
    
    return HttpResponse(response, content_type="application/json")
    

def results(request, file_id):
    response = f'The file resultsd id = {file_id}'

    return HttpResponse(response)


@permission_required('admin.can_add_log_entry')
def pay_upload(request):
    """
    A lot of this should be moved to controller
    [TODO] Break this into cleaner code
    """
    template = 'pay_upload.html'
    
    prompt = {
        'order': 'Order of the CSV should be date, hours worked, employee id, job group'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    # time-report-42.csv.... we want 42., extract the file id from file name
    # so much can go wrong with the file name that I took a genral try / catch. This could be improved
    try:
        csv_file_name = csv_file.name
        fn = csv_file_name.split('-')
        fn2 = fn[2].split('.')
        file_id = fn2[0]
    
        # check if the file has already been processed
        check = checkIfPreviouslyProcessed(file_id)

        # return error if file has already been processed    
        if check == True:
            messages.error(request, 'File has already been processed.')
            
        # return error if file is not a csv 
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File must be a csv file')
        
        data_set = csv_file.read().decode('UTF-8')

        io_string = io.StringIO(data_set)
        next(io_string) # skip the header

        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            record_date = datetime.datetime.strptime(column[0], "%d/%m/%Y").strftime("%Y-%m-%d")
            
            _, create = Archive_file.objects.update_or_create(
                file_name = csv_file_name,
                file_id = file_id,
                record_date = record_date,
                hours_worked = column[1],
                employee_id = column[2],
                job_group = column[3]
            )
    except:
        messages.error(request, 'Something went wrong with the file! File must be a csv file in this format time-report-42.csv.')
    
    return render(request, template, prompt)
