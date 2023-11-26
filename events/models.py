from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class homepost(models.Model):
    postname = models.CharField('Name',max_length=20)      
    introduction = models.TextField('Introduction',max_length=500)
    writer = models.CharField('writer',max_length=20 ,null=True)
    website = models.URLField(max_length=250 ,blank=True ,null=True)    
    post_date = models.DateTimeField(default=datetime.now ,blank=True)
    owner = models.IntegerField("Information Owner", blank=False, default=1)
    ownerid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):  #superuser要用的
        return self.postname
        
class Interest(models.Model):
    game = models.CharField('Interest Game',max_length=20)
    code = models.CharField('Interest Code',max_length=20)
    Hobby = models.CharField('Interest Hobby',max_length=20)
    
    def __str__(self):  #superuser要用的
        return self.game
   
class information(models.Model):
    name = models.CharField('Name',max_length=20)      
    interest = models.ForeignKey(Interest, blank=True, null=True, on_delete=models.CASCADE)
    introduction = models.CharField('Introduction',max_length=50)
    recent_events = models.CharField('Recent_events',max_length=50)
    refresh_date = models.DateTimeField(default=datetime.now, blank=True)
    autobiography = models.TextField('Autobiography',max_length=500)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.IntegerField("Information Owner", blank=False, default=1)
    ownerid = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):  #superuser要用的
        return self.name

#以下三個為About me       
class wherefrom(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title

class introduction(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title
    
class autobiography(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title    

#以下二個為Licence   
class Licence(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title

class Licence1(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title
    
#以下二個為Ability
class Ability(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title

class Ability1(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title
    
#以下二個為Experience
class Experience(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title

class Experience1(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title
    
#以下為Dream
class Dream(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title
    



class paper(models.Model):
    papername = models.CharField('Papername',max_length=100)
    papercontent = models.TextField('Papercontent',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.papername
        
class all_aboutus(models.Model):
    experience = models.CharField('Experience',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.experience
        
class Portfolio(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title
        
class article(models.Model):
    title = models.CharField('title',max_length=100)
    content = models.TextField('content',max_length=10000)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):  #superuser要用的
        return self.title


#API
class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):  #superuser要用的
        return self.name