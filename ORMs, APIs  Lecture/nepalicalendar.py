
import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=5221032e999efc59769fe8b56f46b146&symbols=USD,AUD,CAD,PLN,NPR&format=1")
    if res.status_code != 200:
        raise Exception("errer")
    data=res.json()
    print(data)
if __name__ =="__main__":
    main()