
#Importación de librerías:

from Proyecto import proyecto
from Conexion import Conexion
from tkinter import messagebox as mb





class BDatos:
    SELECCIONAR = 'SELECT * FROM proyecto'
    INSERTAR = 'INSERT INTO proyecto(descripcion,tematica,academia,prioridad,fecha_inicio,fecha_fin) VALUES(%s, %s, %s,%s, %s, %s)'
    ACTUALIZAR = 'UPDATE proyecto SET descripcion=%s, tematica=%s, academia=%s,prioridad=%s, fecha_inicio=%s, fecha_fin=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM proyecto WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            proyectos = []
            for registro in registros:
                Proyecto = proyecto(registro[0], registro[1],
                                  registro[2], registro[3],
                                  registro[4], registro[5],registro[6])
                proyectos.append(Proyecto)
            return proyectos
        except Exception as e:
            mb.showerror('Error', message='Ocurrio un error al seleccionar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, proyec):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (proyec.descripcion, proyec.tematica,proyec.academia,proyec.prioridad,proyec.fecha_inicio,proyec.fecha_fin)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
             mb.showerror('Error', message='Ocurrio un error al insertar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, proyec):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (proyec.descripcion, proyec.tematica,proyec.academia,proyec.prioridad,proyec.fecha_inicio,proyec.fecha_fin)
                     
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            mb.showerror('Error', message='Ocurrio un error al actualizar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, proyec):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (proyec.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            mb.showerror('Error', message='Ocurrio un error al borrar clientes')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':

    proyectos = proyecto.seleccionar()
    for proyecto in proyectos:
        print(proyecto)