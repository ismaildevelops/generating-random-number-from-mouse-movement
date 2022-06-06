import time
import winsound
import pyautogui
def random_number():
    k = int(input("Set a time in seconds for wait to move your cursor: "))
    
    t_end = time.time()  + k
    print(time.time())
    print("\n",t_end)
    print("\n")

    RGB3 = ""
    
    winsound.Beep(1000, 500)
    time.sleep(3)

    while time.time()<t_end:
        x, y = pyautogui.position()
        a,b,c = pyautogui.pixel(x,y)
        positionOfxy = str(x).rjust(4) + str(y).rjust(4)
        
        #print("Position = ",positionOfxy ,end =" ")
        RGB = str(a).rjust(4) + str(b).rjust(4)+ str(c).rjust(4)
        RGB2 = RGB.replace(' ','')
        
        RGB3 = RGB3 + RGB2
        #print(RGB3 ,end ="")
    winsound.Beep(1000, 500)
    print("Random number Based on The mouse co-ordinates: ",positionOfxy)
    print("\n")    
    
##    LatestRGB = RGB3
##    print("Random number generated based on the pixel values of mouse movements: ",LatestRGB)
##    LatestRGB  = int(LatestRGB)
##    print("\n")
##    print("I am now finished")
##    if LatestRGB %2 ==0:
##        print("YES   = = EVEN NUMBER  ")
##    else:
##        print("NO      = = ODD NUMBER ")
random_number()
