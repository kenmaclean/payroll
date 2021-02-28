From Ken Maclean
1-403-892-8089
krmaclean@gmail.com


Original readme follows

Documentation:
[x] Please commit the following to this README.md:

[x] Instructions on how to build/run your application
Instructions:
1. I suggest you create a new virtual env (I like using virtualenvwrapper) I assume you have knowledge (I use Python version 3.9.1)
2. copy the repo.bundle file to inside your virtual environment directory
3. run "git clone repo.bundle repo" at terminal

3.5 run pip insatll -r requirements.txt

4. create a postgresql database called payroll
5. run python manage.py migrate (this will create the DB schema)
6. create a django super user "python manage.py createsuperuser (python3 manage.py createsuperuser)" with a user name and password
7. in the settings.py file you need to include your django secret key and database password. I will mark locations with <<<password>>> and <<<secretkey>>>
    The secretkey is generated on starting a new project. To be honest I am not sure the correct usage of this. I think you can use a secret key from another django project that you have created on your system
    https://docs.djangoproject.com/en/3.1/ref/settings/
    on second check the secret key may be okay if it remains blank
8. Run python manage.py runserver
9. navigate to http://127.0.0.1:8000/admin/
10. Log in
11. If you make it this far we are in good shape
12. Navigate to http://127.0.0.1:8000/uploadfile/
13. click choose file
14. navigate to payroll/data and select time-report-1.csv
15. click the upload file button
16. try this again and you should see a "File has already been processed." message.
17. navigate to http://127.0.0.1:8000/pay/
18. This should show you all records in the database consolidated so any unique employee id with unique pay period start and end dates are listed sorted by employee id and date
19. navigate to http://127.0.0.1:8000/pay/1/ to see the sample read me data (The 1 in this case is the file id or number that is in the filename)
20. to view your data via admin page navigate to http://127.0.0.1:8000/admin/pay/archive_file/
21. You can CRUD individual records this way if you desired. (This should be user auth protected in future)
22. You can test uploading the same file a second time and a non CSV file (functionality to test these are included.)
23. note a file with a valid  name but invalid contect data will crash the program this would be a future todo.
24. I think this covers the requirements. 
25. This was a really fun excersise and a good refreshed for me. I have not created a ground up django project for some time. 

