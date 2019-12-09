import pyautogui as pag
import time

if __name__ == '__main__' :
    # 메모장 실행
    pag.moveTo(457, 1061,2)
    pag.doubleClick()
    # Hello World 입력
    pag.moveTo(200,200,2)
    pag.typewrite("Hello World")
    # enter 두번
    pag.press("enter")
    pag.press("enter")
    # 반갑구나 세상아 입력
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk") # 반갑구나 세상아
    pag.press("hangul")
    # 저장
    pag.hotkey('ctrl', 's')
    time.sleep(1)
    # 파일 이름 = python_world
    pag.typewrite("python_world")
    # pag.typewrite("C\\Users\\CHAENINI\\Downloads\\") - 지정 위치에 저장
    pag.press("enter")