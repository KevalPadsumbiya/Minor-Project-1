from django.db import models

class mobileSpecsLink(models.Model):
    brand_name = models.CharField(max_length=100)
    mobile_name = models.CharField(max_length=250)
    specifications = models.CharField(max_length=1500)
    image_link = models.CharField(max_length=1000) 

    def __str__(self):
        return self.brand_name+'---'+self.mobile_name+'---'+self.image_link+'---'+self.specifications

class UserData(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=100)
    password = models.CharField(max_length=10)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.user_name

class Compare(models.Model):
    username = models.ForeignKey(UserData,on_delete=models.CASCADE)
    mobile = models.ForeignKey(mobileSpecsLink,on_delete=models.CASCADE)
    # primary_key = models.IntegerField()

    def __str__(self):
        return str(self.mobile)+"...."+str(self.username)

class Favourite(models.Model):
    username = models.ForeignKey(UserData,on_delete=models.CASCADE)
    mobile = models.ForeignKey(mobileSpecsLink,on_delete=models.CASCADE)
    # primary_key = models.IntegerField()

    def __str__(self):
        return str(self.mobile)+"...."+str(self.username)
    
class Comments(models.Model):
    username = models.ForeignKey(UserData,on_delete=models.CASCADE)
    mobile = models.ForeignKey(mobileSpecsLink,on_delete=models.CASCADE)
    comment= models.CharField(max_length=2000)
    date = models.DateField()
    vote_count = models.IntegerField()

    def __str__(self):
        return str(self.mobile)+"---"+str(self.vote_count)+"---"+str(self.username)+"---"+self.comment+"---"+str(self.date)

class Votes(models.Model):
    username = models.ForeignKey(UserData,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
    mobile = models.ForeignKey(mobileSpecsLink,on_delete=models.CASCADE)
    upvote = models.IntegerField()
    downvote = models.IntegerField()

    def __str__(self):
        return str(self.username)+"---"+str(self.comment)+"---"+str(self.upvote)+"---"+str(self.downvote)
