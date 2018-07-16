from __future__ import unicode_literals

from django.db import models
from .. login.models import User

class ItemManager(models.Manager):
    def makeItem(self,postData):
        status={'valid:true, 'errors':[]}
        if not postData['name'] or len(postData['name']) <3:
            status['vaild']=False
            status['errors'].append('Invaild Item. Check your item')

            item = Item.objects.filter(name=postData['name'])

            if status['vaild']is False:
                try:
                    status['errors'].append('Item was not created. Please try again')
                except:
                    item = Item.objects.create(name=postData['name'], owner=objects.get(id=postData['owner']))
                    item.save()

                return status

    def add_to_list(self, item_id, user_id):
        status={'vaild':True, 'errors':[]}
        try:
            item = Item.objects.get(id=item_id)
            item.wanted.add(user_id)
        except:IntegrutyError as e:
            status['vaild']=False
            status['errors'].append.(e.message)

        return status

class Item(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey('login.User', related_name='owner')
    wanted = models.ManyToManyField('login.User', related_name='wanted')
    created = models.DateTimeField(auto_now_add=TRUE)
    updated = models.DateTimeField(auto_now=TRUE)

    objects = ItemManger()

    def __str__(self):
        return self.name



# Create your models here.
