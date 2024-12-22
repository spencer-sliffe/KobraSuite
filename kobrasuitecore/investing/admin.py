# investing/admin.py

from django.contrib import admin
from .models import (
    Portfolio, Asset, Holding, TradeTransaction,
    Watchlist, MarketData
)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at',)

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'asset_type', 'name')
    search_fields = ('symbol', 'name')
    list_filter = ('asset_type',)

@admin.register(Holding)
class HoldingAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'asset', 'quantity', 'average_cost', 'created_at')
    search_fields = ('portfolio__name', 'asset__symbol')
    list_filter = ('created_at',)

@admin.register(TradeTransaction)
class TradeTransactionAdmin(admin.ModelAdmin):
    list_display = ('holding', 'transaction_type', 'quantity', 'price_per_unit', 'transaction_date', 'fees')
    search_fields = ('holding__portfolio__name', 'holding__asset__symbol')
    list_filter = ('transaction_type', 'transaction_date')

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('created_at',)
    filter_horizontal = ('assets',)

@admin.register(MarketData)
class MarketDataAdmin(admin.ModelAdmin):
    list_display = ('asset', 'date', 'open_price', 'close_price', 'volume')
    search_fields = ('asset__symbol',)
    list_filter = ('date',)
