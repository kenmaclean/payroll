import calendar
import datetime
import json

from .models import Archive_file

# These should be added to config or settings file so you can change them globally quick
# better as more categories are created this would make a good model
JOB_GROUP_A_PAY = 20.0 # paid 20$ an hour.
JOB_GROUP_B_PAY = 30.0 # paid 30$ an hour. 

def generateReportJSON(requested_file_id=-1):
    """
    Function is to long and could be shrunk with helper functions

    This function returns a JSON object (Report per specifications)

    Using -1 to get all records on request
    """
    employeeReports = [] # This will hold dictionaries with an employee id, pay period and amountpaid

    if requested_file_id > 0:
        record = Archive_file.objects.filter(file_id=requested_file_id)
    else:
        # so this is going to get increasingly dangerous as more and more pay periods and employees are created
        record = Archive_file.objects.all()
    
    
    for i in range(len(record)):
        
        temp_month = record[i].record_date.month
        temp_day = record[i].record_date.day
        temp_year = record[i].record_date.year

        # Figure out the start and end period that day will fit in
        # watch for leap years (handled by only checking start of month)
        # this should be made into a helper function
        if temp_day > 15:
            last_day_of_month = calendar.monthrange(temp_year, temp_month)[1]
            start_pay_period = 16
            end_pay_period = last_day_of_month
        else:
            start_pay_period = 1
            end_pay_period = 15
        
        # determine amount paid and add it to the pay period for that employee
        # this should be made into a helper function
        if record[i].job_group == 'A':
            rate = JOB_GROUP_A_PAY
        elif record[i].job_group == 'B':
            rate = JOB_GROUP_B_PAY
        else:
            pass
            #raise exceptions

        # add padding to the dates as per specifications requirements
        # this should be made into a helper function
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

    # Build the format required per specifications
    sorted_list = sorted(employeeReports, key=lambda k: (k['employeeId'], k['payPeriod']['startDate']))
    result = {"payrollReport": {"employeeReports": sorted_list}}
    result = json.dumps(result, indent=4)
    
    return result


def checkIfPreviouslyProcessed(file_id):

    recordProcessed = False
    record = Archive_file.objects.filter(file_id=file_id).first()

    if record:
        recordProcessed = True

    return recordProcessed
    



