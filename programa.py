from tkinter import *
from time import *
from random import randint

bg_color = "#28501A"
text_color = "white"

# modificar para alterar los parametros horas, minutos y segundos
# que estan inicialmente como proxima descarga.
h_ini = "00"
m_ini = "00"
s_ini = "09"

# estos son las horas, mins, y sec del tiempo de espera predefinido
# tmb se puede modificar para alterar el programa
h_wt = "00"
m_wt = "00"
s_wt = "05"

# si el modo config esta activado o no
cfg_Mode = False

ventana = Tk()
ventana.geometry("600x600")
ventana.title("Dispensador de sal de polifosfato")
ventana.configure(background=bg_color)

def mainWindow():
    # str str str -> list(str)
    def parseTime(h, m, s):
        if int(h) < 10:
            h = "0" + str(int(h))
        if int(m) < 10:
            m = "0" + str(int(m))
        if int(s) < 10:
            s = "0" + str(int(s))
        return [h, m, s]

    # int(timestamp) -> str
    def obtenerHora(date):
        date = ctime(date)
        return date[11:19]

    # int(timestamp) -> str
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

    # str str str -> int(timestamp)
    def toTimestamp(h, m, s):
        return int(h) * 3600 + int(m) * 60 + int(s)

    # Label Label Label Label Label int -> None
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
            countdown(h_wt, m_wt, s_wt, 240, 410, 1, wait_time, dispose_time)
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
            countdown(h_ini, m_ini, s_ini, 240, 40, 0, dispose_time, wait_time)

    canvas = Canvas(bg=bg_color)
    # Lineas principales
    vertical = canvas.create_line(210, 0, 210, 555)
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
    # str str str int int int Label Label -> None
    def countdown(h, m, s, x, y, stage, main_label, second_label):
        global cfg_Mode
        # si esta en el modo config, no queremos que siga la cuenta atras
        if cfg_Mode:
            return
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
                        countdownEnd(main_label, date_label, hour_label, main_label, second_label, stage)
                    return
                else:
                    h = str(int(h) - 1)
            else:
                m = str(int(m) - 1)
        else:
            s = str(int(s) - 1)

        nh, nm, ns = parseTime(h, m, s)
        sleep(1)
        ventana.update()

        countdown(nh, nm, ns, x, y, stage, main_label, second_label)

    def test():
        global cfg_Mode
        cfg_Mode = True
        canvas.move(vertical, 20, 0)
        primer_frame[0].configure(text="PERIODO DE")
        primer_frame[0].place(x=20, y=60)
        primer_frame[1].configure(text="DISPENSACION:")
        primer_frame[1].place(x=5, y=90)
        primer_frame[2].configure(text="")
        primer_frame[2].place(x=5, y=110)
        segundo_frame[0].configure(text="SAL A")
        segundo_frame[1].configure(text="DISPENSAR:")

    # Event -> None
    def seccion_handler(e):
        global cfg_Mode
        if not cfg_Mode:
            return
        x, y = e.x, e.y
        print(x, y)
        if x > 600 or x < 230 or y < 0 or y > 570:
            return
        if 0 <= y <= 190:
            def fH_up(_):
                global h_ini
                if int(h_ini) >= 90:
                    resto = int(h_ini) % 10
                    h_ini = "0" + str(resto)
                else:
                    h_ini = str(int(h_ini) + 10)
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(250, 40, 265, 20, 280, 40, tags="H_up")
            canvas.tag_bind("H_up", "<Button-1>", fH_up)

            def fh_up(_):
                global h_ini
                if int(h_ini) == 99:
                    h_ini = "00"
                else:
                    h_ini = parseTime(str(int(h_ini) + 1), m_ini, s_ini)[0]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(295, 40, 310, 20, 325, 40, tags="h_up")
            canvas.tag_bind("h_up", "<Button-1>", fh_up)

            def fM_up(_):
                global m_ini
                if int(m_ini) >= 50:
                    resto = int(m_ini) % 10
                    m_ini = "0" + str(resto)
                else:
                    m_ini = str(int(m_ini) + 10)
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(360, 40, 375, 20, 390, 40, tags="M_up")
            canvas.tag_bind("M_up", "<Button-1>", fM_up)

            def fm_up(_):
                global m_ini
                if int(m_ini) == 59:
                    m_ini = "00"
                else:
                    m_ini = parseTime(h_ini, str(int(m_ini) + 1), s_ini)[1]
                lv.configure(text=h_ini + ":" + m_ini + ":" + s_ini)

            canvas.create_polygon(405, 40, 420, 20, 435, 40, tags="m_up")
            canvas.tag_bind("m_up", "<Button-1>", fm_up)

            def fS_up(_):
                global s_ini
                if int(s_ini) >= 50:
                    resto = int(s_ini) % 10
                    s_ini = "0" + str(resto)
                else:
                    s_ini = str(int(s_ini) + 10)
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(470, 40, 485, 20, 500, 40, tags="S_up")
            canvas.tag_bind("S_up", "<Button-1>", fS_up)

            def fs_up(_):
                global s_ini
                if int(s_ini) == 59:
                    s_ini = "00"
                else:
                    s_ini = parseTime(h_ini, m_ini, str(int(s_ini) + 1))[2]
                lv.configure(text=h_ini + ":" + m_ini + ":" + s_ini)

            canvas.create_polygon(515, 40, 530, 20, 545, 40, tags="s_up")
            canvas.tag_bind("s_up", "<Button-1>", fs_up)

            # Flechas pa abajo
            def fH_down(_):
                global h_ini
                if int(h_ini) < 10:
                    resto = int(h_ini) % 10
                    h_ini = "9" + str(resto)
                else:
                    h_ini = parseTime(str(int(h_ini) - 10), m_ini, s_ini)[0]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(250, 150, 265, 170, 280, 150, tags="H_down")
            canvas.tag_bind("H_down", "<Button-1>", fH_down)

            def fh_down(_):
                global h_ini
                if h_ini == "00":
                    h_ini = "99"
                else:
                    h_ini = parseTime(str(int(h_ini) - 1), m_ini, s_ini)[0]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(295, 150, 310, 170, 325, 150, tags="h_down")
            canvas.tag_bind("h_down", "<Button-1>", fh_down)

            def fM_down(_):
                global m_ini
                if int(m_ini) < 10:
                    resto = int(m_ini) % 10
                    m_ini = "5" + str(resto)
                else:
                    m_ini = parseTime(h_ini, str(int(m_ini) - 10), s_ini)[1]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(360, 150, 375, 170, 390, 150, tags="M_down")
            canvas.tag_bind("M_down", "<Button-1>", fM_down)

            def fm_down(_):
                global m_ini
                if m_ini == "00":
                    m_ini = "59"
                else:
                    m_ini = parseTime(h_ini, str(int(m_ini) - 1), s_ini)[1]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(405, 150, 420, 170, 435, 150, tags="m_down")
            canvas.tag_bind("m_down", "<Button-1>", fm_down)

            def fS_down(_):
                global s_ini
                if int(s_ini) < 10:
                    resto = int(s_ini) % 10
                    s_ini = "5" + str(resto)
                else:
                    s_ini = parseTime(h_ini, m_ini, str(int(s_ini) - 10))[2]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(470, 150, 485, 170, 500, 150, tags="S_down")
            canvas.tag_bind("S_down", "<Button-1>", fS_down)

            def fs_down(_):
                global s_ini
                if s_ini == "00":
                    s_ini = "59"
                else:
                    s_ini = parseTime(h_ini, m_ini, str(int(s_ini) - 1))[2]
                lv.configure(text=h_ini+":"+m_ini+":"+s_ini)

            canvas.create_polygon(515, 150, 530, 170, 545, 150, tags="s_down")
            canvas.tag_bind("s_down", "<Button-1>", fs_down)

        if 190 < y <= 380:
            print("pico pal que lee")
        if 380 < y <= 570:
            print("pico pal que baila")

    def homeBtn():
        global cfg_Mode
        cfg_Mode = False
        canvas.move(vertical, -20, 0)
        primer_frame[0].configure(text="PRÓXIMA")
        primer_frame[0].place(x=40, y=50)
        primer_frame[1].configure(text="DESCARGA")
        primer_frame[1].place(x=30, y=80)
        primer_frame[2].configure(text="EN:")
        primer_frame[2].place(x=80, y=110)
        segundo_frame[0].configure(text="PROGRAMADO")
        segundo_frame[0].place(x=5, y=250)
        segundo_frame[1].configure(text="PARA EL:")
        segundo_frame[1].place(x=30, y=280)
        # aqui debo hacer el countdown de nuevo con los parametros h_ini, m_ini, s_ini nuevos
        return None

    ventana.bind('<Button-1>', seccion_handler)

    b1 = Button(ventana, text="Configuración", command=test, bg=bg_color, font=("System", 10))
    b1.place(x=310, y=565)
    b2 = Button(ventana, text="Inicio", command=homeBtn, bg=bg_color, font=("System", 10))
    b2.place(x=415, y=565)
    b3 = Button(ventana, text="Regresar", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b3.place(x=465, y=565)
    b4 = Button(ventana, text="Apagar", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b4.place(x=540, y=565)

    countdown(h_ini, m_ini, s_ini, 240, 40, 0, lv, wait_label)

mainWindow()
ventana.mainloop()
