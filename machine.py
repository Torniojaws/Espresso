import msvcrt # Windows-only non-blocking input. Universal would need a lot more things
import random
from classes.espresso import Espresso
from classes.queue import Queue
from classes.coffeeenum import CoffeeEnum
from classes.order import Order

# Launch the machine
num_engineers = 1705
chance_superbusy = 25 # percent
max_time_superbusy = 120 # minutes
espresso_machine = Espresso(num_engineers, chance_superbusy, max_time_superbusy)
espresso_machine.start()

# Setup a few things
queue = Queue()
queue_id = 0
coffee_name = CoffeeEnum()
superbusy = False

# Run the show!
espresso_machine.display_coffee_choices()
while True:
	if queue.has_orders() and espresso_machine.is_ready():
		espresso_machine.brew(queue.get_next(), queue)
	
	# Read input to get new orders and enter superbusy mode
	if msvcrt.kbhit():
		# There's a chance the engineer is superbusy!
		if random.randrange(0, 100) < chance_superbusy:
			print("By surprise, you are now superbusy!")
			superbusy = True
			
		input = msvcrt.getch().decode("ascii").upper()
		# Engineer can also choose to be superbusy to skip the line (hmm...)
		if input == "Y":
			print("You are superbusy! Your order now has priority.")
			superbusy = True
		if input == "S":
			queue.status()
		if input.isdigit():
			if int(input) in range(1, 6):
				print("You ordered:", coffee_name.get_name(input))
				queue_id += 1
				print("Your queue ID is", queue_id)
				new_order = [queue_id, input, superbusy]
				queue.append(new_order)
				superbusy = False
				print("Ready for a new order.")