import pyautogui as pag

if __name__ == '__main__':
    pag.moveTo(425.37,duration=1)   #절대위치
    # 더블클릭 하는 방법 1
    # pag.click()
    # pag.click()
    # 더블클릭 하는 방법 2
    # pag.click(clicks=2)
    # 더블클릭 하는 방법 3
    # pag.doubleClick()
    # pag.move(100.200,duration=1)    #상대위치
    # 오른쪽마우스 클릭하는 방법 1
    # pag.rightClick()
    # 오른쪽마우스 클릭하는 방법 2
    pag.click(button="rignt")
    # 마우스 드래그
    pag.drag(0,200,duration=2)