#order
class Order:
    _drinks = [Coffee("아메리카노",1800),BubbleTea("하동녹차오레오", 3900)]

    def __init__(self):
        self.order_menu = []

    def show_menu(self):
        print("0: 아메리카노 1800원, 1: 하동녹차오레오 3900원")
    
    def order_drink(self):

        while True:
            #show menu
            self.show_menu()

            #주문받기, 음료선택하기
            order = input("무엇을 고르시겠습니까? ")
            drink = Order._drinks[int(order)]
            if order == "":
                break

            #음료 옵션선택하기
            drink.order()

            self.order_menu.append(drink)
        
        #주문한 음료 내용 보여주기
        for d in self.order_menu:
            print(d)

        #합계 금액 보여주기
        print("총금액: "+str(self.sum_price())+"원")
        
    def sum_price(self):
        sum = 0
        for d in self.order_menu:
            sum += d.price

        return sum