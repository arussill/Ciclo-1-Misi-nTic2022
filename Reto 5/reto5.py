# -*- coding: utf-8 -*-
"""reto5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KDkbdrAYtBe_loFvrFdfZENG2CeSc-Kj
"""

""" Reto 5 """
"""===============================INICIALIZACIONES============================================"""

import pandas as pd
import numpy as np

"""==================================ENTRADAS============================"""

archivo = pd.read_csv('data.csv')#leyendo el archivo con pandas
entrada = input().split()#varios números identificadores de distintas sucursales.
entrada = [int(i) for i in entrada] #funcion que cambia los str de una lista a tipo  int
entrada.sort()

"""================================FUNCIONES======================================="""

def salida_1(x,df):#Funcion que calcula id_branch, city_name, department_name
  condicion = (df[df["id_branch"] == x]).head(1)
  resultado = condicion[["id_branch", "city_name", "department_name"]]
  for i in resultado.index:
    sucursal = resultado["id_branch"][i]
    ciudad = resultado["city_name"][i]
    departamento = resultado["department_name"][i]
  return (sucursal, ciudad, departamento)

def salida_3_4_5(x,df):#Funcion que calcula la cantidad de hombres y mujeres y el total de pacientes que solicitaron medicamentos
  cantidad_male, cantidad_female  = 0, 0
  condicion = (df[df["id_branch"] == x])
  resultado = condicion[["gender"]]
  for i in resultado.index:
    if resultado.loc[i, "gender"] == "m":
      cantidad_male += 1
    if resultado.loc[i, "gender"] == "f":
      cantidad_female += 1
    total = cantidad_male + cantidad_female
  return (cantidad_male, cantidad_female, total)

def salida_7_8_9_10_11(x,df):#Funcion que calcula el mean, std, min, max, total de los medicamentos solicitados en esa sucursal sin importar tipo
  lista = []
  condicion = (df[df["id_branch"] == x])
  promedio = condicion["medicine_quantity"].mean()
  desviacion = condicion["medicine_quantity"].std()
  minimo = condicion["medicine_quantity"].min()
  maximo = condicion["medicine_quantity"].max()
  total = condicion["medicine_quantity"].sum()
  return (promedio, desviacion, minimo, maximo, total)

def salida_13_14_15(x,df):#Funcion que calcula m, f y totla de pacientes programados
  cantidad_male, cantidad_female = 0, 0
  condicion = (df[df["id_branch"] == x])
  resultado = condicion[["gender", "systolic_pressure", "diastolic_pressure"]]
  for i in resultado.index:
    comprobante = categoria(resultado.loc[i,"systolic_pressure"],resultado.loc[i,"diastolic_pressure"])
    if comprobante == True and resultado.loc[i, "gender"] == "m":
        cantidad_male +=1
    if comprobante == True and resultado.loc[i, "gender"] == "f":
      if comprobante == True:
        cantidad_female +=1
  total = cantidad_male + cantidad_female
  return (cantidad_male, cantidad_female, total)

def salida_17_18_19_20_21(x,df):#Funcion que calcula mean, std, min, max, total de los medicamentos programados
  lista = []
  condicion = (df[df["id_branch"] == x])
  resultado = condicion[["systolic_pressure", "diastolic_pressure", "medicine_quantity"]]
  for i in resultado.index:
    comprobante = categoria(resultado.loc[i,"systolic_pressure"],resultado.loc[i,"diastolic_pressure"])
    if comprobante == True:
      lista.append(resultado.loc[i,"medicine_quantity"])
  promedio = np.mean(lista)
  desviacion = np.std(lista, ddof=1)
  minimo = min(lista)
  maximo = max(lista)
  total = sum(lista)
  return (promedio, desviacion, minimo, maximo, total)

def datos_min(x,df,minimo):#Funcion que entrega nombre, apellido,genero y tipo de medicamento del valor min_programada
  name_min, last_name_min = [], []
  gender_min, type_min = [], []
  condicion = (df[df["id_branch"] == x])
  resultado = condicion[["first_name","last_name","gender","medicine_type","systolic_pressure", "diastolic_pressure", "medicine_quantity"]]
  for i in resultado.index:
    comprobante = categoria(resultado.loc[i,"systolic_pressure"],resultado.loc[i,"diastolic_pressure"])
    if comprobante == True:
      if minimo == resultado.loc[i,"medicine_quantity"]:
        name_min.append(resultado.loc[i,"first_name"])
        last_name_min.append(resultado.loc[i,"last_name"])
        gender_min.append(resultado.loc[i,"gender"])
        type_min.append(resultado.loc[i,"medicine_type"])
  nombre = name_min[0]
  apellido = last_name_min[0]
  genero = gender_min[0]
  tipo = type_min[0]
  return (nombre, apellido, genero, tipo)

