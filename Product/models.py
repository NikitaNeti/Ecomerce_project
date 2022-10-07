from django.db import models
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=False)

    parent = TreeForeignKey('self',blank=True, null=True, related_name='children',db_index=True, on_delete=models.CASCADE )

    class Meta:
        unique_together = ('slug', 'parent',)    
        verbose_name_plural = "categories"   

    def __str__(self):                           
        full_path = [self.name]            
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

class Product(models.Model):
        name = models.CharField(max_length=100, unique=True)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        
        short_description = models.CharField(max_length=100)
        # discount_price = models.PositiveBigIntegerField(null=True, blank=True)
        description = models.TextField(null=True, blank=True)
        price = models.DecimalField(max_digits=10,decimal_places=2)
        image = models.ImageField(upload_to='Images/',null=False)
        slug = models.SlugField(max_length=150, unique=True)
        status = models.BooleanField(default=False)
        # tracker = FieldTracker(fields=['slug', 'name', 'product_type'])

        def __str__(self):
            return self.name