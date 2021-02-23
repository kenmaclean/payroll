from django.db import models


class Archive_file(models.Model):
  file_name = models.CharField(max_length=100, null=False, blank=False) # is max lenght required? To short? 
  file_id = models.IntegerField(null=False, blank=False)
  record_date = models.DateTimeField('date of time recorded')
  hours_worked = models.FloatField(null=False) # DecimalField is over precise and not required for half or quarter hours
  employee_id = models.IntegerField(null=False, blank=False) # could use SmallIntegerField for < ~32k employees
  job_group = models.CharField(max_length=1, null=False, blank=False) # in validation check that this is A or B or log error


  def __str__(self):
    return f'{self.file_name}\n {self.file_id}\n {self.record_date}\n {self.hours_worked}\n {self.employee_id}\n {self.job_group}'
