class CoffeeEnum:
	def get_name(self, id):
		id = int(id)
		return {
			1: "Espresso",
			2: "Cappuccino",
			3: "Latte",
			4: "Macchiato",
			5: "Irish Coffee",
		}.get(id, "Coffee")