## 4.2 ¿Qué es la serialización de datos en Python? ¿Para qué se utiliza?
La serialización es el proceso de convertir estructuras de datos como objetos o diccionarios a un formato que es mas sencillo de transmitir o almacenar, 
algunos formatos para la serialización que existen son JSON, XML o pickle en Python.

La serialización es usada a través de internet para transmitir datos de forma que no requieran un gran ancho de banda, por ejemplo, 
la gran mayoría de las API sirven sus datos en formato JSON. 

Por otro lado, Django REST framework utiliza la serialización de datos para convertir querys de base de datos a tipos de datos de Python 
que luego pueden ser renderizados como JSON o XML.
