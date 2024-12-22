from django.db import models

class AssetType(models.TextChoices):
    STOCK = "STOCK", "Stock"
    CRYPTO = "CRYPTO", "Crypto"
    ETF = "ETF", "ETF"
    REIT = "REIT", "REIT"
    OTHER = "OTHER", "Other"

class TradeTransactionType(models.TextChoices):
    BUY = "BUY", "Buy"
    SELL = "SELL", "Sell"
