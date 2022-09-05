import math,random,time
from pyray import *
init_window(600, 600, "Maurer Rose")
n,d = random.randint(2,100),random.randint(2,100)
tx,ty = 300,300
c = Color(random.randint(100,255),random.randint(100,255),random.randint(100,255),255)
while not window_should_close():
    set_target_fps(60)
    draw_fps(10,10,10)
    draw_text("Press \"r\" to reset",10,35,20,LIME)
    begin_drawing()
    clear_background(Color(0,0,0,0))
    for theta in range(361):
        k = theta * d * math.pi / 180
        r = 300 * math.sin(n * k)
        x = r * math.cos(k)
        y = r * math.sin(k)
        x += 300
        y += 300
        draw_line(int(tx),int(ty),int(x),int(y),c)
        tx,ty = x,y
    if is_key_pressed(KEY_R):
        n,d = random.randint(2,100),random.randint(2,100)
        tx,ty = 300,300
        c = Color(random.randint(100,255),random.randint(100,255),random.randint(100,255),255)
    
    

        

    
    end_drawing()
close_window()

