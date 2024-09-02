import http.client
import urllib.parse
import json

class GuthubIntegration:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        parsedUrl = urllib.parse.urlparse(self.baseUrl)
        self.host = parsedUrl.netloc
    
    def getUserInformation(self, username):
        userBaseUrl = f"/users/{username}/events"
        
        try:
            conn = http.client.HTTPSConnection(self.host)
            # Add header to request
            headers = {
                "User-Agent": "MyApp/1.0",
                'Content-type': 'application/json'
            }
            conn.request("GET", userBaseUrl, headers=headers)
            response = conn.getresponse()
            if response.status == 200:
                data = response.read()
                json_data = json.loads(data.decode())
                return json_data
            else:
                print(f"Error: {response.status} {response.reason}")
        except http.client.HTTPException as e:
            print("HTTP Exception:", e)
        except Exception as e:
            print(f"Something happened: {e}")
        finally:
            conn.close()