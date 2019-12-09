import pyautogui as pag
import time

if __name__ == '__main__' :
    # 크롬 이미지 인식
    # 배경이 단색일 경우 아이콘이 어디에 있던지 인식가능
    img = pag.locateOnScreen("chrom_icon.PNG")
    print(img)
    # 가운데 좌표 찾기
    center = (img.left+(img.width/2),img.top+(img.height/2))
    # 마우스 이동
    pag.moveTo(center,duration=2)
    # 더블클릭릭
    pag.doubleClick()

    # imgs = pag.locateOnScreen("chrom_icon.PNG")
    # for img in imgs :
    #     print(img)
    #     center = pag.center(img)
    #     pag.moveTo(center,duration=1)