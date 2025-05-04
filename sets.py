#4
all_students ={"Alice","Bob","Charlie","David","Eve","Frank"}
football_players={"Alice","Bob","Charlie"}
cricket_players={"Charlie","David","Eve"}

both=football_players &cricket_players

only_one=(football_players^cricket_players)

none=all_students-(football_players| cricket_players)

print("students who play both football and cricket:",both)
print("students who play only one of the games:",only_one)
print("students who play none:",none)
