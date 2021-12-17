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

# cantidad default de sal a dispensar (en gramos)
# puede ser editada desde aqui o desde el menu config
sal_default = "50"
sal_disponible = "1000"

# periodo default de dispensacion (1 dia)
# d=dia h=hora m=minuto s=segundo w=semana mo=mes
# lo mismo de antes aplica para esta opcion
periodo_default = "1d"

# si el modo config esta activado o no
cfg_Mode = False

ventana = Tk()
ventana.geometry("600x600")
ventana.title("Dispensador de sal de polifosfato - DEMO (E19 Kakosbathiophobia CD1201-3)")
ventana.configure(background=bg_color)

def mainWindow():
    def obtenerId(periodo):
        return ''.join([i for i in periodo if not i.isdigit()])

    def obtenerNumero(periodo):
        return ''.join([i for i in periodo if i.isdigit()])

    def traducirPeriodo(periodo):
        periodo_len = len(obtenerId(periodo))
        # cant es la cantidad e id puede ser "s", "m", "h", etc
        cant, id = periodo[0:-periodo_len], periodo[-periodo_len:]
        traducciones = { "h": "hr", "w": "sem", "d": "día", "mo": "mes" }
        if int(cant) != 1 and id != "w":
            if id != "mo":
                id = traducciones[id] + "s"
            else:
                id = traducciones[id] + "es"
        else:
            id = traducciones[id]

        return cant + " " + id

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
        canvas.create_text((45, 570), font=("System", 10), text=curr_fecha)
        canvas.create_text((45, 585), font=("System", 10), text=curr_hora)
        #l4 = Label(ventana, text=curr_hora, font=("System", 10))
        #l4.place(x=25, y=560.5)
        #l4 = Label(ventana, text=curr_fecha, font=("System", 10))
        #l4.place(x=10, y=570.5)
        #l4.after(1000, actualizarReloj)

    actualizarReloj()

    l6 = Label(ventana, text="56%", bg=bg_color, font=("System", 10))
    l6.place(x=130, y=567.5)

    sal_label = Label(ventana, text="Disp.: "+sal_disponible+"mg ("+sal_default+"mg por periodo)", \
                      bg=bg_color, font=("System", 10))
    sal_label.place(x=180, y=567.5)

    # De aqui para abajo, incluyendo countdown(h,m,s), hace que el tiempo de dispensacion baje.
    # str str str int int int Label Label -> None
    def countdown(h, m, s, x, y, stage, main_label, second_label):
        global cfg_Mode, sal_disponible
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
                        if int(sal_disponible) - int(sal_default) >= 0:
                            sal_disponible = str(int(sal_disponible) - int(sal_default))
                            sal_label.configure(text="Disp.: "+sal_disponible+"mg ("+sal_default+"mg por periodo)")
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

    # widgets contiene todos los botones y flechas usadas, para borrarlo dps
    widgets = []
    def configMenu():
        global cfg_Mode
        if cfg_Mode:
            return
        cfg_Mode = True
        canvas.move(vertical, 20, 0)
        L = Label(ventana, text="MODIFICAR", bg=bg_color, font=("System", 20))
        widgets.append(L)
        L.place(x=30, y=50)
        primer_frame[0].configure(text="PERIODO DE")
        primer_frame[0].place(x=20, y=80)
        primer_frame[1].configure(text="DISPENSACION:")
        primer_frame[1].place(x=5, y=110)
        primer_frame[2].configure(text="")
        primer_frame[2].place(x=5, y=110)
        primer_frame[3].configure(text=traducirPeriodo(periodo_default))
        primer_frame[3].place(x=290, y=40)
        L = Label(ventana, text="MODIFICAR", bg=bg_color, font=("System", 20))
        widgets.append(L)
        L.place(x=30, y=240)
        segundo_frame[0].configure(text="CANT. DE SAL A")
        segundo_frame[0].place(x=10, y=270)
        segundo_frame[1].configure(text="DISPENSAR:")
        segundo_frame[1].place(x=30, y=300)
        segundo_frame[2].configure(text="")
        segundo_frame[3].configure(text=sal_default + " mg")
        segundo_frame[3].place(x=260, y=230)
        L = Label(ventana, text="MODIFICAR", bg=bg_color, font=("System", 20))
        widgets.append(L)
        L.place(x=30, y=420)
        tercer_frame[0].place(x=30, y=450)
        tercer_frame[1].place(x=50, y=480)
        tercer_frame[2].configure(text=h_wt+":"+m_wt+":"+s_wt)
        tercer_frame[2].place(x=255, y=410)

        def hrsFn():
            global periodo_default
            periodo_default = obtenerNumero(periodo_default) + "h"
            primer_frame[3].configure(text=traducirPeriodo(periodo_default))

        B = Button(ventana, text="Horas", command=hrsFn, bg=bg_color, font=("System", 10))
        widgets.append(B)
        B.place(x=270, y=150)

        def diasFn():
            global periodo_default
            num = obtenerNumero(periodo_default)
            if int(num) > 7:
                num = "7"
            periodo_default = num + "d"
            primer_frame[3].configure(text=traducirPeriodo(periodo_default))

        B = Button(ventana, text="Días", command=diasFn, bg=bg_color, font=("System", 10))
        widgets.append(B)
        B.place(x=330, y=150)

        def semanasFn():
            global periodo_default
            num = obtenerNumero(periodo_default)
            if int(num) > 4:
                num = "4"
            periodo_default = num + "w"
            primer_frame[3].configure(text=traducirPeriodo(periodo_default))
            primer_frame[3].place(x=260, y=40)

        B = Button(ventana, text="Semanas", command=semanasFn, bg=bg_color, font=("System", 10))
        widgets.append(B)
        B.place(x=380, y=150)

        def mesesFn():
            global periodo_default
            num = obtenerNumero(periodo_default)
            if int(num) > 12:
                num = "12"
            periodo_default = num + "mo"
            primer_frame[3].configure(text=traducirPeriodo(periodo_default))

        B = Button(ventana, text="Meses", command=mesesFn, bg=bg_color, font=("System", 10))
        widgets.append(B)
        B.place(x=460, y=150)

        def fperiodo_up(_):
            global periodo_default
            id = obtenerId(periodo_default)
            num = obtenerNumero(periodo_default)
            new_x, new_y = 0, 0
            if id == "h":
                if int(num) == 24:
                    periodo_default = "1h"
                else:
                    periodo_default = str(int(num) + 1) + "h"
                if int(num) < 9:
                    new_x, new_y = 280, 40
                else:
                    new_x, new_y = 260, 40
            elif id == "d":
                if int(num) == 7:
                    periodo_default = "1d"
                else:
                    periodo_default = str(int(num) + 1) + "d"
                new_x, new_y = 270, 40
            elif id == "w":
                if int(num) == 4:
                    periodo_default = "1w"
                else:
                    periodo_default = str(int(num) + 1) + "w"
                new_x, new_y = 260, 40
            elif id == "mo":
                if int(num) == 12:
                    periodo_default = "1mo"
                else:
                    periodo_default = str(int(num) + 1) + "mo"
                new_x, new_y = 280, 40
            primer_frame[3].configure(text=traducirPeriodo(periodo_default))
            primer_frame[3].place(x=new_x, y=new_y)

        P = canvas.create_polygon(520, 60, 535, 40, 550, 60, tags="periodo_up")
        widgets.append(P)
        canvas.tag_bind("periodo_up", "<Button-1>", fperiodo_up)

        def fperiodo_down(_):
            global periodo_default
            id = obtenerId(periodo_default)
            num = obtenerNumero(periodo_default)
            new_x, new_y = 0, 0
            if id == "h":
                if int(num) == 1:
                    periodo_default = "24h"
                else:
                    periodo_default = str(int(num) - 1) + "h"
                if int(num) < 10:
                    new_x, new_y = 270, 40
                else:
                    new_x, new_y = 260, 40
            elif id == "d":
                if int(num) == 1:
                    periodo_default = "7d"
                else:
                    periodo_default = str(int(num) - 1) + "d"
                new_x, new_y = 270, 40
            elif id == "w":
                if int(num) == 1:
                    periodo_default = "4w"
                else:
                    periodo_default = str(int(num) - 1) + "w"
                new_x, new_y = 260, 40
            elif id == "mo":
                if int(num) == 1:
                    periodo_default = "12mo"
                else:
                    periodo_default = str(int(num) - 1) + "mo"
                new_x, new_y = 280, 40
            primer_frame[3].configure(text=traducirPeriodo(periodo_default))
            primer_frame[3].place(x=new_x, y=new_y)

        P = canvas.create_polygon(520, 130, 535, 150, 550, 130, tags="periodo_down")
        widgets.append(P)
        canvas.tag_bind("periodo_down", "<Button-1>", fperiodo_down)

        def fsal_up(_):
            global sal_default
            if int(sal_default) == 120:
                sal_default = "25"
            else:
                sal_default = str(int(sal_default) + 1)
            segundo_frame[3].configure(text=sal_default + " mg")
            if int(sal_default) >= 100:
                segundo_frame[3].place(x=240, y=230)
            else:
                segundo_frame[3].place(x=260, y=230)

        P = canvas.create_polygon(520, 250, 535, 230, 550, 250, tags="sal_up")
        widgets.append(P)
        canvas.tag_bind("sal_up", "<Button-1>", fsal_up)

        def fsal_down(_):
            global sal_default
            if int(sal_default) == 25:
                sal_default = "120"
            else:
                sal_default = str(int(sal_default) - 1)
            segundo_frame[3].configure(text=sal_default + " mg")
            if int(sal_default) >= 100:
                segundo_frame[3].place(x=240, y=230)
            else:
                segundo_frame[3].place(x=260, y=230)

        P = canvas.create_polygon(520, 320, 535, 340, 550, 320, tags="sal_down")
        widgets.append(P)
        canvas.tag_bind("sal_down", "<Button-1>", fsal_down)

        def fH_up(_):
            global h_wt
            if int(h_wt) >= 90:
                resto = int(h_wt) % 10
                h_wt = "0" + str(resto)
            else:
                h_wt = str(int(h_wt) + 10)
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(265, 410, 280, 390, 295, 410, tags="H_up")
        widgets.append(P)
        canvas.tag_bind("H_up", "<Button-1>", fH_up)

        def fh_up(_):
            global h_wt
            if int(h_wt) == 99:
                h_wt = "00"
            else:
                h_wt = parseTime(str(int(h_wt) + 1), m_wt, s_wt)[0]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(310, 410, 325, 390, 340, 410, tags="h_up")
        widgets.append(P)
        canvas.tag_bind("h_up", "<Button-1>", fh_up)

        def fM_up(_):
            global m_wt
            if int(m_wt) >= 50:
                resto = int(m_wt) % 10
                m_wt = "0" + str(resto)
            else:
                m_wt = str(int(m_wt) + 10)
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(375, 410, 390, 390, 405, 410, tags="M_up")
        widgets.append(P)
        canvas.tag_bind("M_up", "<Button-1>", fM_up)

        def fm_up(_):
            global m_wt
            if int(m_wt) == 59:
                m_wt = "00"
            else:
                m_wt = parseTime(h_wt, str(int(m_wt) + 1), s_wt)[1]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(420, 410, 435, 390, 450, 410, tags="m_up")
        widgets.append(P)
        canvas.tag_bind("m_up", "<Button-1>", fm_up)

        def fS_up(_):
            global s_wt
            if int(s_wt) >= 50:
                resto = int(s_wt) % 10
                s_wt = "0" + str(resto)
            else:
                s_wt = str(int(s_wt) + 10)
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(485, 410, 500, 390, 515, 410, tags="S_up")
        widgets.append(P)
        canvas.tag_bind("S_up", "<Button-1>", fS_up)

        def fs_up(_):
            global s_wt
            if int(s_wt) == 59:
                s_wt = "00"
            else:
                s_wt = parseTime(h_wt, m_wt, str(int(s_wt) + 1))[2]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(530, 410, 545, 390, 560, 410, tags="s_up")
        widgets.append(P)
        canvas.tag_bind("s_up", "<Button-1>", fs_up)

        # Flechas pa abajo
        def fH_down(_):
            global h_wt
            if int(h_wt) < 10:
                resto = int(h_wt) % 10
                h_wt = "9" + str(resto)
            else:
                h_wt = parseTime(str(int(h_wt) - 10), m_wt, s_wt)[0]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(265, 520, 280, 540, 295, 520, tags="H_down")
        widgets.append(P)
        canvas.tag_bind("H_down", "<Button-1>", fH_down)

        def fh_down(_):
            global h_wt
            if h_wt == "00":
                h_wt = "99"
            else:
                h_wt = parseTime(str(int(h_wt) - 1), m_wt, s_wt)[0]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(310, 520, 325, 540, 340, 520, tags="h_down")
        widgets.append(P)
        canvas.tag_bind("h_down", "<Button-1>", fh_down)

        def fM_down(_):
            global m_wt
            if int(m_wt) < 10:
                resto = int(m_wt) % 10
                m_wt = "5" + str(resto)
            else:
                m_wt = parseTime(h_wt, str(int(m_wt) - 10), s_wt)[1]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(375, 520, 390, 540, 405, 520, tags="M_down")
        widgets.append(P)
        canvas.tag_bind("M_down", "<Button-1>", fM_down)

        def fm_down(_):
            global m_wt
            if m_wt == "00":
                m_wt = "59"
            else:
                m_wt = parseTime(h_wt, str(int(m_wt) - 1), s_wt)[1]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(420, 520, 435, 540, 450, 520, tags="m_down")
        widgets.append(P)
        canvas.tag_bind("m_down", "<Button-1>", fm_down)

        def fS_down(_):
            global s_wt
            if int(s_wt) < 10:
                resto = int(s_wt) % 10
                s_wt = "5" + str(resto)
            else:
                s_wt = parseTime(h_wt, m_wt, str(int(s_wt) - 10))[2]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(485, 520, 500, 540, 515, 520, tags="S_down")
        widgets.append(P)
        canvas.tag_bind("S_down", "<Button-1>", fS_down)

        def fs_down(_):
            global s_wt
            if s_wt == "00":
                s_wt = "59"
            else:
                s_wt = parseTime(h_wt, m_wt, str(int(s_wt) - 1))[2]
            tercer_frame[2].configure(text=h_wt + ":" + m_wt + ":" + s_wt)

        P = canvas.create_polygon(530, 520, 545, 540, 560, 520, tags="s_down")
        widgets.append(P)
        canvas.tag_bind("s_down", "<Button-1>", fs_down)

    def homeBtn():
        global cfg_Mode
        if not cfg_Mode:
            return
        cfg_Mode = False
        # borramos todos los widgets de la config
        for widget in widgets:
            if type(widget) == int:
                canvas.delete(widget)
            else:
                widget.destroy()
        canvas.move(vertical, -20, 0)
        # Por si modifico la cant. de sal
        sal_label.configure(text="Disp.: " + sal_disponible + "mg (" + sal_default + "mg por periodo)")
        # Primer frame
        primer_frame[0].configure(text="PRÓXIMA")
        primer_frame[0].place(x=40, y=50)
        primer_frame[1].configure(text="DESCARGA")
        primer_frame[1].place(x=30, y=80)
        primer_frame[2].configure(text="EN:")
        primer_frame[2].place(x=80, y=110)
        primer_frame[3].configure(text=h_ini + ":" + m_ini + ":" + s_ini)
        primer_frame[3].place(x=240, y=40)
        timestamp = time()
        timestamp += toTimestamp(h_ini, m_ini, s_ini)
        n_hora = obtenerHora(timestamp)
        n_fecha = obtenerFecha(timestamp)
        # Segundo frame
        segundo_frame[0].configure(text="PROGRAMADO")
        segundo_frame[0].place(x=5, y=250)
        segundo_frame[1].configure(text="PARA EL:")
        segundo_frame[1].place(x=30, y=280)
        segundo_frame[2].configure(text=n_fecha + " A LAS:")
        segundo_frame[2].place(x=220, y=210)
        segundo_frame[3].configure(text=n_hora)
        segundo_frame[3].place(x=240, y=260)
        # Tercer frame
        tercer_frame[0].place(x=20, y=430)
        tercer_frame[1].place(x=40, y=460)
        tercer_frame[2].configure(text="--:--:--")
        tercer_frame[2].place(x=290, y=410)

        countdown(h_ini, m_ini, s_ini, 240, 40, 0, primer_frame[3], tercer_frame[2])

    b1 = Button(ventana, text="Ajustes", command=configMenu, bg=bg_color, font=("System", 10))
    b1.place(x=420, y=565)
    b2 = Button(ventana, text="Inicio", command=homeBtn, bg=bg_color, font=("System", 10))
    b2.place(x=487, y=565)
    b4 = Button(ventana, text="Apagar", command=ventana.destroy, bg=bg_color, font=("System", 10))
    b4.place(x=540, y=565)

    countdown(h_ini, m_ini, s_ini, 240, 40, 0, lv, wait_label)

mainWindow()
ventana.mainloop()
