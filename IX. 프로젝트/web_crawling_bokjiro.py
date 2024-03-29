
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

if __name__ == '__main__':
        url = "http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
        data = {"searchIntClId":"03","pageUnit":"200"}
        with requests.post(url, data=data) as response:
                soup = BeautifulSoup(response.text, "lxml")

        benefits = soup.select("dt.tit > a")

        for benefit in benefits:
                 print(benefit.text)