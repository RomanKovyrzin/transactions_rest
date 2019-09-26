from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import rest_framework as filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
# Login/password authentication
from rest_framework import permissions
from transfer import custompermission
# Token authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from transfer.models import Country
from transfer.models import City
from transfer.models import Currency
from transfer.models import Transaction
from transfer.serializers import CountrySerializer
from transfer.serializers import CitySerializer
from transfer.serializers import CurrencySerializer
from transfer.serializers import TransactionsSerializer
# from transfer.serializers import TransactionCreateSerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    name = 'country-list'
    filterset_fields = (
        'name',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        )


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    name = 'country-detail'


class CityList(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    name = 'city-list'
    filterset_fields = (
        'name',
        )
    search_fields = (
        '^name',
        )
    ordering_fields = (
        'name',
        )


class CityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    name = 'city-detail'


class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name = 'currency-list'
    filterset_fields = (
        'iso_code',
        )
    search_fields = (
        '^iso_code',
        )
    ordering_fields = (
        'iso_code',
        )


class CurrencyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    name = 'currency-detail'


# Create a customized filter applying to the Competition model
class TransactionFilter(filters.FilterSet):
    from_achievement_time = DateTimeFilter(
        field_name='transaction_time', lookup_expr='gte')
    to_achievement_time = DateTimeFilter(
        field_name='transaction_time', lookup_expr='lte')
    min_transaction_amount = NumberFilter(
        field_name='amount', lookup_expr='gte')
    max_transaction_amount = NumberFilter(
        field_name='amount', lookup_expr='lte')
    currency = AllValuesFilter(
        field_name='currency__iso_code')
    country = AllValuesFilter(
        field_name='country__name')
    city = AllValuesFilter(
        field_name='city__name')

    class Meta:
        model = Transaction
        fields = (
            'from_achievement_time',
            'to_achievement_time',
            'min_transaction_amount',
            'max_transaction_amount',
            'currency',
            'country',
            'city',
            )


class TransactionsList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer
    name = 'transactions-list'
    filterset_class = TransactionFilter
    search_fields = (
        '^amount',
        'transaction_time'
        )
    ordering_fields = (
        'country',
        'city',
        'currency',
        'transaction_time',
        )
    # Set permissions polices
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
        # IsAuthenticated, # token authentication
        )
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    # Set token authentication
    # authentication_classes = (
    #     TokenAuthentication,
    #     )


class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer
    name = 'transaction-detail'
    # Set permissions polices
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsCurrentUserOwnerOrReadOnly,
        IsAuthenticated,
        )
    # Set token authentication
    authentication_classes = (
        TokenAuthentication,
        )
    # permission_classes = (
    #     IsAuthenticated,
    #     )


# class TransactionCreateList(generics.ListCreateAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionCreateSerializer
#     name = 'create-transaction-list'
#
#
# class TransactionCreateDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionCreateSerializer
#     name = 'create-transaction-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'Transactions': reverse(TransactionsList.name, request=request),
            # 'Create Transaction': reverse(TransactionCreateList.name, request=request),
            'Countries': reverse(CountryList.name, request=request),
            'Cities': reverse(CityList.name, request=request),
            'Currencies': reverse(CurrencyList.name, request=request),
            })
