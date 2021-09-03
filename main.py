from dotenv import load_dotenv
import os
import urllib3
import cassiopeia as cass
from cassiopeia.data import Season, Queue
from collections import Counter

load_dotenv()
key = os.environ.get('KEY')
played_champions = Counter()
cass.set_riot_api_key(key)
champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region="NA")}
sum = cass.Summoner(name="SINGED TURBO SEX", region="NA")
singed = cass.Champion(name="Singed", id=27, region="NA")
print(sum.exists)
matches = sum.match_history()
matches = matches(queues={Queue.ranked_solo_fives})

for match in matches:
    champion_id = match.participants[sum.name].champion.id
    champion_name = champion_id_to_name_mapping[champion_id]
    played_champions[champion_name] += 1
    print("Length of match history:", len(matches))
print("Top 10 champions {} played:".format(sum.name))
for champion_name, count in played_champions.most_common(10):
        print(champion_name, count)
print()
match = matches[0]
print('Match ID:', match.id)

p = match.participants[sum]
print(p.summoner.name, 'playing', p.champion.name)
print(p.id, p.summoner.region, p.summoner.account_id, p.summoner.name, p.summoner.id, p.champion.id)
print("////BLOCKER////")
print("Blue team:")
for p in match.blue_team.participants:
    print(p.summoner.name, 'playing', p.champion.name, "with", p.runes.keystone.name, "in", p.role.name)
print("Red team:")
for p in match.red_team.participants:
    print(p.summoner.name, 'playing', p.champion.name, "with", p.runes.keystone.name, "in", p.role.name)