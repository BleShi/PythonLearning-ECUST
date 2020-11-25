import tkinter as tk

window = tk.Tk()

window.title('登录')
 
window.geometry('230x130') 

frame = tk.Frame(window)
frame.pack()
 

frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')
 

tk.Label(frame_l, font=('微软雅黑', 12), text='姓名：').pack()
tk.Label(frame_l, font=('微软雅黑', 12), text='密码：').pack()
tk.Button(frame_l, text='登录', font=('微软雅黑', 12), width=10, height=1,).pack()
tk.Entry(frame_r, show=None, font=('微软雅黑', 14)).pack()
tk.Entry(frame_r, show='*', font=('微软雅黑', 14)).pack()
tk.Button(frame_r, text='退出', font=('微软雅黑', 12), width=10, height=1,).pack()
 
window.mainloop()