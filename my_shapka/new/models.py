from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = User.objects.all().filter(['email'])
    OPERATOR = 'Operator'
    SUPERVISOR = 'Supervisor'
    ROLE = ((OPERATOR, 'Operator'),
            (SUPERVISOR, 'Supervisor'),)
    role = models.CharField(max_length=20, choices=ROLE, default=SUPERVISOR)
    department = models.CharField(max_length=50, default='null')

    phone = models.IntegerField(default=0)
    tg_user = models.CharField(max_length=30, default='null')
    password = models.CharField(max_length=50, default='null')
    date_last_update = models.DateTimeField()
    avatar = models.ImageField(upload_to='uploads')
    operator_id = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.first_name}'


users = User.objects.filter(email='anna.nekrasova@chat2desk.com')
print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
print(users)


class Equipment(models.Model):
    session = models.CharField(max_length=20)

    BS = 'BS'
    CLICKER = 'Clicker'
    TYPE = ((BS, 'BS'),
            (CLICKER, 'Clicker'),)

    type = models.CharField(max_length=20, choices=TYPE, default=CLICKER)

    FREE = 'Free'
    BUSY = 'Busy'
    STATUS = ((FREE, 'Free'),
              (BUSY, 'Busy'),)

    status = models.CharField(max_length=20, choices=STATUS, default=BUSY)


class Ru(models.Model):
    device_id = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)

    VIBER = 'Viber'
    WHATSAPP = 'Whatsapp'
    MESSENGER = ((VIBER, 'Viber'),
                 (WHATSAPP, 'Whatsapp'),)

    transport = models.CharField(max_length=20, choices=MESSENGER, default=WHATSAPP)

    key = models.CharField(max_length=10)

    WE = 'We'
    CLIENT = 'Client'
    OWNER = ((WE, 'We'),
             (CLIENT, 'Client'),)

    device_owner = models.CharField(max_length=20, choices=OWNER, default=CLIENT)

    ONLINE = 'Online'
    OFFLINE = 'Offline'
    LOST_REGISTRATION = 'Lost_registration'
    STATUS = ((ONLINE, 'Online'),
              (OFFLINE, 'Offline'),
              (LOST_REGISTRATION, 'Lost_registration'))

    stable_status = models.CharField(max_length=20, choices=STATUS, default=ONLINE)

    email = models.CharField(max_length=50)

    company_id = models.IntegerField(default=1)

    equipment_code = models.CharField(max_length=20, default='client')

    partner_id = models.IntegerField(default=1)

    status_datetime = models.DateTimeField()


class Euro(models.Model):
    device_id = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)

    VIBER = 'Viber'
    WHATSAPP = 'Whatsapp'
    MESSENGER = ((VIBER, 'Viber'),
                 (WHATSAPP, 'Whatsapp'),)

    transport = models.CharField(max_length=20, choices=MESSENGER, default=WHATSAPP)

    key = models.CharField(max_length=10)

    WE = 'We'
    CLIENT = 'Client'
    OWNER = ((WE, 'We'),
             (CLIENT, 'Client'),)

    device_owner = models.CharField(max_length=20, choices=OWNER, default=CLIENT)

    ONLINE = 'Online'
    OFFLINE = 'Offline'
    LOST_REGISTRATION = 'Lost_registration'
    STATUS = ((ONLINE, 'Online'),
              (OFFLINE, 'Offline'),
              (LOST_REGISTRATION, 'Lost_registration'))

    stable_status = models.CharField(max_length=20, choices=STATUS, default=ONLINE)

    email = models.CharField(max_length=50)

    company_id = models.IntegerField(default=1)

    equipment_code = models.CharField(max_length=20, default='client')

    partner_id = models.IntegerField(default=1)

    status_datetime = models.DateTimeField()















