#Calculator

import time

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
            def temp_func(line):
              
                i = 0
                while i < len(line):
                    item = line[i]
                 
                   
                  
                    
                    if ")" == item:     #5+)2*9( #Tamamen bozuk burası           
                       
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
                                    print(c)
                                    self.numbers.append(temp_func(c))
                                    
                                i = j+1
                                break
                        
                                    
                    elif item in self.consNumbers:#?
                        item = int(item) 
                        self.temp.append(item)
                        self.tempc += 1
                        
                        if i == len(line)-1:
                            x = self.reverse_temp()
                           
                            self.numbers.append(x)
                            
                            tempc = 0
                            self.temp.clear()
                        i+=1
                    elif item == "+": 
                        i+=1
                        if self.tempc > 0:
                            
                            x = self.reverse_temp()
                            self.ekleme(self.addIndex,x)
                            
                    elif item == "-":
                        i+=1
                        if self.tempc > 0:
                            
                            x = -self.reverse_temp()
                        
                            self.ekleme(self.addIndex,x)
                            
                    elif item == "*": 
                        i+=1
                        if self.tempc > 0:
                            
                            x = self.reverse_temp()
                        
                        self.ekleme(self.multIndex,x)
                        
                    elif item == "/":
                        i+=1
                        if self.tempc > 0:
                            
                            x = 1/self.reverse_temp()
                            
                            self.ekleme(self.multIndex,x)
                             
                    else :
                        return 0
                        # Current index : i
                        # Begin index : index
                        # Temporary i =  tempI                            
                        #inside bracket is a new line of input        
                
                    
                result = 0
               
               
               
                if len(self.multIndex) > 0 :                
                    n = len(self.multIndex)-1
                    while n >= 0:
                    
                        if self.multIndex[n] >= len(self.numbers):
                            return 0
                        else:
                            self.numbers[self.multIndex[n]-1] *= self.numbers[self.multIndex[n]]
                            self.numbers[self.multIndex[n]] = 0
                           
                            
                        n -= 1
                    
                if len(self.numbers) > 1:
                  
                     result = sum(self.numbers)      
                else :
                    result = self.numbers[0]
                
                self.numbers.clear()
               
                return result
            
            
            
            return temp_func(self.line)
        
        

        
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
        def ekleme(self, operator_list: list, x):
            if x != None:
                numbers_lenght = len(self.numbers)
                self.numbers.append(x)
                operator_list.append(numbers_lenght+1)
                self.tempc = 0
            elif x == None:
                numbers_lenght = len(self.numbers)
                if operator_list == self.multIndex:
                    x = 1
                    self.numbers.append(x)
                elif operator_list == self.addIndex:
                    x = 0
                    self.numbers.append(x)
              
                operator_list.append(numbers_lenght+1)
                
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
            self.line = str(a)+b
            self.line = self.reversed_line()
            result = self.parse(self.line)
            a = result.get_result()
            #en son bir işlem yapıp devam edebilir işlemlere sonuç üzerinden
    
  
    
    def reversed_line(self):
        return self.line[::-1]

    def end(self):
        return 
if "__main__" == __name__:
    cal = Calculator()
    cal.start()