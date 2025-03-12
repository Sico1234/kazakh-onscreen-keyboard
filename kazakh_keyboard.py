import tkinter as tk
import pyautogui
import pyperclip
import time

# Цвета
BG_COLOR = '#F9F9F9'                # Основной фон (почти белый)
BTN_COLOR = '#FFFFFF'               # Белые кнопки
BTN_ACTIVE_COLOR = '#E5E5EA'        # Серый при наведении
TEXT_COLOR = '#000000'              # Черный текст
SHIFT_ACTIVE_COLOR = '#D1D1D6'      # Для активного Shift

letters_lower = ['ә', 'і', 'ң', 'ғ', 'ү', 'ұ', 'қ', 'ө', 'һ']
letters_upper = ['Ә', 'І', 'Ң', 'Ғ', 'Ү', 'Ұ', 'Қ', 'Ө', 'Һ']

shift_active = False

def type_letter(letter):
    root.withdraw()
    time.sleep(0.1)
    pyperclip.copy(letter)
    pyautogui.hotkey('ctrl', 'v')
    root.deiconify()

def toggle_shift():
    global shift_active
    shift_active = not shift_active
    update_keys()
    if shift_active:
        shift_btn.itemconfig(1, fill=SHIFT_ACTIVE_COLOR, outline=SHIFT_ACTIVE_COLOR)
    else:
        shift_btn.itemconfig(1, fill=BTN_COLOR, outline=BTN_COLOR)

def update_keys():
    for idx, btn in enumerate(letter_buttons):
        text = letters_upper[idx] if shift_active else letters_lower[idx]
        btn.itemconfig(2, text=text)
        btn.bind("<Button-1>", lambda event, l=text: type_letter(l))
        btn.tag_bind(2, "<Button-1>", lambda event, l=text: type_letter(l))

def create_rounded_button(master, text, command, x, y, w=80, h=50, r=15,
                           bg=BTN_COLOR, fg=TEXT_COLOR, active_bg=BTN_ACTIVE_COLOR, font_size=16):
    canvas = tk.Canvas(master, width=w, height=h, bg=master['bg'], highlightthickness=0)
    
    def round_rect(x1, y1, x2, y2, radius, **kwargs):
        points = [
            x1 + radius, y1,
            x2 - radius, y1,
            x2 - radius, y1,
            x2, y1,
            x2, y1 + radius,
            x2, y2 - radius,
            x2, y2 - radius,
            x2, y2,
            x2 - radius, y2,
            x1 + radius, y2,
            x1 + radius, y2,
            x1, y2,
            x1, y2 - radius,
            x1, y1 + radius,
            x1, y1 + radius,
            x1, y1
        ]
        return canvas.create_polygon(points, **kwargs, smooth=True)

    btn_bg = round_rect(1, 1, w - 1, h - 1, r, fill=bg, outline='#D1D1D6', width=1.5)
    btn_text = canvas.create_text(w / 2, h / 2, text=text, fill=fg, font=('Helvetica Neue', font_size))

    def on_click(event):
        command()

    def on_enter(event):
        canvas.itemconfig(btn_bg, fill=active_bg)

    def on_leave(event):
        canvas.itemconfig(btn_bg, fill=bg)

    canvas.tag_bind(btn_bg, "<Button-1>", on_click)
    canvas.tag_bind(btn_text, "<Button-1>", on_click)

    canvas.tag_bind(btn_bg, "<Enter>", on_enter)
    canvas.tag_bind(btn_text, "<Enter>", on_enter)

    canvas.tag_bind(btn_bg, "<Leave>", on_leave)
    canvas.tag_bind(btn_text, "<Leave>", on_leave)

    canvas.place(x=x, y=y)
    return canvas

# Окно
root = tk.Tk()
root.title("Kazakh Keyboard - Apple Style")
root.config(bg=BG_COLOR)
root.geometry("900x300")
root.attributes('-topmost', True)
root.resizable(False, False)

# Создание кнопок
letter_buttons = []
x_offset = 20
for idx, letter in enumerate(letters_lower):
    btn = create_rounded_button(root, letter, lambda l=letter: type_letter(l),
                                x=x_offset, y=30)
    letter_buttons.append(btn)
    x_offset += 90  # расстояние между кнопками

# Shift Button
shift_btn = create_rounded_button(root, 'Shift', toggle_shift, x=20, y=150, w=120)

# Exit Button
exit_btn = create_rounded_button(root, 'Exit', root.destroy, x=760, y=150, w=120, bg='#FF3B30', active_bg='#FF453A', fg='white')

root.mainloop()
