from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify
from mptt.models import MPTTModel, TreeForeignKey
from tinymce import models as tinymce_models

class Category(MPTTModel):

    name = models.CharField(max_length=50)
    slug = models.SlugField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    def natural_key(self):
        return {
            'slug': self.slug,
            'name': self.name
        }


class Post(models.Model):
    DRAFT = 0
    PUBLISHED = 1

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    )

    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, upload_to='uploads/')
    slug = models.SlugField()
    content = tinymce_models.HTMLField()
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=DRAFT
    )

    def __str__(self):
        return self.title
