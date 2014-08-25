from classes.coffeeenum import CoffeeEnum

class Order:
	id = 0
	product = 0
	is_superbusy = False
	
	def __init__(self, list_order):
		# This is used to get the coffee names from the id
		coff = CoffeeEnum()
		
		# Order comes in as a list: [id, product, boolean superbusy]
		self.id = list_order[0]
		self.product = coff.get_name(list_order[1])
		self.is_superbusy = list_order[2]