from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("danh sach hoc sinh")
window.geometry("500x600+100+50")

def show_choice():
    messagebox.showinfo("Kết quả", f"Bạn đã chọn số: {value.get()}")

hoten = "Nguyễn Văn A"
ngaysinh = "01/01/2004"
mssv = "12345678"
nganh = "Kỹ thuật điều khiển và tự động hóa"


# --- Biến lưu giá trị radio ---
value = IntVar()
value.set(0)

lbl = Radiobutton(window, text="First", variable=value, value=1, font=("Arial", 12))
lbl.place(x= 0, y = 0)
lbl = Radiobutton(window, text="Second", variable=value, value=2, font=("Arial", 12))
lbl.place(x = 60, y =0)
lbl = Radiobutton(window, text="Third", variable=value, value=3, font=("Arial", 12))
lbl.place(x=140, y = 0)
btn = Button(window, text="Click Me", command=show_choice,
          font=("Arial", 12), width=10)
btn.place(x = 210, y = 0)

lbl = Label(window, text="THÔNG TIN CÁ NHÂN", font=("Arial", 16, "bold"))
lbl.place(x = 200, y = 100)
lbl = Label(window, text="Họ và tên: " + hoten, font=("Arial", 12))
lbl.place(x= 100, y = 150)
lbl = Label(window, text="Ngày sinh: " + ngaysinh, font=("Arial", 12))
lbl.place(x= 100, y = 175)
lbl = Label(window, text="MSSV: " + mssv, font=("Arial", 12))
lbl.place(x=100, y = 200)
lbl = Label(window, text="Ngành học: " + nganh, font=("Arial", 12))
lbl.place(x = 100, y = 225)



window.mainloop()
