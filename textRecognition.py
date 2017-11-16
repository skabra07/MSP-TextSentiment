"""Docstring."""
import http.client, urllib.request, urllib.parse, urllib.error, base64,json
import json

# libray made by Suyash Kabra.
def makeRequest(text):
    passage = text.split('\n')
    maxCount = 1300
    ids=[]
    x = 0
    while True:
        count = 0
        texts = ''
        while(count + len(passage[x]) < maxCount):
            texts = texts + passage[x]
            count = count + len(passage[x])
            x= x+1
            if(x == len(passage)):
                break
        ids.append(texts)
        if(x == len(passage)):
            break
    sizeOfId = len(ids)
    input_texts = '{"documents":['
    for y in range(0,sizeOfId):
        input_texts = input_texts +  '{"language": "en","id":"' + str(y)+ '","text":"' + ids[y].replace('"','') + '"},'

    input_texts = input_texts[:-1] + ']}'
    return input_texts,sizeOfId

def recognition(text):
    api= 'a209a75828954939bb43d0ecaf194f96'
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api,
    }

    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, text.encode('utf-8'), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def getScore(text,size):
    scores = []
    for sentiment_analysis in text['documents']:
        scores.append(sentiment_analysis['score'])
    avg = 0
    for score in scores:
        avg = avg + score
    return avg / size

def text_sentiment(text):
    input_texts,size = makeRequest(text)
    results = recognition(input_texts)
    results = json.loads(results.decode("utf-8"))
    score = getScore(results,size)
    return score
