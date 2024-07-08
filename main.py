import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def select_image():
    global img_path, img_tk
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        label_image.config(image=img_tk)
        label_image.image = img_tk

def resize_and_save():
    try:
        if not img_path:
            messagebox.showerror("Ошибка", "Выберите изображение сначала")
            return
        
        new_width = int(entry_width.get())
        new_height = int(entry_height.get())
        quality = int(entry_quality.get())
        
        image = Image.open(img_path)
        resized_image = image.resize((new_width, new_height), Image.LANCZOS)
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[
            ("JPEG files", "*.jpg"), 
            ("PNG files", "*.png"),
            ("GIF files", "*.gif"),
            ("BMP files", "*.bmp"),
            ("TIFF files", "*.tiff"),
            ("All files", "*.*")
        ])
        if save_path:
            resized_image.save(save_path, quality=quality)
            messagebox.showinfo("Успех", "Изображение сохранено")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось изменить размер изображения: {e}")

root = tk.Tk()
root.title("Image Resizer")

frame_controls = tk.Frame(root)
frame_controls.pack(side=tk.LEFT, pady=10, padx=10)

frame_image = tk.Frame(root)
frame_image.pack(side=tk.RIGHT, pady=10, padx=10)

btn_select = tk.Button(frame_controls, text="Выбрать изображение", command=select_image)
btn_select.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

label_width = tk.Label(frame_controls, text="Ширина:")
label_width.grid(row=1, column=0, pady=5, sticky="e")
entry_width = tk.Entry(frame_controls)
entry_width.grid(row=1, column=1, pady=5, sticky="w")

label_height = tk.Label(frame_controls, text="Высота:")
label_height.grid(row=2, column=0, pady=5, sticky="e")
entry_height = tk.Entry(frame_controls)
entry_height.grid(row=2, column=1, pady=5, sticky="w")

label_quality = tk.Label(frame_controls, text="Качество (1-95):")
label_quality.grid(row=3, column=0, pady=5, sticky="e")
entry_quality = tk.Entry(frame_controls)
entry_quality.grid(row=3, column=1, pady=5, sticky="w")

btn_save = tk.Button(frame_controls, text="Изменить размер и сохранить", command=resize_and_save)
btn_save.grid(row=4, column=0, columnspan=2, pady=10)

label_image = tk.Label(frame_image)
label_image.pack()

root.mainloop()
