#Calculator

import os

class Calculator():

    
    class parse():  
        
        def __init__(self, line: str):
            self.consNumbers =  ("1","2","3","4","5","6","7","8","9","0")
            self.line = line
            self.addIndex = [] #stores to numberindex of each nunber that is to left + operator
            self.multIndex = [] #stores to numberindex of each nunber that is to left * operator
            self.numbers = [] #stores numbers
            self.temp = [] #Temporary number list
            self.tempc = 0 #Temporary Count        
            
        def get_result(self):
            b = self._start_parse()
            return b     
        
        def _start_parse(self):
            def temp_func(line: str,numbers:list, plus:list, mult:list):
                  
                i = 0
                while i < len(line):
                    item = line[i]
                    if ")" == item:     #5+)2*9( #Tamamen bozuk burası           
                        bracket_numbers = []
                        bracket_add = []
                        bracket_mult = []
                        inside_bracket = ""
                        brackets_count = -1
                        control = False
                        for j in range(i, len(line)):
                            
                            
                            item_br =  line[j]
                            if ")" == item_br:
                                brackets_count += 1
                            elif "(" == item_br and brackets_count > 0:
                                brackets_count -= 1
                            elif "(" ==  line[j] and brackets_count == 0 :
                                if control == False:
                                    c = line[i+1:j]
                                    numbers.append(temp_func(c,bracket_numbers,bracket_mult,bracket_add))
                                    
                                i = j+1
                                break
                        
                                    
                    elif item in self.consNumbers:#?
                        item = int(item) 
                        self.temp.append(item)
                        self.tempc += 1
                        
                        if i == len(line)-1:
                            x = self.reverse_temp()
                           
                            numbers.append(x)
                            
                            tempc = 0
                            self.temp.clear()
                        i+=1
                    elif item == "+": 
                        i+=1
                        if self.tempc > 0:
                            
                            x = self.reverse_temp()
                            self.ekleme(plus,x, numbers)
                            
                    elif item == "-":
                        i+=1
                        if self.tempc > 0:
                            
                            x = -self.reverse_temp()
                        
                            self.ekleme(plus,x, numbers)
                            
                    elif item == "*": 
                        i+=1
                        if self.tempc > 0:
                            
                            x = self.reverse_temp()
                        
                        self.ekleme(mult,x, numbers)
                        
                    elif item == "/":
                        i+=1
                        if self.tempc > 0:
                            
                            x = 1/self.reverse_temp()
                            
                            self.ekleme(mult,x, numbers)
                             
                    else :
                        return 0
                        # Current index : i
                        # Begin index : index
                        # Temporary i =  tempI                            
                        #inside bracket is a new line of input        
                
                    
                result = 0
                if len(mult) > 0 :                
                    n = len(mult)-1
                    while n >= 0:
                    
                        if mult[n] >= len(numbers):
                            return 0
                        else:
                            numbers[mult[n]-1] *= numbers[mult[n]]
                            numbers[mult[n]] = 0  
                        n -= 1
                    
                if len(numbers) > 1:
                     result = sum(numbers)      
                elif len(numbers) > 1 and numbers.count(0) == len(numbers)-1 :
                    result = numbers[0]
                
                numbers.clear()
               
                return result
            
            
            
            return temp_func(self.line,self.numbers,self.multIndex,self.addIndex)
        
        

        
        def reverse_temp(self):#reverse temp and extrac items from temp list
            self.temp = self.temp[::-1]
         
            lenght_temp = len(self.temp)
            if lenght_temp > 1:
                number = ""
                for i in range(lenght_temp):
                    number = number + str(self.temp[i])
                return int(number) 
            elif lenght_temp == 1: 
                return self.temp[0]
            elif lenght_temp == 0:
                return 
        def ekleme(self, operator_list: list, x, numbers: list):
            if x != None:
                numbers_lenght = len(numbers)
                numbers.append(x)
                operator_list.append(numbers_lenght+1)
                self.tempc = 0
            elif x == None:
                numbers_lenght = len(numbers)
              
                operator_list.append(numbers_lenght)
                
                self.tempc = 0
            self.temp.clear()
    
    

    def __init__(self):
        pass
    def start(self):
        print("---------Calculator---------")
        a = ""
        while True:#Ya her şeyi silecek baştan işlem yapacak ya da programdan çıkacak
            self.line = str(a)
            b = str(input(f" = {a}"))    
            if b == "c": #clear
                os.system('cls||clear')
            elif b == "q":
                break
            else :
                self.line = str(a)+b
                self.line = self.reversed_line()
                result = self.parse(self.line)
                a = result.get_result()
            #en son bir işlem yapıp devam edebilir işlemlere sonuç üzerinden
            
        print("--------------------------")
  
    
    def reversed_line(self):
        return self.line[::-1]

    def end(self):
        return 
if "__main__" == __name__:
    cal = Calculator()
    cal.start()