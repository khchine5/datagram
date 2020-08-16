from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse_lazy

from admin_actions.admin import ActionsModelAdmin

from .models import Product, Store,Chain

admin.site.register(Product)
admin.site.register(Store)
#admin.site.register(Chain)

@admin.register(Chain)
class ChainAdmin(ActionsModelAdmin):
    actions_row = ('do_scrap_products', )


    def do_scrap_products(self, request, pk):
        # custom logic here
        object = self.get_object(request,pk)
        object.do_scrap_products()
        return redirect(reverse_lazy('admin:product_chain_changelist'))
    do_scrap_products.short_description = ('Scrap products')