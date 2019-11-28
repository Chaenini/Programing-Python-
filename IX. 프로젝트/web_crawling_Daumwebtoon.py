# pip install beautifulsoap4
# pip install LxmL
from urllib.request import urlopen
import json

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
        # 다음 웹툰 > 취향저격그녀 제목 가져오기
        # with가 끝나면 자동으로 close 해줌
        with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/favorite") as data:
            j = json.loads(data.read())    #httpResponse -> json


        html = "<html><head><meta charset = 'utf-8'></head><body>"

        cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]    # data > webtoon > webtoonEpisodees
        for cartoon_title in cartoon_titles :   #리스트
            title = cartoon_title["title"]  #타이틀 가져오기

            thumbnail = cartoon_title["thumbnailImage"]["url"]

            url = cartoon_title["id"]
            url = "http://webtoon.daum.net/webtoon/viewer/"+str(url)
            html += "<a href='{}'><img src = '{}' />{}</a>".format(url,thumbnail,title)

        html += "</body></html>"

        outputsoup = BeautifulSoup(html, "lxml")    # 내가 생성한 html 문자열을 soup 객체로 만들기
        prettyHtml = str(outputsoup.prettify())     # 예쁘게 html 코드 만들기
        with open("취향저격그녀.html","w",encoding="utf-8") as f :   # html파일 만들기
            f.write(prettyHtml)

























        # html = "<html><head><meta charset = 'utf-8'></head><body>"
        # cartoon_titles = soup.find_all("td", attrs={"class": "title"})  # <td class = "title"> ... </td>
        # for cartoon_title in cartoon_titles:    # cartoon_titles[:2] - 최근꺼 2개만 보기
        #     title = cartoon_title.find("a").text    # <a> text </a> - 텍스트 가져오기
        #     link = cartoon_title.find("a").get("href")  # <a href = ""> text </a> - 테그의 속성값 가져오기
        #     link = "https://comic.naver.com"+link
        #     # print(title)
        #     # print(link)
        #     html += "<a href = '{}'>{}</a><br/>".format(link,title) # <a href = 'link'>title</a>
        # html += "</body></html>"
        # # print(html)
        #
        # outputsoup = BeautifulSoup(html, "lxml")    # 내가 생성한 html 문자열을 soup 객체로 만들기
        # prettyHtml = str(outputsoup.prettify())     # 예쁘게 html 코드 만들기
        # with open("간떨어지는동거.html","w",encoding="utf-8") as f :   # html파일 만들기
        #     f.write(prettyHtml)