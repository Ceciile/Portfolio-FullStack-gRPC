from django.db import models

class Intern(models.Model):
    STATUS_ITEMS = [
        (0, 'Applied'),
        (1, 'Interview'),
        (2, 'WellDone'),
    ]
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=128)

    # Intern.get_status_display function
    status = models.IntegerField(choices=STATUS_ITEMS,default=0)
    started_time = models.DateField()
    postal = models.CharField(max_length=128,default=0)

    def __unicode__(self):
        return '<Internship: {}>'.format(self.company_name)



# Model.Manager
class FrontManager(models.Manager):
    def get_query_set(self):
        return super(FrontManager,self).get_queryset().filter(tech='UI')

class BackManager(models.Manager):
    def get_query_set(self):
        return super(BackManager,self).get_queryset().filter(tech='Server')

class SchoolProject(models.Model):
    subject = models.CharField(max_length=128)
    end_time = models.DateField()
    group_nb = models.IntegerField(default=1,blank=True)
    tech = models.CharField(max_length=6,choices=(('UI','Front'),('Server','Back'),('Full','Full')))
    project = models.Manager()
    front = FrontManager()
    back = BackManager()

    def __unicode__(self):
        return self.subject
        