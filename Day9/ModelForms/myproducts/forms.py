from django.forms import ModelForm
from myproducts.models import Products

class Myclass(ModelForm):
	class Meta:
		model=Products
		fields='__all__'#['p_name','p_cost']
