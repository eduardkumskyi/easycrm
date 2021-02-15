from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PrimaryProductSupplier(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    phone = models.CharField(verbose_name='Телефон', max_length=150, blank=True)
    link = models.CharField(verbose_name='Ссылка', max_length=150, blank=True)
    comment = models.CharField(verbose_name='Комментарий', max_length=400, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class PrimaryProductType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип сырья'
        verbose_name_plural = 'Типы сырья'


class PrimaryProduct(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    type = models.ForeignKey(PrimaryProductType, verbose_name='Тип', on_delete=models.CASCADE)
    in_stock = models.IntegerField(verbose_name='Кол-во')
    UNITS = (
        (1, 'м.'),
        (2, 'кг'),
        (3, 'шт.'),
        (4, 'уп.')
    )
    unit = models.IntegerField(verbose_name='Ед. измерения', choices=UNITS, default='1')
    price = models.IntegerField(verbose_name='Стоимость', default=0)
    supplier = models.ForeignKey(PrimaryProductSupplier, verbose_name='Поставщик', on_delete=models.CASCADE)
    date_of_receiving = models.DateTimeField(verbose_name='Дата получения', blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сырье'
        verbose_name_plural = 'Сырье'


class ProductType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товара'


class ProductSize(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)
    type = models.ForeignKey(ProductType, verbose_name='Тип', on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, verbose_name='Размер', on_delete=models.CASCADE, blank=True)
    in_stock = models.IntegerField(verbose_name='Кол-во', default=0)
    UNITS = (
        (1, 'м.'),
        (2, 'кг'),
        (3, 'шт.'),
        (4, 'уп.')
    )
    unit = models.IntegerField(verbose_name='Ед. измерения', choices=UNITS, default='1')
    standard_price = models.IntegerField(verbose_name='Стандартная стоимость', default=0)
    sale_price = models.IntegerField(verbose_name='Акционная стоимость', default=0, blank=True)
    wholesale_price = models.IntegerField(verbose_name='Оптовая стоимость', default=0, blank=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
