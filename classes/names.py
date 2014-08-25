import random

class Names:
	def get_name(self, id):
		id = int(id)
		# Keep value in 0-9 range for demo purposes
		if id >= 10:
			id = random.randint(0, 9)
		return {
			1: "Albert",
			2: "Benjamin",
			3: "Charles",
			4: "Dmitri",
			5: "Euclid",
			6: "Francis",
			7: "Gustav",
			8: "Hermann",
			9: "Isaac",
			0: "John",
		}.get(id, "Bjarne")