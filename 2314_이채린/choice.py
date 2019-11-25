from urllib.parse import urlunparse, urlparse
from tutorial import Tutorial
from schoolFileReader import SchoolFileReader

class Choice:



    def choice(self) :

            name = input("이름을 입력해주세요 : ")
            age = input("나이를 입력해주세요 : ")

            f = open("data.txt", 'w')
            f.write(name + "   ")
            f.write(age + "   ")

            print("\n")
            print("안녕하세요 ! " + name + "님의 고등학교 진학을 도와드릴 '학교가고' 프로그램 입니다 :) ! ")
            print("\n")


            t = Tutorial()
            t.tutorial()

            arr = ["1. 컴퓨터 코딩","2. 회계 및 전산","3. 디자인","4. 조리 및 식품","5. 기계","6. 과학","7. 항공정비 및 항공서비스","8. 동물","9. 농사","10. 뷰티"]
            school = ["미림여자정보과학고등학교","서울여자상업고등학교","서울디자인고등학교","서울조리고등학교","수도전기공업고등학교","서울과학고등학교","강호항공고등학교","광주자연과학고등학교","충주농업고등학교","한국뷰티고등학교"]
            url = ['https://www.e-mirim.hs.kr/main.do', "http://sys.sen.hs.kr/index.do", "http://seodi.sen.hs.kr/51522/subMenu.do","http://kcas.hs.kr/", "http://sudo.sen.hs.kr/index.do", "http://sshs.hs.kr/index.do","http://school.jbedu.kr/kangho", "http://kns.hs.kr/main/main.php", "http://school.cbe.go.kr/cjagh-h","http://kbeauty.jje.hs.kr/"]

            for i in arr:
                print(i)

            print("원하는 분야의 번호를 입력하세요 : ")

            keyword = input()

            print("▼▽▼▽▼▽▼▽▼▽▼▽▼▽▼▽▼▽▼▽▼▽▼▽")
            print(arr[(int(keyword)-1)])

            print("학교 : "+school[int(keyword)-1])
            print("사이트 : "+url[int(keyword)-1])
            print("▲△▲△▲△▲△▲△▲△▲△▲△▲△▲△▲△▲△")

            f.write(school[int(keyword)-1] + "   ")
            f.write(url[int(keyword)-1] + "   ")
            f.close()