def move (players,step):
    num =step - 1
    while num > 0:
        tmp = players.pop(0)
        players.append(tmp)
        num = num-1
    return players

def play(players,step,alive):
    players_list=[i for i in range(1,players+1)]
    while len(player_list)>alive
        play_list = move(player_list,step)
        player_list.pop(0)
    return players_list
plays = int(input())
step = int(input())
alive = int(input())