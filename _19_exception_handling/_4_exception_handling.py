class demo:
    def divide(self):
        div = 0
        no1 = int(input("Enter no1 : "))
        no2 = int(input("Enter no2 : "))
        try:
            div = no1 / no2    
        except:
            pass
        print("Division : ",div)
        print("End of program")

    def division(self):
        self.divide()
        
if __name__ == "__main__":
    obj = demo()
    obj.division()
