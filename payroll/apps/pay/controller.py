#from django.db import models
import calendar
import datetime
import json

from .models import Archive_file

JOB_GROUP_A_PAY = 20.0 # paid 20$ an hour. Could move this to settings.py
JOB_GROUP_B_PAY = 30.0 # paid 30$ an hour. 

def generateReportJSON(requested_file_id):
    
    employeeReports = [] # This will hold dictionaries with an employee id, pay period and amountpaid

    record = Archive_file.objects.filter(file_id=requested_file_id)
    
    for i in range(len(record)):
        print(f'\nIn The loop === {record[i].file_name}, {record[i].file_id}, {record[i].record_date}, {record[i].hours_worked}, {record[i].employee_id}, {record[i].job_group}\n')
        
        temp_month = record[i].record_date.month
        temp_day = record[i].record_date.day
        temp_year = record[i].record_date.year

        if temp_day > 15:
            last_day_of_month = calendar.monthrange(temp_year, temp_month)[1]
            start_pay_period = 16
            end_pay_period = last_day_of_month
        else:
            start_pay_period = 1
            end_pay_period = 15
        
        # determine amount paid and add it to the pay period for that employee
        if record[i].job_group == 'A':
            rate = JOB_GROUP_A_PAY
        elif record[i].job_group == 'B':
            rate = JOB_GROUP_B_PAY
        else:
            pass
            #raise exceptions

        # startDate: "2020-01-01",
        # endDate: "2020-01-15"
        if temp_month < 10:
            str_temp_month = '0' + str(temp_month)
        else:
            str_temp_month = str(temp_month)

        if end_pay_period < 10:
            str_temp_day_end = '0' + str(end_pay_period)
        else:
            str_temp_day_end = str(end_pay_period)
        
        if start_pay_period < 10:
            str_temp_day_start = '0' + str(start_pay_period)
        else:
            str_temp_day_start = str(start_pay_period)
            
        start_Date = str(temp_year) + '-' + str(str_temp_month) + '-' + str(str_temp_day_start)
        end_Date = str(temp_year) + '-' + str(str_temp_month) + '-' + str(str_temp_day_end)

        amount_paid = record[i].hours_worked * rate
                
        payroll_dict_element = {
            "employeeId": record[i].employee_id,
            "payPeriod": {
                "startDate": start_Date,
                "endDate": end_Date,
            },
            "amountPaid": amount_paid,
        }
        #print(f'the single element {payroll_dict_element}\n\n')


        print('------------------------')
        #print(f'lenght of payroll_dict_element = {len(payroll_dict_element)}')
        x = payroll_dict_element['employeeId']
        y = payroll_dict_element['payPeriod']['startDate']
        z = payroll_dict_element['payPeriod']['endDate']
        print(f'payroll_dict_element employeeId = {x}')
        print(f'payroll_dict_element payPeriod start = {y}')
        print(f'payroll_dict_element payPeriod end = {z}')
        print(f'start_pay_period = {start_pay_period}')
        print(f'end_pay_period = {end_pay_period}')
        print('------------------------')
        
        # check to see if a record existing inside the list of dictionaries, if not create one.
        if not any(payroll_dict_element['employeeId'] == record[i].employee_id 
                and payroll_dict_element['payPeriod']['startDate'] == start_Date
                and payroll_dict_element['payPeriod']['endDate'] == end_Date
                for payroll_dict_element in employeeReports):

            # Add the dictionary to the list
            employeeReports.append(dict(payroll_dict_element))
        else:
            # find the index of the dictionary that exists in the list
            for index, d in enumerate(employeeReports):
                if d['employeeId'] == record[i].employee_id and d['payPeriod']['startDate'] == start_Date and d['payPeriod']['endDate'] == end_Date:
                    # once found, update the existing dictionary entries amount paid
                    employeeReports[index]['amountPaid'] += amount_paid

    #print(f'before sort == {employeeReports}')

    #from operator import itemgetter

   # new_list = sorted(employeeReports, key=itemgetter('employeeId', 'payPeriod'))
    new_list = sorted(employeeReports, key=lambda k: (k['employeeId'], k['payPeriod']['startDate']))

    #print(f'After sort == {new_list}')

   
    result = {"payrollReport": {"employeeReports": new_list}}


    #result[payrollReport] = employeeReports
    #print(f'{result}')

    #return HttpResponse(json.dumps(response, sort_keys=True, indent=4), content_type="application/json")
    result = json.dumps(result, indent=4)

    print(f'{result}')
    
    return result

    # payroll_dict_list = { 
    #     "employeeReports": [],
    # }

   

    #create a list of dictionaries, then add employeeReports: with list to payroll_dict_list
    # json.dumps

    # determine start and end date and which period it is in
    # get record[i].record_date
    # extract the day the month and year
    # if day < 16
    # pay period start 1 == yyyy-mm-01
    # pay period end == yyyy-mm-15
    
    #print(last_day_of_month)    # Output = 31
    # record_date = datetime.datetime.strptime(column[0], "%d/%m/%Y").strftime("%Y-%m-%d")
    #x = datetime.datetime.strptime('23/11/2016', "%d/%m/%Y")
    #x.month
    # x.day
    #last_day_of_month = calendar.monthrange(2019,8)[1]

    # Get Start Date



    

    # get the first row of data (employee record)
    # check if there is an entry for that employee in that time period
    # unique on Start date, end date, employee id
    # if not create one
    # if so, modify the existing entry

"""
 {
        employeeId: 1,
        payPeriod: {
          startDate: "2020-01-01",
          endDate: "2020-01-15"
        },
        amountPaid: "$300.00"
      },


      if not any(payroll_dict_element['employeeId'] == record[i].employee_id for payroll_dict_element in employeeReports):
            # append the entry to the list
            employeeReports.append(dict(payroll_dict_element))
        else:
"""
# create a dictionary
# check if employee id is in it


    



