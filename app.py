import requests
## This is a simple Python application that makes a GET request to the httpbin.org API
def main():
    response = requests.get("https://httpbin.org/get")
    print(response.json())

if __name__ == "__main__":
    main()
