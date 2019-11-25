# pip install beautifulsoap4
# pip install LxmL


from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
        # 네이버 웹툰 > 간떨어지는 동거 제목 가져오기
        data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=699415&weekday=thu")
        soup = BeautifulSoup(data, "lxml")

        cartoon_titles = soup.find_all("td", attrs={"class": "title"})
        for cartoon_title in cartoon_titles:
            title = cartoon_title.find("a").text
            print(title)ㅈ