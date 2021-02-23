# Need to process 
# employees paid by the hour
# Group A is 20$ an hour
# Group B is 30$ an hour


# handle validation later



"""
[Complete] An endpoint for uploading a file.

[Complete] This file will conform to the CSV specifications outlined in the previous section.
[Complete] Upon upload, the timekeeping information within the file must be stored to a database for archival purposes.
[TODO] If an attempt is made to upload a file with the same report ID as a previously uploaded file, this upload should fail with an error message indicating that this is not allowed.



"""


#from django.db import models
import calendar
import datetime

from .models import Archive_file

JOB_GROUP_A_PAY = 20.0 # paid 20$ an hour. Could move this to settings.py
JOB_GROUP_B_PAY = 30.0 # paid 30$ an hour. 

def doSomething(requested_file_id):
    #test = Archive_file.objects.all()
    #print(f'{test[0]}')
    
    
    employeeReports = [] # This will hold dictionaries with an employee id, pay period and amountpaid

    next = Archive_file.objects.filter(file_id=requested_file_id)
    
    for i in range(len(next)):
        #print(f'{next[i].file_name}, {next[i].file_id}, {next[i].record_date}, {next[i].hours_worked}, {next[i].employee_id}, {next[i].job_group}')
        
        temp_month = next[i].record_date.month
        temp_day = next[i].record_date.day
        temp_year = next[i].record_date.year

        if temp_day > 15:
            last_day_of_month = calendar.monthrange(temp_year, temp_month)[1]
            start_pay_period = 16
            end_pay_period = last_day_of_month
        else:
            start_pay_period = 1
            end_pay_period = 15
        
        # determine amount paid and add it to the pay period for that employee
        if next[i].job_group == 'A':
            rate = JOB_GROUP_A_PAY
        elif next[i].job_group == 'B':
            rate = JOB_GROUP_B_PAY
        else:
            pass
            #raise exceptions

        amount_paid = next[i].hours_worked * rate
                
        payroll_dict_element = {
            "employeeId": next[i].employee_id,
            "payPeriod": {
                "startDate": start_pay_period,
                "endDate": end_pay_period,
            },
            "amountPaid": amount_paid,
        }
        print(f'{payroll_dict_element}')

        #now we need to check if a dictionary with employee id and start and end date exists in list, if not create, if so ammend 
        if not any(payroll_dict_element['employeeId'] == next[i].employee_id and payroll_dict_element['payPeriod'].startDate == start_pay_period for payroll_dict_element in employeeReports):
            # append the entry to the list
            employeeReports.append(dict(payroll_dict_element))
        else:
            pass


    print(f'here ====== {employeeReports}')
    return 'wicked'

    # payroll_dict_list = { 
    #     "employeeReports": [],
    # }

   

    #create a list of dictionaries, then add employeeReports: with list to payroll_dict_list
    # json.dumps

    # determine start and end date and which period it is in
    # get next[i].record_date
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


      if not any(payroll_dict_element['employeeId'] == next[i].employee_id for payroll_dict_element in employeeReports):
            # append the entry to the list
            employeeReports.append(dict(payroll_dict_element))
        else:
"""
# create a dictionary
# check if employee id is in it


    



