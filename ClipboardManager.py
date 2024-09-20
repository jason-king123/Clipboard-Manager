import tkinter as tk
from tkinter import ttk
import pyperclip
import datetime
import json
import os

X = []
DATA_FILE = 'clipboard_data.json'

# 创建主窗口
root = tk.Tk()
root.geometry('600x500')
root.title('Clipboard Manager')
root.configure(bg='#ffffff')

# 设置窗口图标
icon_path = 'sad.ico'
root.iconbitmap(icon_path)

# 设置样式
style = ttk.Style()
style.configure('TFrame', background='#ffffff')
style.configure('TLabel', background='#ffffff', font=('Helvetica', 12))
style.configure('TButton', background='#4CAF50', foreground='#ffffff', font=('Helvetica', 10, 'bold'))
style.map('TButton', background=[('active', '#45a049')])  # 设置按钮的激活状态颜色

# 创建框架
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.X)

label = ttk.Label(frame, text='Clipboard Contents:')
label.grid(row=0, column=0, padx=5, pady=5)

# 清除按钮
clear_button = tk.Button(frame, text='Clear', command=lambda: clear_listbox(), bg='#4CAF50', fg='#ffffff', font=('Helvetica', 10, 'bold'))
clear_button.grid(row=0, column=1, padx=5, pady=5)

# 提示标签
copy_label = ttk.Label(frame, text='', foreground='green')
copy_label.grid(row=0, column=2, padx=5, pady=5)

# 创建滚动条
scrollbar_y = ttk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# 创建列表框
listbox = tk.Listbox(root, width=80, height=20, yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set, font=('Courier', 10))
listbox.pack(pady=10, padx=10)

scrollbar_y.config(command=listbox.yview)
scrollbar_x.config(command=listbox.xview)

def get_current_time():
    return datetime.datetime.now().strftime(r"%Y-%m-%d %H:%M:%S")

def update_listbox():
    new_item = pyperclip.paste()
    if new_item not in X:
        X.append(new_item)
        listbox.insert(tk.END, new_item)
        listbox.insert(tk.END, f'----------------------------{get_current_time()}----------------------------')
        listbox.yview(tk.END)
    root.after(1000, update_listbox)

def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(X, file)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    else: # 不存在就创建
        with open(DATA_FILE, 'w') as file:
            return []

def populate_listbox():
    for item in X:
        listbox.insert(tk.END, item)
        listbox.insert(tk.END, f'----------------------------{get_current_time()}----------------------------')

# 复制到剪贴板函数
def copy_to_clipboard(event):
    selected_item = listbox.get(listbox.curselection())
    if selected_item:
        pyperclip.copy(selected_item)
        copy_label.config(text='Copied to clipboard!')
        root.after(2000, lambda: copy_label.config(text=''))  # 2秒后清除提示信息

# 清空列表框函数
def clear_listbox():
    listbox.delete(0, tk.END)
    X.clear()
    with open(DATA_FILE, 'w') as file:
        json.dump(X, file)
    copy_label.config(text='List cleared!')
    root.after(2000, lambda: copy_label.config(text=''))  # 2秒后清除提示信息

# 关闭程序时保存数据
def on_closing():
    save_data()
    root.destroy()

# 加载数据并填充列表框
X = load_data()
populate_listbox()

# 启动更新列表框循环
update_listbox()

# 绑定事件
listbox.bind('<Double-Button-1>', copy_to_clipboard)

# 绑定关闭事件
root.protocol("WM_DELETE_WINDOW", on_closing)

# 启动主循环
root.mainloop()