list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
players_cnt = len(list_players)
team_cnt = players_cnt//2

players_1 = list_players[:team_cnt:]
players_2 = list_players[team_cnt::]
print(players_1)
print(players_2)