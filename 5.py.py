import random

class LootBox:
    def __init__(self):
        self.items = {
            'обычные': {'шанс': 0.7, 'цвет': 'белый'},
            'редкие': {'шанс': 0.2, 'цвет': 'синий'},
            'эпические': {'шанс': 0.1, 'цвет': 'фиолетовый'},
            'легендарные': {'шанс': 0.05, 'цвет': 'оранжевый'}
        }
        self.guarantee_count = 20
        self.total_opened = 0
        self.results = {'обычные': 0, 'редкие': 0, 'эпические': 0, 'легендарные': 0}
        self.items_received = []

    def open_box(self):
        self.total_opened += 1
        total_weight = sum(item['шанс'] for item in self.items.values())
        result = None
        rand_num = random.uniform(0, total_weight)
        cumulative_weight = 0
        for item, data in self.items.items():
            cumulative_weight += data['шанс']
            if rand_num < cumulative_weight:
                result = item
                break
        self.results[result] += 1
        self.items_received.append({'качество': result, 'цвет': self.items[result]['цвет']})

    def check_guarantee(self):
        if self.total_opened % self.guarantee_count == 0:
            self.results['легендарные'] += 1
            self.items_received.append({'качество': 'легендарные', 'цвет': 'оранжевый'})

    def display_results(self):
        print("Результаты открытия лутбоксов:")
        for quality, count in self.results.items():
            print(f"{quality}: {count}")
        print("Полученные предметы:")
        for item in self.items_received:
            print(f"\033[1;37;40m{item['качество']}: \033[1;{self.color_code(item['цвет'])};40m██████\033[0;37;40m")

    def color_code(self, color):
        if color == 'белый':
            return 37
        elif color == 'синий':
            return 34
        elif color == 'фиолетовый':
            return 35
        elif color == 'оранжевый':
            return 33
        else:
            return 37

    def run_simulations(self, simulations=20):
        for _ in range(simulations):
            self.open_box()
            self.check_guarantee()
        self.display_results()

# Создаем объект лутбокса и запускаем симуляцию открытия 20 лутбоксов
loot_box = LootBox()
loot_box.run_simulations()
