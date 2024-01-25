from rest_framework import serializers

from ticket.models import Ticket


class TicketSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    title = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    price_usd = serializers.IntegerField()
    odometer = serializers.IntegerField()
    username = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    phone_number = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    image_url = serializers.CharField(max_length=255, allow_blank=False, allow_null=False)
    images_count = serializers.IntegerField()
    car_number = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    car_vin = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    datatime_found = serializers.DateTimeField(required=False, allow_null=True)

    def create(self, validated_data):
        if Ticket.objects.filter(url=validated_data.get('url')).exists():
            raise serializers.ValidationError('Ticket already exists')
        return Ticket.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        instance.title = validated_data.get('title', instance.title)
        instance.price_usd = validated_data.get('price_usd', instance.price_usd)
        instance.odometer = validated_data.get('odometer', instance.odometer)
        instance.username = validated_data.get('username', instance.username)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.images_count = validated_data.get('images_count', instance.images_count)
        instance.car_number = validated_data.get('car_number', instance.car_number)
        instance.car_vin = validated_data.get('car_vin', instance.car_vin)
        instance.datatime_found = validated_data.get('datatime_found', instance.datatime_found)
        instance.save()
        return instance

    def to_representation(self, instance):
        return {
            'url': instance.url,
            'title': instance.title,
            'price_usd': instance.price_usd,
            'odometer': instance.odometer,
            'username': instance.username,
            'phone_number': instance.phone_number,
            'image_url': instance.image_url,
            'images_count': instance.images_count,
            'car_number': instance.car_number,
            'car_vin': instance.car_vin,
            'datatime_found': instance.datatime_found
        }
