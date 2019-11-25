# pip install beautifulsoap4
# pip install LxmL


from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__' :
        # 네이버 웹툰 > 간떨어지는 동거 제목 가져오기
        data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=699415&weekday=thu")
        soup = BeautifulSoup(data, "lxml")  # httpResponse -> HTML

        html = "<html><head><meta charset = 'utf-8'></head><body>"
        cartoon_titles = soup.find_all("td", attrs={"class": "title"})  # <td class = "title"> ... </td>
        for cartoon_title in cartoon_titles:    # cartoon_titles[:2] - 최근꺼 2개만 보기
            title = cartoon_title.find("a").text    # <a> text </a> - 텍스트 가져오기
            link = cartoon_title.find("a").get("href")  # <a href = ""> text </a> - 테그의 속성값 가져오기
            link = "https://comic.naver.com"+link
            # print(title)
            # print(link)
            html += "<a href = '{}'>{}</a><br/>".format(link,title) # <a href = 'link'>title</a>
        html += "</body></html>"
        # print(html)

        with open("간떨어지는동거.html","w",encoding="utf-8") as f :   # html파일 만들기
            f.write(html)