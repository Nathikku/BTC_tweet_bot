#! /usr/bin/env python3
import tweepy
import bs4

consumer_key='fOPepkUD4s'

consumer_secret='zCBwKRPVfg65mHrapQIReA'

access_token='94967236352-03Iv8OrbkqKhDGa'


access_token_secret='RYFBmwVjqmQvY8SXeQa'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
import bs4
import requests

url = 'https://coinmarketcap.com/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'html.parser')
price = soup.select_one('tr#id-bitcoin a.price').text
print(price)
volume = soup.select_one('tr#id-bitcoin a.volume').text
print(volume)

print(type(soup.select_one('tr#id-bitcoin td.no-wrap.percent-change.text-right.negative_change')))
ty=str((type(soup.select_one('tr#id-bitcoin td.no-wrap.percent-change.text-right.negative_change'))))
print("Type is "+ ty)
#var=soup.select_one('tr#id-bitcoin td.no-wrap.percent-change.text-right.negative_change').text
if ty == "<class 'NoneType'>":
             change= soup.select_one('tr#id-bitcoin td.no-wrap.percent-change.text-right.positive_change').text
else:
              change= soup.select_one('tr#id-bitcoin td.no-wrap.percent-change.text-right.negative_change').text
              

#change= soup.select_one('tr#id-bitcoin td.no-wrap.percent-24h.text-right.positive_change').text


import bs4
import requests

url2='https://api.blockcypher.com/v1/btc/main'

req=requests.get(url2)

#print(req)

json_obj=req.json()
high_fee_per_60_mins=requests.get('https://estimatefee.com/n/6')

medium_fee_per_8_hrs=requests.get('https://estimatefee.com/n/48')
low_fee_per_1day=requests.get('https://estimatefee.com/n/1008')
fees_60_mins=high_fee_per_60_mins.text
fees_8hrs=medium_fee_per_8_hrs.text
fees_24hrs=low_fee_per_1day.text
fees_60=round((float(fees_60_mins))*100000,2)
fees_8hrs=round((float(fees_8hrs))*100000,2)
fees_24hrs=round((float(fees_24hrs))*100000,2)
onehr=('One hour fee: '+str(fees_60)+' sat/byte')
eighthr=('Eight hour fee: '+str(fees_8hrs)+' sat/byte')
oneday=('One day fee: '+str(fees_24hrs)+' sat/byte')

#status_update='Bitcoin Price: ' +price 'Bitcoin Volume:' +volume  'Bitcoin Change in %: '+ change
api.update_status(status='Bitcoin Price: ' +price + '\n'  +'Bitcoin Volume:' +volume +'\n'  + 'Bitcoin Change in %: '+ change + '\n' + '-------------#Bitcoinfee------------ '+'\n' +onehr +'\n' +eighthr +'\n' + oneday+ '\n #Bitcoin #BTC #BitcoinPrice #Bitcoinfees' '\n')
print('Success')
