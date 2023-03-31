from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct
from rest_framework.exceptions import ValidationError


class ProductSerializer(serializers.ModelSerializer):
    # настройте сериализатор для продукта
    title = serializers.CharField(min_length=2)

    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    product_name = serializers.ReadOnlyField(source='product.title')
    product_desc = serializers.ReadOnlyField(source='product.description')

    class Meta:
        model = StockProduct
        fields = ['product', 'product_name', 'product_desc', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    # настройте сериализатор для склада
    class Meta:
        model = Stock
        fields = ['id', 'address', 'positions']

    def validate_positions(self, value):
        product_ids = [i['product'].id for i in value]
        if len(product_ids) != len(set(product_ids)):
            raise ValidationError('Дублирование продукта на складе')
        return value

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # здесь вам надо заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for i in positions:
            StockProduct.objects.create(stock=stock, product=i['product'], quantity=i['quantity'], price=i['price'])

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions

        for i in positions:
            product = i.pop('product')

            StockProduct.objects.update_or_create(stock=stock, product=product, defaults={
                'quantity': i['quantity'],
                'price': i['price']
            })

        return stock