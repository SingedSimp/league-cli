from dotenv import load_dotenv
import os
import urllib3
import cassiopeia as cass

load_dotenv()
key = os.environ.get('KEY')
cass.set_riot_api_key(key)
sts = cass.Summoner(name="SINGED TURBO SEX", region="NA")
singed = cass.Champion(name="Singed", id=27, region="NA")
print(sts.exists)
print(sts.level)
print(sts.platform)
singedm = cass.ChampionMastery(summoner=sts, champion=singed, region="NA")
print(singedm.points)