def datos_max(x,df,maximo):#Funcion que entrega nombre, apellido,genero y tipo de medicamento del valor max_programada
  name_max, last_name_max = [], []
  gender_max, type_max = [], []
  condicion = (df[df["id_branch"] == x])
  resultado = condicion[["first_name","last_name","gender","medicine_type","systolic_pressure", "diastolic_pressure", "medicine_quantity"]]
  for i in resultado.index:
    comprobante = categoria(resultado.loc[i,"systolic_pressure"],resultado.loc[i,"diastolic_pressure"])
    if comprobante == True: 
      if maximo == resultado.loc[i,"medicine_quantity"]:
          name_max.append(resultado.loc[i,"first_name"])
          last_name_max.append(resultado.loc[i,"last_name"])
          gender_max.append(resultado.loc[i,"gender"])
          type_max.append(resultado.loc[i,"medicine_type"])
  nombre = name_max[0]
  apellido = last_name_max[0]
  genero = gender_max[0]
  tipo = type_max[0]
  return (nombre, apellido, genero, tipo)

"""===================================CATEGORIA_DE_PRESIONES====================================="""
def categoria(presion_1, presion_2):
  if (presion_1 < 90) and (presion_2 < 70): 
    programa = True
  elif (90 <= presion_1 < 130) and (70 <= presion_2 < 90): 
    programa = False
  elif (130 <= presion_1 < 140) and (90 <= presion_2 < 95): 
    programa = False
  elif (140 <= presion_1 < 150) and (95 <= presion_2 < 100):
    programa = True            
  elif (150 <= presion_1 < 170) and (100 <= presion_2 < 110):
    programa = True            
  elif (170 <= presion_1 < 190) and (110 <= presion_2 < 120):
    programa = True            
  elif (presion_1 >= 190) and (presion_2 >= 120):
    programa = True            
  elif (presion_1 >= 150) and (presion_2 < 100):
    programa = True            
  else: #Sin categoria
    programa = False
  return programa

"""====================================SALIDAS================================"""

for elemento in entrada:
  sucursal, ciudad, departamento = salida_1(elemento,archivo)
  cantidad_m, cantidad_f, total_pacientes = salida_3_4_5(elemento,archivo)
  promedio_medicamentos, std_medicamentos, min_medicamentos, max_medicamentos, total_medicamentos = salida_7_8_9_10_11(elemento,archivo)
  cantidad_m_programada, cantidad_f_programada, total_pacientes_programados = salida_13_14_15(elemento, archivo)
  promedio_medicamentos_programados, std_medicamentos_programados, min_medicamentos_programados, max_medicamentos_programados, total_medicamentos_programados = salida_17_18_19_20_21(elemento, archivo)
  nombre_min, apellido_min, genero_min, tipo_min = datos_min(elemento,archivo,min_medicamentos_programados)
  nombre_max, apellido_max, genero_max, tipo_max = datos_max(elemento,archivo,max_medicamentos_programados)

  print(sucursal, ciudad, departamento)#salida 1
  print("patients")#salida 2
  print("male", cantidad_m)#salida 3
  print("female", cantidad_f)#salida 4
  print("total", total_pacientes)#salida 5
  print("medicine quantity")#salida 6
  print("mean", "{0:.2f}".format(promedio_medicamentos))#salida 7
  print("std", "{0:.2f}".format(std_medicamentos))#salida 8
  print("min", min_medicamentos)#salida 9
  print("max", max_medicamentos)#salida 10
  print("total", total_medicamentos)#salida 11
  print("scheduled patients")#salida 12
  print("male", cantidad_m_programada)#salida 13
  print("female", cantidad_f_programada)#salida 14
  print("total", total_pacientes_programados)#salida 15
  print("scheduled medicine quantity")#salida 16
  print("mean", "{0:.2f}".format(promedio_medicamentos_programados))#salida 17
  print("std", "{0:.2f}".format(std_medicamentos_programados))#salida 18
  print("min", min_medicamentos_programados, nombre_min, apellido_min, genero_min, tipo_min)#salida 19
  print("max", max_medicamentos_programados, nombre_max, apellido_max, genero_max, tipo_max)#salida 20
  print("total", total_medicamentos_programados)#salida 21