from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
import random

# use a custom auth user model to add extra fields
# for both Employer and Employee
class User(AbstractUser):
    # override username and email(unique)
    username = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    
    # denotes whether the user is Employer
    is_employer = models.BooleanField(default=False)
    
    # denotes wether the user is Employee
    is_employee = models.BooleanField(default=False)
    
    # role of the user
    position = models.CharField(max_length=200, default=None, blank=True, null=True)
    
    # # phone number
    # phone_number = models.CharField(max_length=15, blank=False)
    
    # date of birth
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    
    # # national ID
    # national_id = models.CharField(max_length=15, default=None, blank=True, null=True)
    
    # KRA PIN
    # kra_pin = models.CharField(max_length=50, default=None, blank=True, null=True)
    
    # mandatory fields
    REQUIRED_FIELDS = ['username',]
    
    # require the email to be the unique identifier
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
        
        
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("hrms:dept_detail", kwargs={"pk": self.pk})
    


# profile model for fields specific to Employer
class Employer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    
    # company name
    company = models.CharField(max_length=200, default=None, blank=True, null=True)

    # Employer belongs to Department
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    
    # number of employees associated with the employer
    number_of_employees  = models.IntegerField(default=0, blank=True, null=True)
    
    def __str__(self):
        return self.user.email + ' for company ' + self.company





class Employee(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True
    )
    
    # employee 'belongs' to employer
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)


    # Employee Details
    STATUS_CHOICES = (('Provided', 'Provided'),('Submitted', 'Submitted'),)
    
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    current_ddress = models.TextField(max_length=100, default='')
    permanent_address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    document_status = models.CharField(max_length=55,choices=STATUS_CHOICES,null=True)
    bank = models.CharField(max_length=25, default='First Bank Plc')
    salary = models.CharField(max_length=16,default='00,000.00') 

    
    def __str__(self):
        return self.user.email


class Document(models.Model):
    GOV_ID = (('aadhar-card','AADHAR-CARD'),('voter-card','VOTER-CARD'),('pan-card','PAN-CARD'))
    emp_id = models.IntegerField(null=True)
    document_title = models.CharField(max_length=255,null=True)
    Gov_id_1 = models.CharField(choices=GOV_ID, max_length=10, default='aadharCard')
    Gov_id_2 = models.CharField(choices=GOV_ID, max_length=10, default='aadharCard')
    Gov_id_3 = models.CharField(choices=GOV_ID, max_length=10, default='aadharCard')
    note = models.TextField(null=True)
    # files = models.ImageField(upload_to='otherdocs/',null=True)


class BankDetails(models.Model):
    accou_hol_name = models.CharField(max_length=255,null=True)
    emp_id = models.IntegerField(null=True)
    accou_num = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    document = models.ImageField(upload_to='bankdoc/0',null=True)
    note = models.TextField(max_length=255,null=True)


class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField()
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def save(self,*args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance,self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)


class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start



class Asset(models.Model):
    asset = models.CharField(max_length=50, blank=False, primary_key=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=False)

# track which asset is owned by which employee
class AssignedAsset(models.Model):
    asset = models.OneToOneField(Asset, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)




# class Recruitment(models.Model):
#     first_name = models.CharField(max_length=25)
#     last_name= models.CharField(max_length=25)
#     position = models.CharField(max_length=15)
#     email = models.EmailField(max_length=25)
#     phone = models.CharField(max_length=11)

#     def __str__(self):
#         return self.first_name +' - '+self.position