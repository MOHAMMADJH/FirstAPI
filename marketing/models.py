from django.db import models

from customer.models import Customer
# Create your models here.
from hr.models import Employee
class ContractType(models.Model):
    type = models.CharField(max_length=200)
    def __str__(self):
        return self.type

class ProjectComponent(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class ComponentPart(models.Model):
    project = models.ForeignKey(ProjectComponent , on_delete=models.CASCADE)
    partName  = models.CharField(max_length=200)
    def __str__(self):
        return self.partName
class ComponentPartItem(models.Model):
    componentPart = models.ForeignKey(ComponentPart, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200)

    def __str__(self):
        return self.itemName




class WorkingScope(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title
class WorkingPart(models.Model):
    project = models.ForeignKey(WorkingScope , on_delete=models.CASCADE)
    partName  = models.CharField(max_length=200)
    def __str__(self):
        return self.partName
class WorkingPartItem(models.Model):
    workingPart = models.ForeignKey(WorkingPart, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200)

    def __str__(self):
        return self.itemName


class Contract(models.Model):
    contractType = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    projectName = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    statement = models.TextField()
    priceInNumber = models.FloatField()
    totalArea = models.IntegerField()
    totalTimePeriod = models.IntegerField()
    GregorianDate = models.DateTimeField(auto_now_add=True)
    contractSubject = models.TextField()
    #projectComponents = models.ForeignKey(ProjectComponent, on_delete=models.CASCADE)
    #workingScope = models.ForeignKey(WorkingScope, on_delete=models.CASCADE)
    additionalDetails = models.TextField()
    MunicipalConfirmed = models.BooleanField()

    def __str__(self):
        return self.projectName



class MeetingType(models.Model):
    type = models.CharField(max_length=30)
    def __str__(self):
        return self.type
class MarketingMeeting(models.Model):
    CHOICES  = [('C ' , 'Canceled'),
                ('D', 'Done'),
                ('P' , 'Pending'),
                ('S' , 'Shifted')]

    dateTime = models.DateTimeField()
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    type = models.ForeignKey(MeetingType , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    notes = models.TextField()
    status = models.CharField(choices=CHOICES , max_length=40)
    def __str__(self):
        return self.subject + " " + self.customer.__str__()


