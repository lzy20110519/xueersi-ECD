#连点器 陈昕宇制作
#版本号：v2.0.0 完结
#已上线
import keyboard as kb
import time
import win32api,win32con
def clickforever():
    while True:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        if kb.is_pressed("q"):
            print("连点结束")
            break
        time.sleep(0.05)
def clicktime(_time_):
    for i in range(_time_):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        if kb.is_pressed("q"):
            print("连点结束")    
            break
        time.sleep(0.05)
def clickv(float):
    while True:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        if kb.is_pressed("q"):
            print("连点结束")    
            break
        time.sleep(float)
def clicktimev(_time_,float):
    for i in range(_time_):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        if kb.is_pressed("q"):
            print("连点结束")    
            break
        time.sleep(float)