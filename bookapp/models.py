from django.db import models

class Author(models.Model):

    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        
        return '{}'.format(self.name)
    


class Book(models.Model):

    title=models.CharField(max_length=200,null=True)

    price=models.IntegerField(null=True)

    image=models.ImageField(upload_to='book_media')

    author=models.ForeignKey(Author, on_delete=models.CASCADE,null=True)

    quantity=models.IntegerField()



    def __str__(self):
        
        return '{}'.format(self.title)
    
    