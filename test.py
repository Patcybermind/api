import urllib.request
import json
import requests

# Test GET request 1
def test_get():
    url = 'http://127.0.0.1:5000/get-sensor-data'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print('GET response:', data)

# Test POST request 2
def test_post():
    url = 'http://127.0.0.1:5000/post-sensor-data'
    data = json.dumps({"key": "test value"}).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    response = urllib.request.urlopen(req)
    response_data = json.loads(response.read())
    print('POST response:', response_data)


# Test image post 3
def test_post_image():

    url = "http://localhost:5000/upload" # api url
    image_path = "image.png"

    with open(image_path, "rb") as img:

        files = {"file": img}
        response = requests.post(url, files=files)
        print(response.text)


# Test image download 4
def test_download_image():
    url = "http://localhost:5000/download"
    response = requests.get(url)
    with open("downloaded_image.png", "wb") as img:
        img.write(response.content)
        print("Image downloaded successfully")

# test getting the log 5
def test_get_log():
    url = "http://localhost:5000/get-log"
    response = requests.get(url)
    print(response.text)


def test_clear_log():
    url = "http://localhost:5000/clear-log"
    response = requests.delete(url)
    print(response.text)

if __name__ == '__main__':
    #test_get()
    #test_post()
    pass




while True:
    test_to_run = int(input('test to run: '))
    if test_to_run == 1:
        test_get()
    elif test_to_run == 2:
        test_post()
    elif test_to_run == 3:
        test_post_image()
    elif test_to_run == 4:
        test_download_image()
    elif test_to_run == 5:
        test_get_log()
    elif test_to_run == 6:
        test_clear_log()