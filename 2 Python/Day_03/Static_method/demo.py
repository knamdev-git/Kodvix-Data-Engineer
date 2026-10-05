class A : 
    def heyya(self) : 
        return "I am A Class"

class B : 
    def heyya(self) : 
        return "I am B Class"

class C(B,A) : 
    pass



c_obj = C() 

print(c_obj.heyya())