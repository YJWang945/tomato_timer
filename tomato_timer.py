import tkinter as tk
from tkinter import messagebox
import time

class TomatoTimer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("番茄钟")
        self.window.geometry("400x300")
        self.window.resizable(False, False)
        
        # 设置窗口背景色
        self.window.configure(bg='#f0f0f0')
        
        # 创建时间变量
        self.minutes = tk.StringVar(value="25")
        self.remaining_time = 0
        self.timer_running = False
        self.timer = None
        
        self.create_widgets()
        
    def create_widgets(self):
        # 标题标签
        title_label = tk.Label(
            self.window,
            text="番茄钟",
            font=("Arial", 24, "bold"),
            bg='#f0f0f0',
            fg='#333333'
        )
        title_label.pack(pady=20)
        
        # 时间显示标签
        self.time_label = tk.Label(
            self.window,
            text="25:00",
            font=("Arial", 48),
            bg='#f0f0f0',
            fg='#444444'
        )
        self.time_label.pack(pady=10)
        
        # 时间输入框
        input_frame = tk.Frame(self.window, bg='#f0f0f0')
        input_frame.pack(pady=10)
        
        tk.Label(
            input_frame,
            text="设置时间(分钟):",
            font=("Arial", 10),
            bg='#f0f0f0'
        ).pack(side=tk.LEFT, padx=5)
        
        self.time_entry = tk.Entry(
            input_frame,
            textvariable=self.minutes,
            width=10,
            font=("Arial", 10)
        )
        self.time_entry.pack(side=tk.LEFT, padx=5)
        
        # 按钮框架
        button_frame = tk.Frame(self.window, bg='#f0f0f0')
        button_frame.pack(pady=20)
        
        # 开始按钮
        self.start_button = tk.Button(
            button_frame,
            text="开始",
            command=self.start_timer,
            width=10,
            bg='#4CAF50',
            fg='white',
            font=("Arial", 10)
        )
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        # 暂停按钮
        self.pause_button = tk.Button(
            button_frame,
            text="暂停",
            command=self.pause_timer,
            width=10,
            bg='#ff9800',
            fg='white',
            font=("Arial", 10)
        )
        self.pause_button.pack(side=tk.LEFT, padx=5)
        
        # 重置按钮
        self.reset_button = tk.Button(
            button_frame,
            text="重置",
            command=self.reset_timer,
            width=10,
            bg='#f44336',
            fg='white',
            font=("Arial", 10)
        )
        self.reset_button.pack(side=tk.LEFT, padx=5)
        
    def update_timer(self):
        if self.remaining_time > 0 and self.timer_running:
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.remaining_time -= 1
            self.timer = self.window.after(1000, self.update_timer)
        elif self.remaining_time <= 0 and self.timer_running:
            self.timer_running = False
            self.time_label.config(text="00:00")
            messagebox.showinfo("完成", "恭喜你完成专注！")
            
    def start_timer(self):
        if not self.timer_running:
            try:
                minutes = int(self.minutes.get())
                if minutes <= 0:
                    raise ValueError
                if not self.remaining_time:
                    self.remaining_time = minutes * 60
                self.timer_running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("错误", "请输入有效的分钟数！")
                
    def pause_timer(self):
        self.timer_running = False
        if self.timer:
            self.window.after_cancel(self.timer)
            
    def reset_timer(self):
        self.timer_running = False
        if self.timer:
            self.window.after_cancel(self.timer)
        try:
            minutes = int(self.minutes.get())
            if minutes <= 0:
                raise ValueError
            self.remaining_time = minutes * 60
            self.time_label.config(text=f"{minutes:02d}:00")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的分钟数！")
            
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TomatoTimer()
    app.run() 