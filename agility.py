# id решения: 69304360
from typing import Dict, List


def vic_score(game_field: List[str], num_of_keys: int) -> int:
    """Подсчёт максимально возможных победных очков."""

    # находим количество вхождений каждой цифры
    presence_num: Dict = dict()
    for num in game_field:
        if num in presence_num:
            presence_num[num] += 1
        else:
            presence_num[num] = 1

    # определяем варианты, доступные игрокам
    score: int = 0
    for key, val in presence_num.items():
        if val <= num_of_keys * 2:
            score += 1

    return score


if __name__ == '__main__':

    # считываем входные данные
    num_of_keys: int = int(input())
    game_field: List[str] = []
    for i in range(4):
        game_field.extend([s for s in input() if s != '.'])

    print(vic_score(game_field, num_of_keys))
