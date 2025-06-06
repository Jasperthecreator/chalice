from pytrends.request import TrendReq
import time
from dotenv import load_dotenv
import os
load_dotenv('keys.env')
trends = TrendReq()
trends.build_payload(
    kw_list=['/g/11g8vtqdjz', '/g/11tsnttdcp'],
    geo='IN',
    timeframe='today 1-m'
)
df = trends.interest_over_time()
data_science_7d = int(df['/g/11g8vtqdjz'].iloc[-1])
data_analyst_7d = int(df['/g/11tsnttdcp'].iloc[-1])
from supabase import create_client, Client
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_KEY')
trend_agg = {"data_science_7d": data_science_7d, "data_analyst_7d": data_analyst_7d}
client = create_client(url, key)
client.table("Pytrends - DS").insert(trend_agg).execute()
