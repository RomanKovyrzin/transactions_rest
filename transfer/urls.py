from django.conf.urls import url
from transfer import views
from django_filters.views import FilterView


urlpatterns = [
    url(r'^transaction/$',
        views.TransactionsList.as_view(),
        name=views.TransactionsList.name),
    url(r'^transaction/(?P<pk>[0-9]+)$',
        views.TransactionDetail.as_view(),
        name=views.TransactionDetail.name),

    # url(r'^transactions/$',
    #     views.TransactionCreateList.as_view(),
    #     name=views.TransactionCreateList.name),
    # url(r'^transactions/(?P<pk>[0-9]+)$',
    #     views.TransactionCreateDetail.as_view(),
    #     name=views.TransactionCreateDetail.name),

    url(r'country/$',
        views.CountryList.as_view(),
        name=views.CountryList.name),
    url(r'^country/(?P<pk>[0-9]+)$',
        views.CountryDetail.as_view(),
        name=views.CountryDetail.name),

    url(r'^city/$',
        views.CityList.as_view(),
        name=views.CityList.name),
    url(r'^city/(?P<pk>[0-9]+)$',
        views.CityDetail.as_view(),
        name=views.CityDetail.name),

    url(r'^currency/$',
        views.CurrencyList.as_view(),
        name=views.CurrencyList.name),
    url(r'^currency/(?P<pk>[0-9]+)$',
        views.CurrencyDetail.as_view(),
        name=views.CurrencyDetail.name),

    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
    ]
