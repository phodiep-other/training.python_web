import urllib2
import time
import json
from bs4 import BeautifulSoup
import oauth2

#----

def get_url(pageNumber):
  url = 'http://seattle.craigslist.org/see/apa/'
  if pageNumber == 0:
    return url
  elif pageNumber in range(1,10):
    url += 'index'+str(pageNumber)+'00.html'
  return url


def parse_url(url):
  html = urllib2.urlopen(url)
  readData = html.read()  
  parsed = BeautifulSoup(readData)
  return parsed


def find_lat_long(data):
  data = str(data)
  start = data.find('<')+15
  end = data.find('>')
  dataString = data[start:end].strip('<p class="row" data-latitude=')
  dataString = dataString.replace('" data-longitude="',',')
  tmpList = dataString.split(',')
  return tmpList[0],tmpList[1]


def find_header(data):
  try:
    result = data.find('span', class_='itemph').text.strip()
  except:
    result = ''
  return result


def find_neighborhood(data):
  try:
    result = data.find('span', class_='itempn').text.strip()
  except:
    result = ''
  return result


def find_postURL(data):
  try:
    anchor = data.find('a')
    result = anchor.attrs['href']
  except:
    result = ''
  return result


def find_title(data):
  try:
    anchor = data.find('a')
    result = anchor.text.strip()
  except:
    result = ''
  return result


def yelp_search(loc_lat,loc_long,search):

  #adopted from example ***********
  #https://github.com/Yelp/yelp-api/blob/master/v2/python/sign_request.py#

  consumer_key = 'nqWG3SCAY1XXLwgQF1OCbw'
  consumer_secret = 'cRI33I2Heh_s7neiEm9RECMJhhY'
  token = 'MuznJpvCglO598Iioxi6lrvRQruwo6oK'
  token_secret = 'H_TfQb1v1x07o9Te3GSM9YBO9so'

  loc = '&ll=' + str(loc_lat) + ',' + str(loc_long)
  sort = '&sort=0'
  limit = '&limit=2'
  term = '&term=' + search
  
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  url = 'http://api.yelp.com/v2/search?' + term + loc + sort + limit

  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                      'oauth_timestamp': oauth2.generate_timestamp(),
                      'oauth_token': token,
                      'oauth_consumer_key': consumer_key})
  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()

  #*********

  html = urllib2.urlopen(signed_url)
  readData = html.read()
  rawDict = json.loads(readData)
  rawList = rawDict['businesses']

  print '----' + search + ' (Yelp Rating)----'
  for entry in rawList:
    try:
      print entry['name'], '(', entry['rating'],')'
      print '    ' + str(entry['location']['display_address'][0])
    except:
      continue

#----MAIN----
postDate = ''
postList = []

#load url until date changes

for i in range(0,10):
  url = get_url(i)
  parsed = parse_url(url)

  # if first run, postDate is null, pull postDate from post
  # else check if postDate has changed, if so, break
  if postDate == '':
    postDate = parsed.find('h4', class_='ban').text.strip()
  elif postDate != parsed.find('h4', class_='ban').text.strip():
    break

  
  posts = parsed.find_all('p', class_='row') #type(posts) = bs4.element.ResultSet

  for entry in posts: #type(entry) = bs4.element.Tag
    loc_lat, loc_long = find_lat_long(entry)
    
    if loc_lat == '0.000000' or loc_long == '0.000000':
      continue
    else:

      header = find_header(entry)
      title = find_title(entry)
      neighborhood = find_neighborhood(entry)
      post_url = find_postURL(entry)

      print title
      print loc_lat, loc_long
      print header
      print neighborhood
      print post_url
      print ' '


      yelp_search(loc_lat,loc_long,'Bars')
      yelp_search(loc_lat,loc_long,'Pizza')
      yelp_search(loc_lat,loc_long,'Sushi')

      #print food
      print '======================================'
    




