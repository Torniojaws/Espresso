from time import time
from classes.queue import Queue

class Espresso:
	num_engineers = 0
	chance_superbusy = 0 # percent
	max_time_superbusy = 0 # minutes
	is_running = False
	is_brewing = False
	brew_started_time = 0
	brew_ready_time = time() + 2 # +2 to prevent unneeded message on launch
	queue = 0
	current_brew = 0
	
	def __init__(self, num_engineers, chance_superbusy, max_time_superbusy):
		print("Espresso is booting...")
		print("> Engineer count:", num_engineers)
		print("> Chance superbusy:", chance_superbusy, "%")
		print("> Max time being superbusy:", max_time_superbusy, "minutes")
	
	def start(self):
		is_running = True
		print("Espresso machine started OK")
		print("> Press any key except A-Z or 0-9 to exit")
		
	def display_coffee_choices(self):
		print("Pick your poison, Mr. Engineer! \n"
			  "If you are superbusy, press (Y) for priority lane! \n"
			  "(S) for Queue Status")
		print("1 - Espresso")
		print("2 - Cappuccino")
		print("3 - Latte")
		print("4 - Macchiato")
		print("5 - Irish Coffee")
		return "" # Otherwise will display "None"
		
	def is_ready(self):
		if time() >= self.brew_ready_time and self.is_brewing:
			print("Brew ready!")
			self.queue.remove_order(self.current_brew)
			if not self.queue.has_orders():
				print("Queue empty, ready for new orders!")
			self.is_brewing = False
		if self.is_brewing:
			return False
		else:
			return True
	
	def brew(self, coffee, queue):
		if queue.has_orders():
			self.queue = queue
			self.current_brew = coffee
			print("Brewing now... ready in 15 seconds!")
			self.brew_started_time = time()
			self.brew_ready_time = time() + 15
			self.is_brewing = True