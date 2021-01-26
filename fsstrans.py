#fssolution 단축키중 작업효율을 위해 spacebar로 del키 기능이 가능하도록 하는 코드입니다. 
#만든이 : 함준혁
#문의사항/요청사항은 :kent2499@naver.com으로 연락바랍니다. 
#https://doljokilab.tistory.com/

#키 후킹을 위한 파이썬 라이브러리 임포트 
import pynput
import os

kp = pynput.keyboard.Controller()
print("delete키를 spacebar로 대체하는 프로그램입니다.(ver 0.1)")
print("사용시 발생하는 문제는 개발자가 따로 책임지지 않습니다.")
print("프로그램 실행중, 'esc'누르면 종료됩니다.")
print("소스코드 공개 : https://github.com/dol42/fsHOTKEY/blob/master/fsstrans.py ")


def on_press(key):
    return

#중복키 방지를 위해 키보드에서 뗐을경우 실행하는 함수
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        print("프로그램 종료")
        return False
    elif key == pynput.keyboard.Key.space:
        kp.press(pynput.keyboard.Key.delete)
        kp.release(pynput.keyboard.Key.delete)

# 키 후킹용 리스너 실행
listener = pynput.keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()

os.system("pause")