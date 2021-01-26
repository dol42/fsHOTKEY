#fssolution 단축키중 작업효율을 위해 spacebar로 del키 기능이 가능하도록 하는 코드입니다. 
#만든이 : 함준혁
#문의사항/요청사항은 :kent2499@naver.com으로 연락바랍니다. 
#https://doljokilab.tistory.com/

#키 후킹을 위한 파이썬 라이브러리 임포트 
from pynput import keyboard
from pynput.keyboard import Key, Controller
kp = Controller()

def on_press(key):
    return

#중복키 방지를 위해 키보드에서 뗐을경우 실행하는 함수
def on_release(key):
    if key == keyboard.Key.esc:
        return False
    elif key == keyboard.Key.space:
        kp.press(keyboard.Key.delete)
        kp.release(keyboard.Key.delete)

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

# 키 후킹용 리스너 실행
listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()