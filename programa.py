from tkinter import *
from time import *
from random import randint
from functools import partial

bg_color = "#28501A"
text_color = "white"

# modificar para alterar los parametros horas, minutos y segundos
# que estan inicialmente como proxima descarga.
h_ini = "00"
m_ini = "00"
s_ini = "09"

ventana = Tk()
ventana.geometry("600x600")
ventana.title("Dispensador de sal de polifosfato")
ventana.configure(background=bg_color)

def mainWindow():
    def configurar():
        points = [40, 30, 45, 30, 42.5, 35]
        canvas.create_polygon(points)

    def obtenerHora(date):
        date = ctime(date)
        return date[11:19]

    def obtenerFecha(date):
        date = ctime(date)
        mes = date[4:7]
        if mes == "Jan":
            mes = "1"
        elif mes == "Feb":
            mes = "2"
        elif mes == "Mar":
            mes = "3"
        elif mes == "Apr":
            mes = "4"
        elif mes == "May":
            mes = "5"
        elif mes == "Jun":
            mes = "6"
        elif mes == "Jul":
            mes = "7"
        elif mes == "Aug":
            mes = "8"
        elif mes == "Sep":
            mes = "9"
        elif mes == "Oct":
            mes = "10"
        elif mes == "Nov":
            mes = "11"
        elif mes == "Dec":
            mes = "12"
        return date[8:10] + "-" + mes + "-" + date[20:]

    def toTimestamp(h, m, s):
        return int(h) * 3600 + int(m) * 60 + int(s)

    def countdownEnd(main_label, date, hour, wait_time, dispose_time, stage):
        if stage == 0:
            # la etiqueta principal cambia a --:--:--
            main_label.configure(text="--:--:--")
            main_label.place(x=290, y=40)
            # en la etapa 0 cambia a este formato
            date.configure(text="--/--/-- A LAS")
            date.place(x=275, y=210)
            # lo mismo
            hour.configure(text="--:--:--")
            hour.place(x=290, y=260)
            mins = randint(1, 3)
            # wait_time es el tiempo de espera
            wait_time.configure(text="00:0" + str(mins) + ":00")
            wait_time.place(x=240, y=410)
            countdown("00", "00", "05", 240, 410, 1, wait_time, dispose_time)
        elif stage == 1:
            # main_label ahora es el tiempo de espera
            main_label.configure(text="--:--:--")
            main_label.place(x=290, y=410)
            # aparece de nuevo
            timestamp = time()
            timestamp += toTimestamp(h_ini, m_ini, s_ini)
            hora = obtenerHora(timestamp)
            fecha = obtenerFecha(timestamp)
            date.configure(text=fecha+" A LAS")
            date.place(x=230, y=210)
            hour.configure(text=hora)
            hour.place(x=240, y=260)
            countdown("00", "00", "05", 240, 40, 0, dispose_time, wait_time)

    canvas = Canvas(bg=bg_color)
    # Lineas principales
    canvas.create_line(210, 0, 210, 555)
    canvas.create_line(0, 190, 600, 190)
    canvas.create_line(0, 380, 600, 380)
    canvas.create_line(0, 555, 600, 555)
    # Muestra la bateria restante
    canvas.create_line(90, 570, 120, 570)
    canvas.create_line(90, 585, 120, 585)
    canvas.create_line(90, 570, 90, 585)
    canvas.create_line(120, 570, 120, 574.5)
    canvas.create_line(120, 585, 120, 580.5)
    canvas.create_line(120, 574.5, 125, 574.5)
    canvas.create_line(120, 580.5, 125, 580.5)
    canvas.create_line(125, 574.5, 125, 580.5)
    canvas.create_rectangle(90, 570, 107, 585, fill='black')
    # ---
    canvas.pack(fill=BOTH, expand=1)

    primer_frame = []
    L = Label(ventana, text="PRÓXIMA", bg=bg_color, font=("System", 20))
    primer_frame.append(L)
    L.place(x=40, y=50)
    L = Label(ventana, text="DESCARGA", bg=bg_color, font=("System", 20))
    primer_frame.append(L)
    L.place(x=30, y=80)
    L = Label(ventana, text="EN:", bg=bg_color, font=("System", 20))
    primer_frame.append(L)
    L.place(x=80, y=110)
    lv = Label(ventana, text=h_ini+":"+m_ini+":"+s_ini, bg=bg_color, font=("System", 60))
    primer_frame.append(lv)
    lv.place(x=240, y=40)

    timestamp = time()
    timestamp += toTimestamp(h_ini, m_ini, s_ini)
    hora = obtenerHora(timestamp)
    fecha = obtenerFecha(timestamp)

    segundo_frame = []
    L = Label(ventana, text="PROGRAMADO", bg=bg_color, font=("System", 20))
    segundo_frame.append(L)
    L.place(x=5, y=250)
    L = Label(ventana, text="PARA EL:", bg=bg_color, font=("System", 20))
    segundo_frame.append(L)
    L.place(x=30, y=280)
    date_label = Label(ventana, text=fecha+" A LAS:", bg=bg_color, font=("System", 30))
    segundo_frame.append(date_label)
    date_label.place(x=220, y=210)
    hour_label = Label(ventana, text=hora, bg=bg_color, font=("System", 60))
    segundo_frame.append(hour_label)
    hour_label.place(x=240, y=260)

    tercer_frame = []
    L = Label(ventana, text="TIEMPO DE", bg=bg_color, font=("System", 20))
    tercer_frame.append(L)
    L.place(x=20, y=430)
    L = Label(ventana, text="ESPERA:", bg=bg_color, font=("System", 20))
    tercer_frame.append(L)
    L.place(x=40, y=460)
    wait_label = Label(ventana, text="--:--:--", bg=bg_color, font=("System", 60))
    tercer_frame.append(wait_label)
    wait_label.place(x=290, y=410)

    def actualizarReloj():
        curr_hora = strftime("%H:%M")
        curr_fecha = strftime("%d-%m-%Y")
        l4 = Label(ventana, text=curr_hora, bg=bg_color, font=("System", 10))
        l4.place(x=25, y=567.5)
        l4 = Label(ventana, text=curr_fecha, bg=bg_color, font=("System", 10))
        l4.place(x=200, y=567.5)
        l4.after(1000, actualizarReloj)

    actualizarReloj()

    l6 = Label(ventana, text="56%", bg=bg_color, font=("System", 10))
    l6.place(x=130, y=567.5)

    # De aqui para abajo, incluyendo countdown(h,m,s), hace que el tiempo de dispensacion baje.

    def countdown(h, m, s, x, y, stage, main_label, second_label):
        main_label.configure(text=h+":"+m+":"+s)
        main_label.place(x=x, y=y)

        if int(s)-1 < 0:
            s = "59"
            if int(m)-1 < 0:
                m = "59"
                if int(h)-1 < 0:
                    if stage == 0:
                        # main_label es el dispose_time
                        countdownEnd(main_label, date_label, hour_label, second_label, main_label, stage)
                    elif stage == 1:
                        # main_label ahora es el tiempo de espera
                        countdownEnd(main_label, date_label, hour_label, main_label, second_label,  stage)
                    return
                else:
                    h = str(int(h) - 1)
            else:
                m = str(int(m) - 1)
        else:
            s = str(int(s) - 1)

        # str(int(x)) es para eliminar los ceros del principio
        if int(h) < 10:
            h = "0" + str(int(h))
        if int(m) < 10:
            m = "0" + str(int(m))
        if int(s) < 10:
            s = "0" + str(int(s))

        sleep(1)
        ventana.update()

        countdown(h, m, s, x, y, stage, main_label, second_label)

    b1 = Button(ventana, text="Configuración", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b1.place(x=310, y=565)
    b2 = Button(ventana, text="Inicio", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b2.place(x=415, y=565)
    b3 = Button(ventana, text="Regresar", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b3.place(x=465, y=565)
    b4 = Button(ventana, text="Apagar", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b4.place(x=540, y=565)

    countdown(h_ini, m_ini, s_ini, 240, 40, 0, lv, wait_label)

mainWindow()
ventana.mainloop()
