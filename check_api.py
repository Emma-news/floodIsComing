#import mysecrets
import os
import requests
#from urllib.parse import urlparse
import json


def inqUrl(url):
   response = requests.get(url)
   response.encoding = response.apparent_encoding
   jsonData = None
   if(response.text):
       jsonData = json.loads(response.text)
   return jsonData

def addSubscribeMessageToResults(results=[], name='', url='', full=False):
    gitOrg = os.getenv('GITHUB_OWNER')
    results.append("Subscribe to "+name+" API:")
    results.append("1. Login and 'Subscribe to Test' at "+url)
    results.append("2. Make sure to enter 'Start Free Plan' and press 'Subscribe' - **don't** enter credit card data!") 
    results.append(" ")
    if(full):
        results.append("If it doesn't help, **recheck** the registration and the key entry:") 
        results.append("1. Please register at https://rapidapi.com/auth/sign-up")
        results.append("2. Copy your API key from (**X-RapidAPI-Key**) from the [same site]("+url+")")
        results.append("3. Assign the API key as (new?) organization secret or edit it at https://github.com/organizations/"+gitOrg+"/settings/secrets/actions")       
        results.append("   * Name:  **RAPIDAPI_KEY** ")
        results.append("   * Value: **Your key here** ") 
    return True

## NOT WORKING ANY MORE -> TIMEOUT, 0% Service Level!!
def inqRapidFreeNews(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    apiKey = os.getenv('RAPIDAPI_KEY')
    results.append("### RapidAPI: Free-News")
    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q":"Klimawandel","lang":"de","page":1,"page_size":"20"}
    headers = {
        'x-rapidapi-key': apiKey,
        'x-rapidapi-host': "free-news.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.encoding = response.apparent_encoding
    print(response.text)
    print(response.status_code)     #200
    #504 : The request to the API has timed out
    if((response.text) and (not response.status_code in [204, 500, 504])):
        results.append(":white_check_mark: Free-News respone fine")
        text = response.text
        if(not isinstance(text,str)):
            text = text.decode("utf-8")
        jsonData = json.loads(text)
        if('message' in jsonData):
          if('You are not subscribed to this API.'==jsonData['message']):
            results.append(":no_entry: **Not** subscribed to Free-News")
            addSubscribeMessageToResults(results, "Free-News", "https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/free-news")
            return False
        if (('status' in jsonData) and ('ok'==jsonData['status'])):
          results.append(":white_check_mark: Free-News status fine")
          if (jsonData['total_hits']>0):
            results.append(":white_check_mark: Free-News results found")
            return True
          else: 
            results.append(":no_entry: Free-News results **not** found")
            results.append("Maybe retry later...?") #?
            return False
        else:
          results.append(":no_entry:  Free-News status **failed**:")
          addSubscribeMessageToResults(results, "Free-News", "https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/free-news")
          return False
    else:
      results.append(":no_entry: Free-News respone **failed**") 
      results.append("Maybe retry later...?") #?
      return False
    return False

def inqRapidNewsApi14(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    apiKey = os.getenv('RAPIDAPI_KEY')
    results.append("### RapidAPI: News-API-14")
    url = "https://free-news.p.rapidapi.com/v2/search/articles"
    querystring = {"query":"Klimawandel","language":"de","limit":"20"}
    headers = {
        'x-rapidapi-key': apiKey,
        'x-rapidapi-host': "news-api14.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.encoding = response.apparent_encoding
    print(response.text)
    print(response.status_code)     #200
    #504 : The request to the API has timed out
    if((response.text) and (not response.status_code in [204, 500, 504])):
        results.append(":white_check_mark: News-API-14 respone fine")
        text = response.text
        if(not isinstance(text,str)):
            text = text.decode("utf-8")
        jsonData = json.loads(text)
        if('message' in jsonData):
          if('You are not subscribed to this API.'==jsonData['message']):
            results.append(":no_entry: **Not** subscribed to News-API-14")
            addSubscribeMessageToResults(results, "News-API-14", "https://rapidapi.com/bonaipowered/api/news-api14")
            return False
        if (('success' in jsonData) and jsonData['success']):
          results.append(":white_check_mark: News-API-14 status fine")
          if (jsonData['totalHits']>0):
            results.append(":white_check_mark: News-API-14 results found")
            return True
          else: 
            results.append(":no_entry: News-API-14 results **not** found")
            results.append("Maybe retry later...?") #?
            return False
        else:
          results.append(":no_entry: News-API-14 status **failed**:")
          addSubscribeMessageToResults(results, "News-API-14", "https://rapidapi.com/bonaipowered/api/news-api14")
          return False
    else:
      results.append(":no_entry: News-API-14 respone **failed**") 
      results.append("Maybe retry later...?") #?
      return False
    return False

def inqRapidGoogleNews22(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    apiKey = os.getenv('RAPIDAPI_KEY')
    results.append("### RapidAPI: Google-News-22")
    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q":"Klimawandel","language":"de","country":"de"}
    headers = {
        'x-rapidapi-key': apiKey,
        'x-rapidapi-host': "google-news22.p.rapidapi.com"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response.encoding = response.apparent_encoding
    print(response.text)
    print(response.status_code)     #400
    #504 : The request to the API has timed out
    if((response.text) and (not response.status_code in [204, 500, 504])):
        results.append(":white_check_mark: Google-News-22 respone fine")
        text = response.text
        if(not isinstance(text,str)):
            text = text.decode("utf-8")
        jsonData = json.loads(text)
        if('message' in jsonData):
          if('You are not subscribed to this API.'==jsonData['message']):
            results.append(":no_entry: **Not** subscribed to Google-News-22")
            addSubscribeMessageToResults(results, "Google-News-22", "https://rapidapi.com/bonaipowered/api/google-news22", True)
            return False
        if (('success' in jsonData) and jsonData['success']):
          results.append(":white_check_mark: Google-News-22 status fine")
          if (('total' in jsonData) and (jsonData['total']>0)):
            results.append(":white_check_mark: Google-News-22 results found")
            return True
          else: 
            results.append(":no_entry: Google-News-22 results **not** found")
            results.append("Maybe retry later...?") #?
            return False
        else:
          results.append(":no_entry:  Google-News-22 status **failed**:")
          addSubscribeMessageToResults(results, "Google-News-22", "https://rapidapi.com/bonaipowered/api/google-news22", True)
          return False
    else:
      results.append(":no_entry: Google-News-22 respone **failed**") 
      addSubscribeMessageToResults(results, "Google-News-22", "https://rapidapi.com/bonaipowered/api/google-news22", True)
      return False
    return False


def checkRapidAPI(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    apiKey = os.getenv('RAPIDAPI_KEY')
    results.append("### RapidAPI")
    apiKeyExists = True
    if(apiKey):
      if(apiKey == '1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t1u2v3w4x5y'):
        apiKeyExists = False
    else:
        apiKeyExists = False      
    if(not apiKeyExists): 
        results.append(":no_entry: RapidAPI key **missing**:")
        results.append("1. Please register at https://rapidapi.com/auth/sign-up")
        results.append("2. Login and 'Subscribe to Test' at https://rapidapi.com/bonaipowered/api/google-news22")
        results.append("3. Make sure to enter 'Start Free Plan' and press 'Subscribe' - **don't** enter credit card data!")
        results.append("2. Copy your API key from (**X-RapidAPI-Key**) from the same site")
        results.append("3. Assign the API key as new organization secret at https://github.com/organizations/"+gitOrg+"/settings/secrets/actions/new")       
        results.append("   * Name:  **RAPIDAPI_KEY** ")
        results.append("   * Value: **Your key here** ") 
        return False    
    else:
        results.append(":white_check_mark: RapidAPI key exists")
        return True 
    return False

def inqNewsApi(results=[]):
  apiKey = os.getenv('NEWSAPI_KEY')
  url = ('https://newsapi.org/v2/everything?q=Klimawandel&language=de&apiKey='+apiKey)
  response = requests.get(url)
  response.encoding = response.apparent_encoding
  if(response.text):
    results.append(":white_check_mark: NewsAPI respone fine") 
    jsonData = json.loads(response.text)
    if ('ok'==jsonData['status']):
      results.append(":white_check_mark: NewsAPI status fine")
      if(jsonData['totalResults']>0):
         results.append(":white_check_mark: NewsAPI results found")
         return True
      else:
         results.append(":no_entry: NewsAPI results **not** found")
         return False
    else:
      results.append(":no_entry: NewsAPI status **failed**:")
      results.append("Please recheck the API key and its assignment:")
      results.append("1. Please register at https://newsapi.org/register")
      results.append("2. Login and get your API key at https://newsapi.org/account")
      results.append("3. Assign the API key as new organization secret at https://github.com/organizations/"+gitOrg+"/settings/secrets/actions/new") 
      results.append("   * Name:  **NEWSAPI_KEY** ")
      results.append("   * Value: **Your key here** ")          
      return False
  else:
    results.append(":no_entry: NewsAPI respone failed") 
    results.append("Please recheck the API key and its assignment:")
    results.append("1. Please register at https://newsapi.org/register")
    results.append("2. Login and get your API key at https://newsapi.org/account")
    results.append("3. Assign the API key as new organization secret at https://github.com/organizations/"+gitOrg+"/settings/secrets/actions/new") 
    results.append("   * Name:  **NEWSAPI_KEY** ")
    results.append("   * Value: **Your key here** ")          
    return False
  return False

def checkNewsApi(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    apiKey = os.getenv('NEWSAPI_KEY')
    results.append("### NewsAPI")
    apiKeyExists = True
    if(apiKey):
      if(apiKey == '1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7'):
        apiKeyExists = False
    else:
        apiKeyExists = False      
    if(not apiKeyExists): 
        results.append(":no_entry: NewsAPI key **missing**:")
        results.append("1. Please register at https://newsapi.org/register")
        results.append("2. Login and get your API key at https://newsapi.org/account")
        results.append("3. Assign the API key as new organization secret at https://github.com/organizations/"+gitOrg+"/settings/secrets/actions/new")       
        results.append("   * Name:  **NEWSAPI_KEY** ")
        results.append("   * Value: **Your key here** ") 
        return False    
    else:
        results.append(":white_check_mark: NewsAPI key exists")
        inqNewsApi(results) 
        return True 
    return False

def checkGithubOrganization(results=[]):
    gitOrg = os.getenv('GITHUB_OWNER')
    gitRepo = os.getenv('GITHUB_REPO')
    #print(['Org',gitOrg,'Repo',gitRepo])
    results.append("### Github Organization")
    if(gitOrg):
      orgData = inqUrl('https://api.github.com/users/'+gitOrg)
      #print(orgData)    # check for 'type': 'Organization', 'user_view_type': 'public'
      if(not 'Organization'==orgData['type']):
        results.append(":no_entry: Github Organization **missing**:")   

        results.append("1. Please")
        results.append("2. Logt")
        results.append("3. Assifgn")
        return (True, False) 
      else:
        results.append(":white_check_mark: Github Organization exists") 
        orgAssigned = False
        myOrgs = inqUrl('https://api.github.com/users/KMicha/orgs')
        #print(myOrgs) 
        for org in myOrgs:
          if(org['id']==orgData['id']):
            orgAssigned = True
        if(orgAssigned):
          results.append(":white_check_mark: Github Organization assigned") 
          return (True, True)  
        else:
          results.append(":no_entry: Github Organization **not** assigned (or not public):")
          results.append("1. Please")
          results.append("2. Logt")
          results.append("3. Assifgn KMicha")  
          return (True, True)
    else:
      results.append("No check possible: maybe running locally?") 
      return (False, False)
    return (True, True) 

results=[]
(runOnGithub, runInOrganization) = checkGithubOrganization(results)
results.append("\n---\n")
if(runInOrganization):
  checkNewsApi(results)
  results.append("\n---\n")
  rapidAPIExists = checkRapidAPI(results)
  results.append("\n---\n")
  if(rapidAPIExists):
    inqRapidGoogleNews22(results)
    #inqRapidFreeNews(results)
    inqRapidNewsApi14(results)
    results.append("\n---\n")
    
#print(results)

if(runOnGithub):
  f = open("CHECK.md", "w")
  for res in results:
    f.write(res+"  \n")
  f.close()


