import json
import requests
# Rtoken="1//0gl2SBXHdKuh7CgYIARAAGBASNwF-L9IrD5fk-1wPEDm1Rk4CuDCtomJDqneeuFDoWZ-I4IB_HUoILTFuyVChTXSEm4miX7-2DlQ"
url="https://www.googleapis.com/drive/v2/files"
TOKEN="ya29.a0AfH6SMC13KYfW6N7WPGT4JusYQapa6revdmanjvw6rl3Qn2qGiRXVltXdk94hAdeBFB88yympzAkvSawQVZVnI9ZcETZogu9Rvxo3a8B8frSHETT8rN0BK5KYBNyJ33hUGJ1w1cvaEQzCBhwdMKOfYpJY0z9"
newHeaders = {'Content-type': 'application/json', "Authorization": "Bearer %s" %TOKEN}
response = requests.get(url, headers=newHeaders)
data=response.json()
G_DATA=json.dumps(data, sort_keys=True, indent=4)
print(G_DATA)

# from oauthlib.oauth2 import BackendApplicationClient
# from requests_oauthlib import OAuth2Session
#
# client = BackendApplicationClient(client_id="1019872970781-74brh74imnrasv3ef7a9vc5hdacqi465.apps.googleusercontent.com")
# oauth = OAuth2Session(client=client)
# code= "4/0AY0e-g7Ktfy47A7gNViMEQBM_S6K7YXEQkFh_ufBpEQoEp7s6NEyi058SMmbNFBebPxMLQ"
# client_id ="1019872970781-74brh74imnrasv3ef7a9vc5hdacqi465.apps.googleusercontent.com"
# client_secret= "_kISvDn7uWGIqDsMY0q2OyfQ"
# redirect_uri= "http://127.0.0.1:8000/",
# # gt="authorization_code"
# token = oauth.fetch_token(token_url='https://oauth2.googleapis.com/token',
#                           client_id=client_id,
#                           client_secret=client_secret,
#                           scope="https://www.googleapis.com/auth/drive.readonly",
#                           code=code,
#                           headers={"grant_type":"authorization_code","redirect_uri":"http://127.0.0.1:8000/",'Content-type': 'application/x-www-form-urlencoded'}
#                           # redirect_uri=redirect_uri
#                           )
#
# print(token)

# header = {'Content-type': 'application/x-www-form-urlencoded'}
#
# payload='grant_type=client_credentials&code=4/0AY0e-g7Ktfy47A7gNViMEQBM_S6K7YXEQkFh_ufBpEQoEp7s6NEyi058SMmbNFBebPxMLQ&redirect_uri=http://127.0.0.1:8000/&client_secret=_kISvDn7uWGIqDsMY0q2OyfQ&client_id=1019872970781-74brh74imnrasv3ef7a9vc5hdacqi465.apps.googleusercontent.com'
#
# url = 'https://oauth2.googleapis.com/token'
#
# response = requests.post(url, data=payload, headers=header, verify=False)
# print(response.json())
# params = {
# "code" :"4/0AY0e-g7Ktfy47A7gNViMEQBM_S6K7YXEQkFh_ufBpEQoEp7s6NEyi058SMmbNFBebPxMLQ",
# "client_id": "1019872970781-74brh74imnrasv3ef7a9vc5hdacqi465.apps.googleusercontent.com",
# "client_secret" : "_kISvDn7uWGIqDsMY0q2OyfQ",
# "redirect_uri" : "http://127.0.0.1:8000/",
# "grant_type":"authorization_code"
# }
# url = "https://oauth2.googleapis.com/token"
# response = requests.post(url,params)
# print(response.status_code == 200)
# print(response.json())
# result = json.loads(response.text)


# import http.client
#
# conn = http.client.HTTPSConnection("")
#
# payload = "grant_type=authorization_code&" \
#           "client_id=1019872970781-74brh74imnrasv3ef7a9vc5hdacqi465.apps.googleusercontent.com&" \
#           "client_secret=_kISvDn7uWGIqDsMY0q2OyfQ&" \
#           "code=4/0AY0e-g7Ktfy47A7gNViMEQBM_S6K7YXEQkFh_ufBpEQoEp7s6NEyi058SMmbNFBebPxMLQ&"
#
# headers = { 'content-type': "application/x-www-form-urlencoded" }
#
# conn.request("POST", "https://accounts.google.com/o/oauth2/token", payload, headers)
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))
#



# import adal
# import requests
#
# url = "https://oauth2.googleapis.com/token"
#
# headers = {"code" :"4/0AY0e-g7Ktfy47A7gNViMEQBM_S6K7YXEQkFh_ufBpEQoEp7s6NEyi058SMmbNFBebPxMLQ",
# "client_id": "1019872970781-74brh74imnrasv3ef7a9vc5hdacqi465.apps.googleusercontent.com",
# "client_secret" : "_kISvDn7uWGIqDsMY0q2OyfQ",
# "redirect_uri" : "http://127.0.0.1:8000/",
# }
#
# # newHeaders = {'Content-type': 'application/json', "Authorization": "Bearer %s" % token["accessToken"]}
# response = requests.post(url, headers=headers, verify=False)
# data = response.json()
# print(data)
