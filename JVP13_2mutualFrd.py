from itertools import combinations

data = [
    "user1:user2,user3,user4",
    "user2:user1,user3,user5",
    "user3:user1,user2,user4,user5",
    "user4:user1,user3",
    "user5:user2,user3"
]

user_friends = {}
for line in data:
    user, friends = line.split(':')
    user_friends[user] = set(friends.split(','))

print("Individual Friends:")
for user, friends in user_friends.items():
    print(f'("{user}", {sorted(friends)})')

print("\nMutual Friends Between Pairs:")
pairs = combinations(sorted(user_friends.keys()), 2)
for u1, u2 in pairs:
    mutual = user_friends[u1] & user_friends[u2]
    if mutual:
        print(f'("{u1}", "{u2}"), {sorted(mutual)}')
