# 그리드 : 격자, 좌표 기반으로 해석가능(위젯배치)  [ex) 바둑판] , 격자에 앞에 배운것들을 배치할때 사용할수 있음

from tkinter import *

root = Tk()
root.title("hwankko GUI")  # 제목
root.geometry("640x480")  # 창크기: 가로 x 세로

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # pack을 이용해서 위치 조점
# # btn1.pack(side="right")
# # btn2.pack(side="right")

# # 그리드로 이용해서 위치 조정
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)


 # ---------------------------
# 계산기 키보드 버튼 위젯 만들기

# 맨 윗줄
btn_f16 = Button(root, text="F16", width=7, height=4)
btn_f17 = Button(root, text="F17", width=7, height=4)
btn_f18 = Button(root, text="F18", width=7, height=4)
btn_f19 = Button(root, text="F19", width=7, height=4)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)  # sticky: 내가 지정한 방향으로 위젯을 늘려라
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3,sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", padx=10, pady=10)
btn_equal = Button(root, text=" = ", padx=10, pady=10)
btn_div = Button(root, text = " / ", padx=10, pady=10)
btn_mul = Button(root, text=" * ", padx=10, pady=10)

btn_clear.grid(row=1, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3,sticky=N+E+W+S, padx=3, pady=3)

# 7 시작 줄
btn_7 = Button(root, text=" 7 ",  padx=10, pady=10)
btn_8 = Button(root, text=" 8 ", padx=10, pady=10)
btn_9 = Button(root, text=" 9 ", padx=10, pady=10)
btn_sub = Button(root, text=" - ",padx=10, pady=10)

btn_7.grid(row=2, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3,sticky=N+E+W+S, padx=3, pady=3)


# 4 시작 줄
btn_4 = Button(root, text=" 4 ", padx=10, pady=10)
btn_5 = Button(root, text=" 5 ", padx=10, pady=10)
btn_6 = Button(root, text=" 6 ", padx=10, pady=10)
btn_plu = Button(root, text=" + ", padx=10, pady=10)

btn_4.grid(row=3, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_plu.grid(row=3, column=3,sticky=N+E+W+S, padx=3, pady=3)

# 1 시작 줄
btn_1 = Button(root, text=" 1 ", padx=10, pady=10)
btn_2 = Button(root, text=" 2 ", padx=10, pady=10)
btn_3 = Button(root, text=" 3 ", padx=10, pady=10)
btn_enter = Button(root, text="Enter", padx=10, pady=10)

btn_1.grid(row=4, column=0,sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1,sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2,sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2,sticky=N+E+W+S, padx=3, pady=3) # rowspan: row 2개를 합치겠다(현재 위치로 부터 아랫줄 2줄을 더함)

# 0 시작줄
btn_0 = Button(root, text=" 0 ", padx=10, pady=10)
btn_point = Button(root, text=" . ", padx=10, pady=10)


btn_0.grid(row=5, column=0, columnspan=2,sticky=N+E+W+S, padx=3, pady=3) # columnspan: 현재위치로 부터 오른쪽 2개를 더함
btn_point.grid(row=5, column=2,sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()  # 창이 닫히지 않도록 해줌