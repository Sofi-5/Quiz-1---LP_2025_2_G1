from collections import defaultdict

class Recommender:
    def __init__(self):
        self.user_purchases = defaultdict(set)
        self.product_links = defaultdict(lambda: defaultdict(int))

    def add_purchase(self, user, product):
        # Si el producto ya fue comprado, no lo volvemos a procesar
        if product in self.user_purchases[user]:
            return

        # Actualizar relaciones de co-compra
        for other in self.user_purchases[user]:
            self.product_links[product][other] += 1
            self.product_links[other][product] += 1

        self.user_purchases[user].add(product)

    def get_recommendations(self, user):
        scores = defaultdict(int)
        purchased = self.user_purchases[user]

        for product in purchased:
            related = self.product_links[product]
            for other_product, score in related.items():
                if other_product not in purchased:
                    scores[other_product] += score

        # Ordenar por puntuación de mayor a menor
        return sorted(scores.items(), key=lambda x: -x[1])

####################################### Prueba de la simulación ###############################

# Crear sistema
rec = Recommender()

# Simular compras
rec.add_purchase("Ana", "zapatos")
rec.add_purchase("Ana", "pantalón")
rec.add_purchase("Luis", "zapatos")
rec.add_purchase("Luis", "camisa")
rec.add_purchase("Luis", "gorra")
rec.add_purchase("Carlos", "pantalón")
rec.add_purchase("Carlos", "camisa")
rec.add_purchase("Carlos", "zapatos")

# Recomendaciones para Ana (ya tiene zapatos y pantalón)
print("Recomendaciones para Ana:", rec.get_recommendations("Ana"))

# Recomendaciones para Luis (tiene zapatos, camisa, gorra)
print("Recomendaciones para Luis:", rec.get_recommendations("Luis"))

