from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length = 100, null=False, blank=False)
    category = models.ForeignKey("Category", on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    describdion = models.TextField()
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length = 100, null=False, blank=False)
    email = models.EmailField(max_length = 100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name} - {self.email}"