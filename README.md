# Programa de Simulación de lo Clásico a lo Cuántico

## Descripción 📑
---
Esta es un proyecto que contiene funciones para simular experimentos determinísticos, probabilísticos y cuánticos con posiciones de canicas o partículas en un número determinado de cajas, rendijas u otros lugares en el espacio.  

## Tabla de Contenidos 🗂️
---
Experimentos incluidos:

1. Canicas con coeficientes booleanos
2. Clásico probabilístico con múltiples rendijas
3. Cuántico con múltiples rendijas

## Requisitos 🧾
---
Para poder implementar la librería en su máquina local, se recomienda tener las siguientes ***especificaciones mínimas***:

- **Sistema Operativo:** Windows 8.1 / macOS 10.8 Mountain Lion / Linux Ubuntu 18.04 LTS Bionic Beaver
- **Procesador:** Intel Celeron / AMD Athlon
- **Almacenamiento:** 128 Gb (2 Gb libres)
- **Memoria RAM:** 4 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python [IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

Para una óptima implementación de la librería, se sugieren las siguientes ***especificaciones recomendadas***:

- **Sistema Operativo:** Windows 10 / macOS 13.0 Ventura / Linux Ubuntu 22.04 LTS Jammy Jellyfish
- **Procesador:** Intel Core i3 o i5 10ma Gen. / AMD Ryzen 3 o 5 Serie 3000 / Apple M1
- **Almacenamiento:** 256 Gb (4 Gb libres)- 
- **Memoria RAM:** 8 Gb
- [IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado) con soporte para Python ([IDLE](https://docs.python.org/es/3/library/idle.html), [PyCharm](https://www.jetbrains.com/es-es/pycharm/download/?section=windows), [VSC](https://code.visualstudio.com/), [PyDev](https://www.pydev.org/), [Spyder](https://www.spyder-ide.org/), [Atom](https://github.com/atom))

## Comenzando 🚀
---
Para usar esta proyecto se recomienda seguir los siguientes pasos:

1. Crear una nueva carpeta en su máquina local
2. Dar clic derecho en el interior de la carpeta y abrir "Open Git Bush here"
3. Clonar el repositorio:
     ```sh
     $ git clone https://github.com/JAPV-X2612/Libreria_Simulacion_Clasico_a_Cuantico.git
     ```
4. Verificar que se hallan descargado 5 archivos
5. Salir de la terminal de Git:
     ```sh
     $ git exit
     ```

## Instalación 🔧
---
Una vez descargada una copia del repositorio en su máquina local, se recomienda:

1. Abrir el entorno de desarrollo integrado ([IDE](https://es.wikipedia.org/wiki/Entorno_de_desarrollo_integrado)) de su preferencia
2. Abrir el archivo `Pruebas Libreria_Simulacion_Clasico_Cuantico`
3. Instalar las librerías `Numpy` y `Matplotlib` en el IDE en caso de no tenerlas
4. Ejecutar el intérprete de Python predeterminado
5. Verificar que no haya problemas de ejecución o errores
6. Si la respuesta fue `FAILED (failures=#)`, absténgase de usar la librería y reporte el error a jesus.pinzon-v@mail.escuelaing.edu.co
7. En otro caso, si la respuesta fue `OK`, entonces la librería está lista para su uso personal. 💻😎👍

## Ejecutando Pruebas ⚙️
---
A continuación se muestra un ejemplo de ejecución de cada experimento en [IDLE](https://docs.python.org/es/3/library/idle.html):

#### 1. Canicas con coeficientes booleanos
```
>>> Sim_Exp_Can_Det([[1,0,0,1],[0,0,1,0],[0,0,0,0],[0,1,0,0]],[0,1,3,2],3)
     array([6, 0, 0, 0])
```

#### 2. Clásico probabilísitico con múltiples rendijas
```
>>> Sim_Exp_Part_Prob(2,[[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],\
                    [0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]])
     (array([[0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0., 0., 0., 0.],
          [0.16666667, 0.33333333, 0., 1., 0., 0., 0., 0.],
          [0.16666667, 0.33333333, 0., 0., 1., 0., 0., 0.],
          [0.33333333, 0.33333333, 0.33333333, 0., 0.,1., 0., 0.],
          [0.16666667, 0., 0.33333333, 0., 0., 0., 1., 0.],
          [0.16666667, 0., 0.33333333, 0., 0., 0., 0., 1.]]),
     array([[0.],
          [0.],
          [0.],
          [0.16666667],
          [0.16666667],
          [0.33333333],
          [0.16666667],
          [0.16666667]]))
```

#### 3. Cuántico con múltiples rendijas
```
>>> Sim_Exp_Part_Cuan(2,[[0,0,0,0,0,0,0,0],[1/sqrt(2),0,0,0,0,0,0,0],[1/sqrt(2),0,0,0,0,0,0,0],\
                    [0,(-1+1j)/sqrt(6),0,1,0,0,0,0],[0,(-1-1j)/sqrt(6),0,0,1,0,0,0],[0,(1-1j)/sqrt(6),(-1+1j)/sqrt(6),0,0,1,0,0],\
                    [0,0,(-1-1j)/sqrt(6),0,0,0,1,0],[0,0,(1-1j)/sqrt(6),0,0,0,0,1]])
     (array([[0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
          [(-0.2886751345948129+0.2886751345948129j), (-0.4082482904638631+0.4082482904638631j), 0+0j, 1+0j, 0+0j, 0+0j, 0+0j, 0+0j],\
          [(-0.2886751345948129-0.2886751345948129j), (-0.4082482904638631-0.4082482904638631j), 0+0j, 0+0j, 1+0j, 0+0j, 0+0j, 0+0j],\
          [(2.4514267852689627e-17-2.4514267852689627e-17j), (0.4082482904638631-0.4082482904638631j), (-0.4082482904638631+0.4082482904638631j), 0+0j, 0+0j, 1+0j, 0+0j, 0+0j],\
          [(-0.2886751345948129-0.2886751345948129j), 0+0j,(-0.4082482904638631-0.4082482904638631j), 0+0j, 0+0j, 0+0j, 1+0, 0+0j],\
          [(0.2886751345948129-0.2886751345948129j), 0+0j,(0.4082482904638631-0.4082482904638631j), 0+0j, 0+0j, 0+0j, 0+0j, 1+0j]]),
     array([[0+0j],
          [0+0j],
          [0+0j],
          [-2.88675135e-01+2.88675135e-01j],
          [-2.88675135e-01-2.88675135e-01j],
          [2.45142679e-17-2.45142679e-17j],
          [-2.88675135e-01-2.88675135e-01j],
          [2.88675135e-01-2.88675135e-01j]]))
```

## Textos y Wikis 📖
---
Para mayor información sobre los temas descritos en este proyecto se recomienda revisar los siguientes enlaces:

* [Números Complejos](https://es.wikipedia.org/wiki/N%C3%BAmero_complejo)
* [Qubit](https://es.wikipedia.org/wiki/C%C3%BAbit)
* [Computación Cuántica](https://es.wikipedia.org/wiki/Computaci%C3%B3n_cu%C3%A1ntica)
* [Quantum Computing for Computer Scientists](https://www.cambridge.org/core/books/quantum-computing-for-computer-scientists/8AEA723BEE5CC9F5C03FDD4BA850C711)

## Autor ✒️
---
Este proyecto es de la autoría de ***Jesús Alfonso Pinzón Vega***, Ingeniero de Sistemas de la Escuela Colombiana de Ingeniería Julio Garavito ([ECIJG](https://www.escuelaing.edu.co/es/)).  
**Correo:** jesus.pinzon-v@mail.escuelaing.edu.co

## Licencia 📄
---
Este proyecto tiene licencia de código abierto, por lo cual puede ser usado por cualquier persona u organización con fines educativos y de investigación. No obstante, está **PROHIBIDA SU DISTRIBUCIÓN** parcial o completa con fines lucrativos sin expreso consentimiento del autor.  
Se recomienda revisar el archivo **LICENSE** adjunto al repositorio para mayor información.

## Información Adicional 💡
---
También de recominda visitar las siguientes librerías de operaciones con objetos complejos para un mayor entendimiento de los temas tratados en este proyecto:

* [Librería con Números Complejos](https://github.com/JAPV-X2612/Libreria_Numeros_Complejos)
* [Librería de Operaciones con Vectores y Matrices Complejos](https://github.com/JAPV-X2612/Libreria_Vectores_Matrices_Complejos)