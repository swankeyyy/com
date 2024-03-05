from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Category of product(like genre)"""

    name = models.CharField(
        unique=True, max_length=50, verbose_name="Название жанра(genre name)"
    )
    description = models.TextField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name="Описание категории(жанра)(Category descrition)",
    )
    url = models.SlugField(unique=True, max_length=50, verbose_name="Url")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Brand(models.Model):
    """Game Company name"""

    name = models.CharField(
        max_length=100, unique=True, verbose_name="Название бренда(Brand`s name)"
    )
    description = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    """Game Tags"""

    name = models.CharField(max_length=50, verbose_name="Название тега(Tag name)")

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        
    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    """Single Product Item"""

    name = models.CharField(
        max_length=100, verbose_name="Название игры(Name of game)", unique=True
    )
    short_description = models.TextField(
        max_length=300, verbose_name="Краткое описание(Short_description)"
    )
    description = RichTextField(verbose_name="Полное описание(Full description)")
    categories = models.ManyToManyField(
        Category,
        related_name="games",
        verbose_name="Категории(жанры)(Categories(genres))",
    )
    poster = models.ImageField(
        upload_to="media/posters", verbose_name="Обложка(Wrapper)"
    )
    age_limit = models.BooleanField(
        default=False, verbose_name="Ограничение по совершеннолетию(Age limit(18yo))"
    )
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликовать(To publicate)"
    )
    aviable = models.BooleanField(
        default=True, verbose_name="Есть ли в наличии(Aviable)"
    )
    quantity = models.PositiveSmallIntegerField(
        default=1, verbose_name="КОличество на складе(Quantity on warehouse)"
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2, verbose_name="Цена товара(Product Price)"
    )
    url = models.SlugField(max_length=150, unique=True, verbose_name="Url")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name="games")
    year = models.PositiveSmallIntegerField(
        default=2014, verbose_name="Дата выхода(Premier Year)"
    )
    tag = models.ManyToManyField(Tag,  null=True, blank=True, related_name="games")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.name}"


