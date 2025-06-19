#!/usr/bin/python3
#
# Da de alta (añade) una factura a la base de datos.
#
import sys
import time
import os.path
import facturas

FECHA_FORMATO = "%d/%m/%Y"

# Argumentos de entrada
if len(sys.argv) == 2:
   doc_ruta = sys.argv[1]
else:
   print("Da de alta (añade) una factura a la base de datos.")
   sys.exit("Uso: altafac.py <documento.pdf>")

if not os.path.isfile(doc_ruta):
   sys.exit("Documento no encontrado.")

fac_num = input("Introduce el número de factura: ")
if fac_num == "":
   sys.exit("Número de factura requerido.")
   
fac_fecha_def = time.strftime(FECHA_FORMATO)
fac_fecha = input("Fecha de expedición de la factura [" + fac_fecha_def + "]: ")
if fac_fecha == "":
   fac_fecha = fac_fecha_def
else:
   try:
      fecha = time.strptime(fac_fecha, FECHA_FORMATO)
   except ValueError:
      try:
         fecha = time.strptime(fac_fecha, FECHA_FORMATO)
      except ValueError:
         sys.exit("Formato de fecha no reconocido.")
   fac_fecha = time.strftime(FECHA_FORMATO, fecha)

# Crear entrada en la base de datos
facturas.creaRegistro(facturas.OP_ALTA, doc_ruta, fac_fecha, fac_num)
print("Factura registrada correctamente.")

