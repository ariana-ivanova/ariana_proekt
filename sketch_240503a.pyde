q=300
w=100
a=300
s=140
z=300
x=180

def setup():
    size(600, 600)
def draw():
    global q,w,a,s,z,x
    background(136,250,114)
   # ellipse(300,300, 500, 500)
    textSize(60)
    push()
    fill(0)
    text(u"12",260,110)
    pop()
    
    push()
    fill(0)
    text(u"1",390,140)
    pop()
    
    push()
    fill(0)
    text(u"2",465,220)
    pop()
    
    push()
    fill(0)
    text(u"3",500,310)
    pop()
    
    push()
    fill(0)
    text(u"4",480,400)
    pop()
    
    push()
    fill(0)
    text(u"5",400,490)
    pop()
    
    push()
    fill(0)
    text(u"6",280,530)
    pop()
    
    push()
    fill(0)
    text(u"7",180,500)
    pop()
    
    push()
    fill(0)
    text(u"8",100,430)
    pop()                                            
    
    push()
    fill(0)
    text(u"9",80,330)
    pop() 
    
    push()
    fill(0)
    text(u"10",80,230)
    pop() 
    
    push()
    fill(0)
    text(u"11",140,150)
    pop() 
    
    push()
    strokeWeight(3)
    line(300,300,q,w)    #сек
    if frameCount%5== 0 :
        q+=1
        w+=1
    if q >= 490:
        q -=1
    if q >= 470:
        q -=1   
    if q >= 390:
        q -=1    
        
    if q >= 270:
        q -=1
    if q >= 170:
        q -=1   
    if q >= 90:
        q -=1    
    if q >= 70:
        q -=1
    if q >= 70:
        q -=1   
    if q >= 130:
        q -=1     
           
            
             
              
                
        
    pop()

    push()
    strokeWeight(6)
    line(300,300,a,s)    #мин
    if frameCount%60== 0 :
        a+=1
        s+=1
    
    
    pop()
    
    push()
    strokeWeight(8)
    line(300,300,z,x)    #час
    
    
    
    pop()
