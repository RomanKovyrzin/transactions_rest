from rest_framework import serializers
from django.contrib.auth.models import User
from transfer.models import Country
from transfer.models import City
from transfer.models import Currency
from transfer.models import Transaction
import transfer.views


# Authentication
class UserTransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'url',
            'amount',
            )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    transactions = UserTransactionSerializer(
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = (
            'url',
            'pk',
            'username',
            'transaction'
            )
# End of Authentication


class TransactionsSerializer(serializers.HyperlinkedModelSerializer):
    # Display the owner's username (read-only)
    owner = serializers.ReadOnlyField(source='owner.username')

    # Display country
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(),
        slug_field='name',)

    # Display city
    city = serializers.SlugRelatedField(
        queryset=City.objects.all(),
        slug_field='name',)

    # Display currency
    currency = serializers.SlugRelatedField(
        queryset=Currency.objects.all(),
        slug_field='iso_code',)

    class Meta:
        model = Transaction
        fields = (
            'url',
            # 'pk',
            'owner',
            'country',
            'city',
            'currency',
            'amount',
            'transaction_time')


class CurrencySerializer(serializers.HyperlinkedModelSerializer):

    transactions = TransactionsSerializer(
        many=True,
        allow_null=True,
        read_only=True)

    class Meta:
        model = Currency
        fields = (
            'url',
            # 'pk',
            'iso_code',
            'transactions',)


class CitySerializer(serializers.HyperlinkedModelSerializer):

    # Display the Country
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(),
        slug_field='name')

    transactions = TransactionsSerializer(
        many=True,
        allow_null=True,
        read_only=True)

    class Meta:
        model = City
        fields = (
            'url',
            # 'pk',
            'country',
            'name',
            'transactions',)


class CountrySerializer(serializers.HyperlinkedModelSerializer):

    # cities = CitySerializer(
    #     many=True,
    #     allow_null=True,
    #     read_only=True)

    transactions = TransactionsSerializer(
        many=True,
        allow_null=True,
        read_only=True)

    class Meta:
        model = Country
        fields = (
            'url',
            # 'pk',
            'name',
            # 'cities',
            'transactions',)


# class TransactionCreateSerializer(serializers.HyperlinkedModelSerializer):
#     # Display country
#     country = CountrySerializer()
#
#     # Display city
#     city = CitySerializer()
#
#     # Display currency
#     currency = CurrencySerializer()
#
#     class Meta:
#         model = Transaction
#         fields = (
#             'url',
#             # 'pk',
#             'country',
#             'city',
#             'currency',
#             'amount',)
