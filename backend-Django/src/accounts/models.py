

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.utils.translation import gettext as _


class CustomManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        ## create a user instance 
        user_obj = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )

        user_obj.set_password(password)
       
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "Admin")
        return self._create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    '''
    user class for authetication purpose
    '''

    ##### FIELDS SECTION #####
    ##########################

    Role_choices = (
        ('Admin', 'Admin'),
        ('Doctor', 'Doctor'),
        ('Employee', 'Employee'),
        ('Patient', 'Patient'),
    )
    role = models.CharField(_('Role'), max_length=10, choices=Role_choices)

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[UnicodeUsernameValidator],
        error_messages={
            'unique': _("A user with that username already exists."),
        }
    )

    email = models.EmailField(
        _('email address'),
        unique=True, 
        error_messages={
        'unique': ('A user with that email already exists.'),
        }
    )

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    timestamp = models.DateTimeField(_("timestamp"), auto_now_add=True)


    ##### OTHERS PARAMATERS #####
    #############################

    objects = CustomManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    ##### METHODS AND PROPERTIES #####
    ##################################

    def __str__(self):
        return self.username


class Profile(models.Model):
    '''
    profile is an interface for all users in the system.
    '''

    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    gender = models.CharField(_('gender'), choices=gender_choices,max_length=20, default="Male")
    date_of_birth = models.DateField(_('date of birth'), blank=True, null=True)

    phone = PhoneNumberField(_("phone number"), blank=True, null=True, max_length=27)
    profile_picture = models.ImageField(upload_to='profile_pics',blank=True, null=True)
    address = models.CharField(_('address'), max_length=100, blank=True, null=True)


    class Meta:
        abstract = True


class StaffProfile(Profile):
    '''
    staffProfile is an interface for all type of employees (admin, doctor, employee) in the system.
    '''

    class Meta:
        abstract = True



class Admin(StaffProfile):
    pass

    def __str__(self):
        return self.username
    


class Employee(StaffProfile):
    pass

class Doctor(StaffProfile):
    pass


class Patient(Profile):
    marital_status_choices = (
        ('Married', 'Married'),
        ('Widowed', 'Widowed'),
        ('Separated', 'Separated'),
        ('Divorced', 'Divorced'),
        ('Single', 'Single'),
    )
    marital_status = models.CharField(
        _('marital status'), 
        choices=marital_status_choices, 
        max_length=20, 
        default="Single"
    )


    
    

