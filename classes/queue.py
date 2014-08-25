from classes.coffeeenum import CoffeeEnum
from classes.names import Names

class Queue:
	normal_queue = []
	super_queue = []
	# Gets names of coffee types
	coffee_enum = CoffeeEnum()
	# Connect queue ID with a person name
	names = Names()
	
	def __init__(self):
		print("Queue is ready")
		print("----------")
	
	def get_next(self):
		if self.super_queue:
			return self.super_queue[0]
		elif self.normal_queue:
			return self.normal_queue[0]
	
	def has_orders(self):
		if self.super_queue or self.normal_queue:
			return True
		else:
			return False
	
	def status(self):		
		if self.has_orders():
			print("Queue contains:")
			print("=====")
			if self.super_queue:
				print("> Superbusy orders:")
				for order in self.super_queue:
					print(self.names.get_name(order[0]), 
						  "ordered:", self.coffee_enum.get_name(order[1]))
			if self.normal_queue:
				print("> Normal orders:")
				for order in self.normal_queue:
					print(self.names.get_name(order[0]), 
						  "ordered:", self.coffee_enum.get_name(order[1]))
			print("=====")
		else:
			print("Queue is empty! Ready for orders...")
		
	def append(self, list_order):
		print("> Received order:", 
			  self.coffee_enum.get_name(list_order[1]), 
			  "for", self.names.get_name(list_order[0]), 
			  "(Superbusy:", list_order[2], ")")
		if list_order[2]: # Superbusy
			self.super_queue.append(list_order)
		else:
			self.normal_queue.append(list_order)
		
	def remove_order(self, list_order):
		if list_order:
			if list_order[2]: # Superbusy order
				self.super_queue.remove(list_order)
			else:
				self.normal_queue.remove(list_order)