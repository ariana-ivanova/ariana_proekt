start=0
ugol=0  #угол сек
ugol2=0 #угол мин
ugol3=0 #угол час
frame_sec=50 #кадров на секунду     1- час  5- мин  50-обычно

def setup():
    size(600, 600)
def draw():
    global ugol,ugol2,ugol3,frame_sec,start
    
    background(136,250,114)
    if start == 0 :
        ugol=0  
        ugol2=0 
        ugol3=0
    #if start == 1 :
        
        
        
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
    translate(300,300)
    rotate(radians(ugol))
    line(0,0,0,-200)    #сек
    if frameCount%frame_sec== 0 :
        ugol+=6
    pop()
    
    push()
    strokeWeight(6)
    translate(300,300)
    rotate(radians(ugol2))
    line(0,0,0,-160)    #мин
    if frameCount%(frame_sec*10)== 0 :
        ugol2+=1
    pop()
    
    push()
    strokeWeight(8)
    translate(300,300)
    rotate(radians(ugol3))
    line(0,0,0,-120)    #час
    if frameCount%(frame_sec*10*12)== 0 :
        ugol3+=1
    pop()
    
    rect(540,0,60,20)
    push()
    fill(255)
    textSize(22) 
    text(u"start",545,18)
    pop()
    push()
    fill(112,207,252)
    rect(500,500,50,50)
    
    fill(112,207,252)
    rect(50,500,50,50)
    
    fill(112,207,252)
    rect(50,50,50,50)
    pop()
    fill(0)
    text(u"ч",510,536)
    text(u"м",57,536)
    text(u"с",57,86)
    
    
def mouseClicked():
    global ugol,ugol2,ugol3,frame_sec,start
    if mouseX > 500 and mouseX < 550 and mouseY > 500 and mouseY < 550:
        ugol3+=30
    if mouseX > 50 and mouseX < 100 and mouseY > 500 and mouseY < 550:
        ugol2+=10
    if mouseX > 50 and mouseX < 100 and mouseY > 50 and mouseY < 100:
        ugol+=6
        
    if mouseX > 540 and mouseX < 600 and mouseY > 0 and mouseY < 20:    
        start = 1
        
        
