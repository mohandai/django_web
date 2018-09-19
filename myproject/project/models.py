from django.db import models

# Create your models here.

gender = (
    ('male','male'),
    ('female','female'),
)

evaluation = (
    ('Weak','Weak'),
    ('Normal','Normal'),
    ('Strong','Strong'),
)

class User(models.Model):

    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32,choices=gender, default='male')
    #email = models.EmailField(unique=True, default='123@123.com')
    c_time = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.username

class IMS (models.Model):

    age_group = models.IntegerField(default=0)
    sex = models.CharField(max_length=32,choices=gender, default='male')

    gs_mean = models.IntegerField(default=0)
    apfs_mean = models.IntegerField(default=0)
    ads_mean = models.IntegerField(default=0)
    kfs_mean = models.IntegerField(default=0)
    kes_mean = models.IntegerField(default=0)
    has_mean = models.IntegerField(default=0)
    hers_mean = models.IntegerField(default=0)
    hirs_mean = models.IntegerField(default=0)
    efs_mean = models.IntegerField(default=0)
    ees_mean = models.IntegerField(default=0)
    sers_mean = models.IntegerField(default=0)
    sirs_mean = models.IntegerField(default=0)

    gs_sd = models.IntegerField(default=0)
    apfs_sd = models.IntegerField(default=0)
    ads_sd = models.IntegerField(default=0)
    kfs_sd = models.IntegerField(default=0)
    kes_sd = models.IntegerField(default=0)
    has_sd = models.IntegerField(default=0)
    hers_sd = models.IntegerField(default=0)
    hirs_sd = models.IntegerField(default=0)
    efs_sd = models.IntegerField(default=0)
    ees_sd = models.IntegerField(default=0)
    sers_sd = models.IntegerField(default=0)
    sirs_sd = models.IntegerField(default=0)

    def __str__(self):
        return str(self.age_group)+' '+str(self.sex)

class History_IMS (models.Model):
    userid = models.IntegerField(default=0)

    sex = models.CharField(max_length=32,choices=gender, default='male')
    age = models.IntegerField(default=0)

    gs = models.IntegerField(default=0)
    apfs = models.IntegerField(default=0)
    ads = models.IntegerField(default=0)
    kfs = models.IntegerField(default=0)
    kes = models.IntegerField(default=0)
    has = models.IntegerField(default=0)
    hers = models.IntegerField(default=0)
    hirs = models.IntegerField(default=0)
    efs = models.IntegerField(default=0)
    ees = models.IntegerField(default=0)
    sers = models.IntegerField(default=0)
    sirs = models.IntegerField(default=0)

    gs_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    apfs_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    ads_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    kfs_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    kes_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    has_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    hers_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    hirs_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    efs_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    ees_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    sers_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')
    sirs_eval = models.CharField(max_length=32,choices=evaluation, default='Weak')

    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.c_time)