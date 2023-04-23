class Numbers():
    def __init__(self,ch):
        self.ch = ch

    def kratn(self):
        rez2 = "False"
        rez3 = "False"
        rez4 = "False"
        rez_vsex = "False"
        
        if self.ch%2 == 0:
            rez2 = "True"
            
        if self.ch%3 == 0:
            rez3 = "True"
            
        if self.ch%4 == 0:
            rez4 = "True"
            
        if (self.ch%2 == 0)  and (self.ch%3 == 0)  and (self.ch%4 == 0) :
            rez_vsex = "True"
            
        print('    Число:',self.ch)
        print('{:^8}{:^8}{:^8}{:^8}'.format('кратно: 2 ',' кратно: 3 ',' кратно: 4 ',' кратновсему'))
        print('{:^8}{:^7}{:^5}{:^10}{:^5}{:^8}{:^8}'.format(rez2,'|',rez3,'|',rez4,'|',rez_vsex))
        
    def __gt__(self,other):
        
        if self.ch > other.ch:
            return 'Первое число больше второго'
        
        else:
            return 'Первое число не больше второго'
        
    def __ge__(self,other):
        
        if self.ch >= other.ch:
            return 'Первое число больше или равно второго'
        
        else:
            return 'Первое число не больше или равно второго'
        
n1 = Numbers(12)
print(n1.__dict__)
n1.kratn()
n2 = Numbers(10)
print(n2.__dict__)
n2.kratn()
print(n1 > n2)
print(n1 >= n2)

print( )
print(____________________________________________________________________:))
print( )
