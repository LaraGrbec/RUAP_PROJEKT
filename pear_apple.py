import requests, json
from requests.auth import HTTPBasicAuth
data = {
    "urls": ["http://localhost/images/slika.jpg"], \
    "modelId":"be05fe90-40fd-42e9-8f77-1bb18b2d796a"
}

headers = {
    'accept': 'application/x-www-form-urlencoded'
}


url = "https://app.nanonets.com/api/v2/ImageCategorization/LabelUrls/"
r = requests.post(url, headers=headers, data=data, verify=False, auth=HTTPBasicAuth('K_AAbygpXX05Bp8BojnENlhUw69_a0HWMfkrmo0S9BJ', ''))
print r.content
parsed = json.loads(r.content)
print json.dumps(parsed, indent=4, sort_keys=True)

if parsed["result"][0]["prediction"][0]["probability"] < 0.5:
	print "kruska"
else:
	print "jabuka"
