import requests as req

data="A1:B2:C3:D4:E5:id3, 1, 3.7, 6, xx, 52.0778N, 106.3571W, 05/17/2022-10:25:43, 323, 1, 43.5, 323, 2, 43.5, 323, 3, 43.5, 323, 4, 43.5, 323, 5, 43.5, 323, 6, 43.5, 323, 7, 43.5, 323, 8, 43.5, 323, 9, 43.5, 323, 10, 43.5, 323, 11, 43.5, 323, 12, 43.5, 323, 13, 43.5, 323, 14, 43.5, 323, 15, 43.5, 323, 16, 43.5, 323, 17, 43.5, 323, 18, 43.5, 323, 19, 43.5, 323, 20, 43.5, 323, 21, 43.5, 323, 22, 43.5, 323, 23, 43.5, 323, 24, 43.5 [1]"
resp = req.post(
    "http://haztrackerapi-env.eba-zdf4njwq.us-west-1.elasticbeanstalk.com/sensor/BlockedSensor/publish", 
    data,
    headers={"Content-Type": "text/plain"})

print(resp.text)