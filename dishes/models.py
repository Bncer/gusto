from django.db import models

CATEGORY_CHOICES = (
    ('salads', 'Salads'),
    ('shashlyk', 'Shashlyk'),
    ('first-course', 'First Course'),
    ('second-course', 'Second Course'),
    ('set-lunch', 'Set Lunch'),
    ('meat-dishes', 'Meat Dishes'),
    ('pilaf', 'Pilaf'),
    ('fish', 'Fish'),
    ('alcohol', 'Alcohol'),
    ('drinks', 'Drinks'),
    ('snacks', 'Snacks'),
)


class MenuItem(models.Model):
    name = models.CharField(max_length=255, verbose_name='dish')
    weight = models.IntegerField(null=True, blank=True, verbose_name='weight')
    price = models.IntegerField(verbose_name='price')
    category = models.CharField(max_length=128, choices=CATEGORY_CHOICES, default=0, verbose_name='category')

    class Meta:
        verbose_name='dish'
        verbose_name_plural='dishes'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name