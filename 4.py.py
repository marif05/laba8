import random

def simulate_game(num_doors, num_prizes):
    # Генерируем случайное распределение призов и пустот за дверями
    doors = ["пусто"] * num_doors
    prize_indices = random.sample(range(num_doors), num_prizes)
    for idx in prize_indices:
        doors[idx] = "приз"

    # Предполагаем, что два игрока выбирают случайные двери
    player1_choice = random.randint(0, num_doors - 1)
    player2_choice = random.randint(0, num_doors - 1)

    # Открываем одну из дверей, за которой нет приза
    opened_door = random.choice([idx for idx in range(num_doors) if idx != player1_choice and doors[idx] == "пусто"])

    # Игрок 1 решает поменять свой выбор
    new_player1_choice = next(idx for idx in range(num_doors) if idx != player1_choice and idx != opened_door)

    # Определяем результаты для обоих игроков
    player1_win_if_change = (doors[new_player1_choice] == "приз")
    player2_win_if_stay = (doors[player2_choice] == "приз")

    return {
        "player1_win_if_change": player1_win_if_change,
        "player2_win_if_stay": player2_win_if_stay
    }

def calculate_probabilities(results):
    total_games = len(results)
    player1_change_wins = sum(1 for result in results if result["player1_win_if_change"])
    player2_stay_wins = sum(1 for result in results if result["player2_win_if_stay"])

    probability_change = player1_change_wins / total_games
    probability_stay = player2_stay_wins / total_games

    return probability_change, probability_stay

def main(num_games, num_doors, num_prizes):
    results = []
    for _ in range(num_games):
        results.append(simulate_game(num_doors, num_prizes))
    
    probability_change, probability_stay = calculate_probabilities(results)

    print(f"Вероятность выигрыша для игрока, меняющего свой выбор: {probability_change:.4f}")
    print(f"Вероятность выигрыша для игрока, оставшегося при своем первоначальном выборе: {probability_stay:.4f}")

if __name__ == "__main__":
    num_games = 10000  # количество игр для моделирования
    num_doors = 3  # количество дверей
    num_prizes = 1  # количество призов за дверью

    main(num_games, num_doors, num_prizes)
