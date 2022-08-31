from django.db import models

class Intern(models.Model):
    STATUS_ITEMS = [
        (0, 'Applied'),
        (1, 'Interview'),
        (2, 'WellDone'),
    ]
    company_name = models.CharField(max_length=128)
    job_title = models.CharField(max_length=128)

    # Intern.get_status_display function
    status = models.IntegerField(choices=STATUS_ITEMS)
    started_time = models.DateField()

    def __unicode__(self):
        return '<Internship: {}>'.format(self.company_name)