Answers to the following questions:
1. How did you test that your implementation was correct?
  - Using the sample data in the readme, make sure you get a 100% match, also validate the json data is valid
  - test using the supplied test file (note date formats between readme and test csv file are different, I assume the file is correct)
  - test using new created test data files (found in payroll-->apps-->data)
  - test that the application works via browser (only chrome but I should have tested it with other browsers)
  - test all pages and use bad data to test the csv file error as requested.
  - I manually tested with sublime and google sheets what the outcomes should look like and math for small sample size (e.g. sample data provided)
  - I checked that the response returns valid JSON (using = https://jsonlint.com/)

2. If this application was destined for a production environment, what would you add or change?
    -Security needs to be 100% this is dealing with pay so highly sensitive data
    -User account security required and probably encryption
    -Document how to use the application for primary users
    -put in some safety catches for the "all records report" e.g. if there were many pay periods and users the end point could time out . Pagination could work or just return better reports based on year or specific users. 
    -Having only 2 pays A and B hard coded, this should be a proper model as they would likely be changed and or added to.
    -You could also add file records and metabata
    -Add logging to database
    -Add more and better error handling
    -Add alerts e.g. if bad data is suspected or found on ingest or processing send a slack or sms alert to the person responsible (proactively montitor for errors.)

3. What compromises did you have to make as a result of the time constraints of this challenge?
    -Code is rough and not clean. Could be more reable and formatted better. Not fully pep 8 compliant. 
    -I would add more unit tests.
    -I would handle more edge cases with better exception handling
    -Better documentation of the classe, functions, and files
    -Implement swagger
    -Poor security
    -Cleaner and more mature HTML. Maybe create a proper front end and not use django templates.
    -I did not fully utilize Git / github. I did create a personal repo and a branch but did not create a pull request and meger this to the main branch.


Submission Instructions
[x] Clone the repository.
[x] Complete your project as described above within your local repository.
[x] Ensure everything you want to commit is committed.
[x] Create a git bundle: git bundle create your_name.bundle --all
    [x] this is new to me but good way to test is use bundle on linux computer
[x] Email the bundle file to dev.careers@waveapps.com and CC the recruiter you have been in contact with.
    [x] email to yourself and proceed with Linux test



Task list From Ken Maclean

Below is from the specifications broken into a task list

Notes:
1. I did not use TDD. I Built small parts and tested as I went.
2. Unit test (just a single sample) were written after I had the basics written

From Specifications:
[x] 1. An endpoint for uploading a file.

[x] This file will conform to the CSV specifications outlined in the previous section.
    NOTE: the sample data in https://github.com/wvchallenges/se-challenge-payroll
    has a different date format then the example file.
    [x] Using the example file data as source of truth
    [FUTURE] support both date formats

[x] Upon upload, the timekeeping information within the file must be stored to a database for archival purposes.
    [x] accessible to vieww via admin
[x] If an attempt is made to upload a file with the same report ID as a previously uploaded file, this upload should fail with an error message indicating that this is not allowed.
    [x] Handled a few test cases crudely. There is room for improvement

[x] 2. An endpoint for retrieving a payroll report structured in the following way:

[x] NOTE: It is not the responsibility of the API to return HTML, as we will delegate the visual layout and redering to the front end. The expectation is that this API will only return JSON data.

[x] Return a JSON object payrollReport.
[x] payrollReport will have a single field, employeeReports, containing a list of objects with fields employeeId, payPeriod, and amountPaid.
    [x] matched example response as good as possible,
    [x] took some liberties as example was not valid json
        [x] e.g. keys/properties should be in double quotes and there should not be a ";" after the list
[x] The payPeriod field is an object containing a date interval that is roughly biweekly. Each month has two pay periods; the first half is from the 1st to the 15th inclusive, and the second half is from the 16th to the end of the month, inclusive. payPeriod will have two fields to represent this interval: startDate and endDate.
    [x] I matched the format and padding of the example response as best as possible.
    [x] e.g. in file we have this format "04/01/2020" or "9/11/2016", in example response it requests  "2020-01-01" so I conformed
[x] Each employee should have a single object in employeeReports for each pay period that they have recorded hours worked. The amountPaid field should contain the sum of the hours worked in that pay period multiplied by the hourly rate for their job group.
    [x] consolidated correctly
[x] If an employee was not paid in a specific pay period, there should not be an object in employeeReports for that employee + pay period combination.
[x] The report should be sorted in some sensical order (e.g. sorted by employee id and then pay period start.)
    [x] sorted by employee id the payperiod start date
[x] The report should be based on all of the data across all of the uploaded time reports, for all time.
    [x] I built to process a specific file id (for selfish testing reasons)
        http://127.0.0.1:8000/pay/1
    [x] will add an "all parameter"
        http://127.0.0.1:8000/pay/

[Arguable] Is easy to set up
    [x] postgresql can be tricky, you need PGADMIN 4, postgres, secret key, a database called payroll, and a password and django super user.
    [x] virtual env is always tricky, will omit from instructions
[x] Can run on either a Linux or Mac OS X developer machine
        [x] test this on Linux machine 
        [x] TEST with GIT BUNDLE on linux (emailed the bundle)
        [x] NOTE I developed this on windows. I'm impartial to OS. 
[x] Does not require any non open-source software

Evaluation of your submission will be based on the following criteria.


[To be filled by evaluator]
Did you follow the instructions for submission?
Did you complete the steps outlined in the Documentation section?
Were models/entities and other components easily identifiable to the reviewer?
What design decisions did you make when designing your models/entities? Are they explained?
Did you separate any concerns in your application? Why or why not?
Does your solution use appropriate data types for the problem as described?


************ Ken's todo list (work in progress)
[x] Make sure you remove user name and password from settings.py file for
[x] add a unit test to show concept
    [x] to run "python manage.py test payroll.apps.pay"
    [TODO] Should have a lot more unit tests, add
[TODO] clean up the code, condense
[TODO] comment code better
[TODO] create a helper file with generic functions available to all payroll apps
[FUTURE] add swagger for admin page. 
[x] check that response returns valid JSON (using = https://jsonlint.com/)
[x] Get postgres DB set up on new django app
[x] clone git repo, make local git project
[x] Create personal Git repo to store project
    [x] https://github.com/kenmaclean/payroll
    [x] init, add, commit, push (make 2 branches main and develop)
[x] Create models to store file data
[x] Create some views / end points 
[x] Set up a basic admin page to test view data
[x] Build file ingest part of the project
	[x] small basic html
	[x] test upload
[x] Create a controller to read uploaded data from DB to begin file data processing into proper JSON respons
[x] test the json
[x] check the date formats in the output make sure you have leading zeros for month and day when value < 10
[x] Make sure the list of dictionaries is sorted by employee ID and start date
[x] check that the ordering of the output is correct ()
[TODO] Handle the alternate date format (file vs readme)
[x] HIDE THE DATABASE PASSORD
[x] Document instructions
[x] Test on linux machine
[x] Test git bundle on linux machine
[TODO] Use proper HTML for file upload template
    [TODO] this is week could use a lot of worked
[TODO] add a splash of CSS to file upload template to make it look less terrible
[TODO] Submit assignment with all instructions complete (see read me)
[x] pip freeze and pipe into requirement file
    add this to install instructions
    also mention upgrade pip
    using python version 3.9.1
[TODO] clean up pep 8 violations, conform to snake case, 
[TODO] file level doc strings
[TODO] class / function level docstrings add or improve


***********************************************************
***********************************************************
Original read me file below
***********************************************************
# Wave Software Development Challenge

Applicants for the Full-stack Developer role at Wave must
complete the following challenge, and submit a solution prior to the onsite
interview.

The purpose of this exercise is to create something that we can work on
together during the onsite. We do this so that you get a chance to collaborate
with Wavers during the interview in a situation where you know something better
than us (it's your code, after all!)

There isn't a hard deadline for this exercise; take as long as you need to
complete it. However, in terms of total time spent actively working on the
challenge, we ask that you not spend more than a few hours, as we value your
time and are happy to leave things open to discussion in the on-site interview.

Please use whatever programming language and framework you feel the most
comfortable with.

Feel free to email [dev.careers@waveapps.com](dev.careers@waveapps.com) if you
have any questions.

## Project Description

Imagine that this is the early days of Wave's history, and that we are prototyping a new payroll system API. A front end (that hasn't been developed yet, but will likely be a single page application) is going to use our API to achieve two goals:

1. Upload a CSV file containing data on the number of hours worked per day per employee
1. Retrieve a report detailing how much each employee should be paid in each _pay period_

All employees are paid by the hour (there are no salaried employees.) Employees belong to one of two _job groups_ which determine their wages; job group A is paid $20/hr, and job group B is paid $30/hr. Each employee is identified by a string called an "employee id" that is globally unique in our system.

Hours are tracked per employee, per day in comma-separated value files (CSV).
Each individual CSV file is known as a "time report", and will contain:

1. A header, denoting the columns in the sheet (`date`, `hours worked`,
   `employee id`, `job group`)
1. 0 or more data rows

In addition, the file name should be of the format `time-report-x.csv`,
where `x` is the ID of the time report represented as an integer. For example, `time-report-42.csv` would represent a report with an ID of `42`.

You can assume that:

1. Columns will always be in that order.
1. There will always be data in each column and the number of hours worked will always be greater than 0.
1. There will always be a well-formed header line.
1. There will always be a well-formed file name.

A sample input file named `time-report-42.csv` is included in this repo.

### What your API must do:

We've agreed to build an API with the following endpoints to serve HTTP requests:

1. An endpoint for uploading a file.

   - This file will conform to the CSV specifications outlined in the previous section.
   - Upon upload, the timekeeping information within the file must be stored to a database for archival purposes.
   - If an attempt is made to upload a file with the same report ID as a previously uploaded file, this upload should fail with an error message indicating that this is not allowed.

1. An endpoint for retrieving a payroll report structured in the following way:

   _NOTE:_ It is not the responsibility of the API to return HTML, as we will delegate the visual layout and redering to the front end. The expectation is that this API will only return JSON data.

   - Return a JSON object `payrollReport`.
   - `payrollReport` will have a single field, `employeeReports`, containing a list of objects with fields `employeeId`, `payPeriod`, and `amountPaid`.
   - The `payPeriod` field is an object containing a date interval that is roughly biweekly. Each month has two pay periods; the _first half_ is from the 1st to the 15th inclusive, and the _second half_ is from the 16th to the end of the month, inclusive. `payPeriod` will have two fields to represent this interval: `startDate` and `endDate`.
   - Each employee should have a single object in `employeeReports` for each pay period that they have recorded hours worked. The `amountPaid` field should contain the sum of the hours worked in that pay period multiplied by the hourly rate for their job group.
   - If an employee was not paid in a specific pay period, there should not be an object in `employeeReports` for that employee + pay period combination.
   - The report should be sorted in some sensical order (e.g. sorted by employee id and then pay period start.)
   - The report should be based on all _of the data_ across _all of the uploaded time reports_, for all time.

   As an example, given the upload of a sample file with the following data:

    <table>
    <tr>
      <th>
        date
      </th>
      <th>
        hours worked
      </th>
      <th>
        employee id
      </th>
      <th>
        job group
      </th>
    </tr>
    <tr>
      <td>
        2020-01-04
      </td>
      <td>
        10
      </td>
      <td>
        1
      </td>
      <td>
        A
      </td>
    </tr>
    <tr>
      <td>
        2020-01-14
      </td>
      <td>
        5
      </td>
      <td>
        1
      </td>
      <td>
        A
      </td>
    </tr>
    <tr>
      <td>
        2020-01-20
      </td>
      <td>
        3
      </td>
      <td>
        2
      </td>
      <td>
        B
      </td>
    </tr>
    <tr>
      <td>
        2020-01-20
      </td>
      <td>
        4
      </td>
      <td>
        1
      </td>
      <td>
        A
      </td>
    </tr>
    </table>

   A request to the report endpoint should return the following JSON response:

   ```javascript
   {
     payrollReport: {
       employeeReports: [
         {
           employeeId: 1,
           payPeriod: {
             startDate: "2020-01-01",
             endDate: "2020-01-15"
           },
           amountPaid: "$300.00"
         },
         {
           employeeId: 1,
           payPeriod: {
             startDate: "2020-01-16",
             endDate: "2020-01-31"
           },
           amountPaid: "$80.00"
         },
         {
           employeeId: 2,
           payPeriod: {
             startDate: "2020-01-16",
             endDate: "2020-01-31"
           },
           amountPaid: "$90.00"
         }
       ];
     }
   }
   ```

We consider ourselves to be language agnostic here at Wave, so feel free to use any combination of technologies you see fit to both meet the requirements and showcase your skills. We only ask that your submission:

- Is easy to set up
- Can run on either a Linux or Mac OS X developer machine
- Does not require any non open-source software

### Documentation:

Please commit the following to this `README.md`:

1. Instructions on how to build/run your application
1. Answers to the following questions:
   - How did you test that your implementation was correct?
   - If this application was destined for a production environment, what would you add or change?
   - What compromises did you have to make as a result of the time constraints of this challenge?

## Submission Instructions

1. Clone the repository.
1. Complete your project as described above within your local repository.
1. Ensure everything you want to commit is committed.
1. Create a git bundle: `git bundle create your_name.bundle --all`
1. Email the bundle file to [dev.careers@waveapps.com](dev.careers@waveapps.com) and CC the recruiter you have been in contact with.

## Evaluation

Evaluation of your submission will be based on the following criteria.

1. Did you follow the instructions for submission?
1. Did you complete the steps outlined in the _Documentation_ section?
1. Were models/entities and other components easily identifiable to the
   reviewer?
1. What design decisions did you make when designing your models/entities? Are
   they explained?
1. Did you separate any concerns in your application? Why or why not?
1. Does your solution use appropriate data types for the problem as described?
