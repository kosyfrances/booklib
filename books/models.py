from django.db import models


class Category(models.Model):
    """Model representing a book's category."""

    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model representing a book."""

    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=150)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.title
