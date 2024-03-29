from controlcenter import Dashboard, widgets
from products.models import Product

class ModelItemList(widgets.ItemList):
    model = Product
    list_display = ('ProductName','Supplier')

class PriceDashboard(Dashboard):
    widgets = (
        ModelItemList,
    )


class DashboardPriceChart(widgets.SingleBarChart):
	values_list = ('ProductName')
	queryset = Product.objects.filter(ProductName__icontains="Macbook")
	# values_list = ('name', 'supplier')
	# queryset = Product.objects.order_by('name')
	# limit_to = 3