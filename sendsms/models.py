from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    phone_number = PhoneNumberField()
    information = models.TextField(null=True)

    def __str__(self):
        return self.name


 
class Information(models.Model):
    information = models.TextField(null=True)

    def __str__(self):
        return self.id

# class Person(models.Model):
#     name=models.CharField(max_length=400, null=True)
#     message = models.ForeignKey(Message, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.message.text


    # def save(self, *args,**kwargs):
    #     account_sid = 'ACb7102e89e1e3770287463f0df2b1c23c'
    #     auth_token = '3c010c63d00efa4526b34c92911a88ad'
    #     client = Client(account_sid, auth_token)

    #     message = client.messages.create(
    #                         body=f"Hello {self.name} {self.message.text} ",
    #                         from_='+13862040748',
    #                         to='+254742415221')
    #     return super().save(*args, **kwargs)  


   