play_data = {
    'result' : '승리',
    'champ_name' : '비에고',
    'kill' : 13,
    'death' : 9,
    'assist' : 13
}

print(play_data)

play_data['result'] = '패배'
play_data['level'] = '18'
del play_data['death']

print(play_data)

for key in play_data.keys():
    print(key)

for value in play_data.values():
    print(value)

for key, value in play_data.items():
    print(key, value)