#modules
import math,random,time
from pyray import *

#initialize
init_window(600, 600, "Maurer Rose")

#get size of screen and monitor
dx,dy = get_monitor_width(0),get_monitor_height(0)
tx,ty = 600,600
tempx,tempy = tx/2,ty/2
dempx,dempy = dx/2,dy/2

#variables
n,d = random.randint(2,100),random.randint(2,100)
c = Color(random.randint(100,255),random.randint(100,255),random.randint(100,255),255)
memx,memy = tempx,tempy
imgx,imgy = dempx,dempy

#set fps
set_target_fps(60)

#image
img = gen_image_color(dx,dy,BLACK)

#main loop
while not window_should_close():
    
    #help texts
    draw_fps(10,10,10)
    draw_text("Press \"r\" to randomize \n \"s\" to save \n \"a\" to auto save 10 pictures",10,35,10,LIME)

    #drawing 
    begin_drawing()
    clear_background(Color(0,0,0,0))

    #logic
    for theta in range(361):
        k = theta * d * math.pi / 180
        r = 300 * math.sin(n * k)
        x = r * math.cos(k)
        y = r * math.sin(k)
        draw_line(int(memx),int(memy),int(x) + int(tempx),int(y) + int(tempy),c)
        image_draw_line_v(img,Vector2(int(imgx),int(imgy)),Vector2(int(x) + dempx,int(y) + dempy),c)
        memx,memy = int(x) + int(tempx),int(y) + int(tempy)
        imgx,imgy = int(x) + dempx,int(y) + dempy

    #auto save
    if is_key_pressed(KEY_A):
        
        for i in range(10):
            n,d = random.randint(2,100),random.randint(2,100)
            c = Color(random.randint(100,255),random.randint(100,255),random.randint(100,255),255)
            image_clear_background(img,BLACK)
            for theta in range(361):
                k = theta * d * math.pi / 180
                r = 300 * math.sin(n * k)
                x = r * math.cos(k)
                y = r * math.sin(k)
                image_draw_line_v(img,Vector2(int(imgx),int(imgy)),Vector2(int(x) + dempx,int(y) + dempy),c)
                imgx,imgy = int(x) + dempx,int(y) + dempy
            export_image(img,f"{time.time()}.png")

    #randomize
    if is_key_pressed(KEY_R):
        image_clear_background(img,BLACK)
        n,d = random.randint(2,100),random.randint(2,100)
        tempx,tempy = tx/2,ty/2
        dempx,dempy = dx/2,dy/2
        c = Color(random.randint(100,255),random.randint(100,255),random.randint(100,255),255)

    #save image
    if is_key_pressed(KEY_S):
        export_image(img,f"{time.time()}.png")

    end_drawing()

#closure
close_window()