import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
from modelos.grupo import Grupo
from modelos.actividad import Actividad

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Digital Docente")
        self.root.geometry("700x500")

        # --- Datos en memoria ---
        self.grupos = []
        self.actividades = []

        self.archivo_grupos = "datos/grupos.csv"
        self.archivo_actividades = "datos/actividades.csv"

        self.cargar_datos()

        # --- Menú principal ---
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        menu_grupos = tk.Menu(barra_menu, tearoff=0)
        menu_grupos.add_command(label="Registrar grupo", command=self.ventana_agregar_grupo)
        menu_grupos.add_command(label="Ver grupos", command=self.mostrar_grupos)
        barra_menu.add_cascade(label="Grupos", menu=menu_grupos)

        menu_actividades = tk.Menu(barra_menu, tearoff=0)
        menu_actividades.add_command(label="Registrar actividad", command=self.ventana_agregar_actividad)
        menu_actividades.add_command(label="Ver actividades", command=self.mostrar_actividades)
        barra_menu.add_cascade(label="Actividades", menu=menu_actividades)

        self.frame_principal = ttk.Frame(self.root, padding=10)
        self.frame_principal.pack(fill="both", expand=True)

        self.mostrar_bienvenida()

    # ===============================
    #       SECCIÓN DE DATOS
    # ===============================
    def cargar_datos(self):
        """Carga grupos y actividades desde CSV"""
        if os.path.exists(self.archivo_grupos):
            with open(self.archivo_grupos, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    grupo = Grupo(
                        id_grupo=fila["id"],
                        nombre=fila["nombre"],
                        asignatura=fila["asignatura"],
                        turno=fila["turno"],
                        horario=fila["horario"]
                    )
                    self.grupos.append(grupo)

        if os.path.exists(self.archivo_actividades):
            with open(self.archivo_actividades, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    act = Actividad(
                        id_actividad=fila["id_actividad"],
                        id_grupo=fila["id_grupo"],
                        fecha=fila["fecha"],
                        descripcion=fila["descripcion"],
                        estado=fila["estado"]
                    )
                    self.actividades.append(act)

    def guardar_grupos(self):
        """Guarda los grupos en CSV"""
        with open(self.archivo_grupos, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nombre", "asignatura", "turno", "horario"])
            for g in self.grupos:
                writer.writerow([g.id_grupo, g.nombre, g.asignatura, g.turno, g.horario])

    def guardar_actividades(self):
        """Guarda las actividades en CSV"""
        with open(self.archivo_actividades, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id_actividad", "id_grupo", "fecha", "descripcion", "estado"])
            for a in self.actividades:
                writer.writerow([a.id_actividad, a.id_grupo, a.fecha, a.descripcion, a.estado])

    # ===============================
    #        PANTALLAS
    # ===============================
    def limpiar_pantalla(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

    def mostrar_bienvenida(self):
        self.limpiar_pantalla()
        ttk.Label(self.frame_principal, text="Agenda Digital Docente", font=("Arial", 20)).pack(pady=50)
        ttk.Label(self.frame_principal, text="Seleccione una opción en el menú superior.").pack()

    def mostrar_grupos(self):
        self.limpiar_pantalla()
        ttk.Label(self.frame_principal, text="Listado de grupos", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.frame_principal, columns=("ID", "Nombre", "Asignatura", "Turno", "Horario"), show="headings")
        tree.pack(fill="both", expand=True)
        for col in tree["columns"]:
            tree.heading(col, text=col)
        for g in self.grupos:
            tree.insert("", tk.END, values=(g.id_grupo, g.nombre, g.asignatura, g.turno, g.horario))

    def mostrar_actividades(self):
        self.limpiar_pantalla()
        ttk.Label(self.frame_principal, text="Listado de actividades", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.frame_principal, columns=("ID", "Grupo", "Fecha", "Descripción", "Estado"), show="headings")
        tree.pack(fill="both", expand=True)
        for col in tree["columns"]:
            tree.heading(col, text=col)
        for a in self.actividades:
            tree.insert("", tk.END, values=(a.id_actividad, a.id_grupo, a.fecha, a.descripcion, a.estado))

    # ===============================
    #     FORMULARIOS DE REGISTRO
    # ===============================
    def ventana_agregar_grupo(self):
        win = tk.Toplevel(self.root)
        win.title("Registrar Grupo")
        win.geometry("400x300")

        ttk.Label(win, text="ID Grupo").pack()
        id_entry = ttk.Entry(win)
        id_entry.pack()

        ttk.Label(win, text="Nombre").pack()
        nombre_entry = ttk.Entry(win)
        nombre_entry.pack()

        ttk.Label(win, text="Asignatura").pack()
        asignatura_entry = ttk.Entry(win)
        asignatura_entry.pack()

        ttk.Label(win, text="Turno").pack()
        turno_entry = ttk.Entry(win)
        turno_entry.pack()

        ttk.Label(win, text="Horario").pack()
        horario_entry = ttk.Entry(win)
        horario_entry.pack()

        def guardar():
            grupo = Grupo(
                id_grupo=id_entry.get(),
                nombre=nombre_entry.get(),
                asignatura=asignatura_entry.get(),
                turno=turno_entry.get(),
                horario=horario_entry.get()
            )
            self.grupos.append(grupo)
            self.guardar_grupos()
            messagebox.showinfo("Éxito", "Grupo registrado correctamente")
            win.destroy()

        ttk.Button(win, text="Guardar", command=guardar).pack(pady=10)

    def ventana_agregar_actividad(self):
        win = tk.Toplevel(self.root)
        win.title("Registrar Actividad")
        win.geometry("400x350")

        ttk.Label(win, text="ID Actividad").pack()
        id_entry = ttk.Entry(win)
        id_entry.pack()

        ttk.Label(win, text="Grupo").pack()
        grupo_combo = ttk.Combobox(win, values=[g.id_grupo for g in self.grupos])
        grupo_combo.pack()

        ttk.Label(win, text="Fecha (YYYY-MM-DD)").pack()
        fecha_entry = ttk.Entry(win)
        fecha_entry.pack()

        ttk.Label(win, text="Descripción").pack()
        desc_entry = ttk.Entry(win)
        desc_entry.pack()

        ttk.Label(win, text="Estado").pack()
        estado_combo = ttk.Combobox(win, values=["Pendiente", "Realizada", "Reprogramada"])
        estado_combo.pack()

        def guardar():
            act = Actividad(
                id_actividad=id_entry.get(),
                id_grupo=grupo_combo.get(),
                fecha=fecha_entry.get(),
                descripcion=desc_entry.get(),
                estado=estado_combo.get()
            )
            self.actividades.append(act)
            self.guardar_actividades()
            messagebox.showinfo("Éxito", "Actividad registrada correctamente")
            win.destroy()

        ttk.Button(win, text="Guardar", command=guardar).pack(pady=10)

# EJECUCIÓN
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
