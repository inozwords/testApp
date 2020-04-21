from django.db import models
import random, string

class theModel(models.Model):
    #TODO: сделать динамически добавляемыми места и автоматический подсчет их количества
    name = models.CharField(max_length = 100, blank=True, unique=True)
    objectId = models.IntegerField(blank=True, null=True, unique=True)
    apiKey = models.CharField(max_length = 100, null=True, unique=True)

    def save(self):
        self.apiKey = str(self.objectId) + self.name + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        super(theModel, self).save()
