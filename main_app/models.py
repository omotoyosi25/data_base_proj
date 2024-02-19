from django.db import models

# Create your models here.
class Blogpost (models.Model):
    title= models.CharField(max_length=200, verbose_name="blog title", unique=True, null=False)
    description=models.CharField(max_length=500)
    content=models.TextField()#unlimited number text
    posted_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    view_count=models.PositiveIntegerField()
    published=models.BooleanField(default=False)
    rating=models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.title

    class Meta:
        db_table="post"
        verbose_name="post"
        verbose_name_plural="posts"
        ordering=["posted_at"]