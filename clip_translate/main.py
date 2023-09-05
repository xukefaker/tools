import pyperclip, time
import keyboard
import json
from utils import chatGPTInstance
import threading
import tkinter as tk
from tkinter import Text
import tkinter.font as tkFont

with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

chatgpt = chatGPTInstance(config)
pasted_flag = False
root = tk.Tk()
text = Text(root, width=50, height=10)
text.pack(padx=10, pady = 10)
fontExample = tkFont.Font(family=config['font_family'], size=config['font_size'])
text.configure(font=fontExample)
root.wm_attributes('-topmost', 1)

def save_result():
    global pasted_flag, text
    while True:
        time.sleep(0.1)
        if pasted_flag:
            pasted_flag = False
            clip_txt = pyperclip.paste()
            translate_result = chatgpt.translate_single(clip_txt)
            with open(config['storage_file_path'], encoding='utf-8', mode='a+') as f:
                f.write('请求翻译的句子:{}\n'.format(clip_txt))
                f.write('翻译结果:{}\n'.format(translate_result))
                f.write('翻译时间：{}\n'.format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
            text.delete('1.0', 'end')
            text.insert('end', translate_result)

def change_paste():
    global pasted_flag
    pasted_flag = True

def main():
    thread_1 = threading.Thread(target=save_result)
    thread_1.start()
    keyboard.add_hotkey('ctrl+c', change_paste)
    root.mainloop()
    try:
        keyboard.wait('ctrl+c')
    except KeyboardInterrupt:
        print('用户终止程序')

if __name__ == '__main__':
    main()

