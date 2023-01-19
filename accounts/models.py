from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an e-mail address')
        
        if not username:
            raise ValueError('User must have an Username')

        user = self.model(
            email       = self.normalize_email(email),
            username    = username,
            first_name  = first_name,
            last_name   = last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            email      = self.normalize_email(email),
            username   = username,
            password   = password,
            first_name = first_name,
            last_name  = last_name
        )
        
        user.is_admin   = True
        user.is_active  = True
        user.is_staff   = True
        user.is_superadmin  = True
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=100, unique=True)
    phone_number    = models.CharField(max_length=50,null=True)

    #Required fields
    # image           = models.ImageField(upload_to='profile image',null=True)

    date_joined     = models.DateTimeField(auto_now_add=True)  
    last_login      = models.DateTimeField(auto_now_add=True)  

    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_recruiter    = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_superadmin   = models.BooleanField(default=False)
    my_points       = models.IntegerField(null=True,default=0)

    USERNAME_FIELD      = 'username'
    REQUIRED_FIELDS     = ['email', 'first_name', 'last_name']

    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class App(models.Model):
    creator=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    Appimagelink=models.CharField(max_length=500,null=True)
    Appname=models.CharField(max_length=500,null=True,)
    Applink=models.CharField(max_length=500,null=True)
    appcategory =models.CharField(max_length=500,null=True)
    subcategory =models.CharField(max_length=500,null=True)
    points=models.CharField(max_length=500,null=True)
    def __str__(self):
       return str(self.Appname)





class completedTask(models.Model):
    users=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    app=models.ForeignKey(App,on_delete=models.CASCADE,related_name="name_app",null=True)
    image=models.ImageField(upload_to="images",null=True)
    def __str__(self):
       return str(self.app)