from django.contrib import admin
from .models import ProductReview


class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'rating',
        'comment',
        'created_at',
    )
    list_filter = ('product', 'rating')
    search_fields = ('comment',)


admin.site.register(ProductReview, ReviewsAdmin)
