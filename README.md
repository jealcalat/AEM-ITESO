# Análisis Estadístico Multivariable

Curso de la maestría en ciencia de datos (MCD) del ITESO.

Inicio: 15 de agosto de 2023

Fin: 30 de noviembre de 2023

**Plataforma**: Teams (reuniones virtuales), CANVAS (administración del curso), y GitHub (materiales del curso y calendario)

**Instructor**: Emmanuel Alcalá

**Correo**: <jaime.alcala@iteso.mx>

**Asesorías**: solicitar cita.

---

**Contenido**

- [Análisis Estadístico Multivariable](#análisis-estadístico-multivariable)
  - [Calendario del curso](#calendario-del-curso)
  - [Temas del curso](#temas-del-curso)
  - [Bibliografía](#bibliografía)
  - [Evaluación](#evaluación)
    - [Tareas](#tareas)
    - [Participación en clase](#participación-en-clase)
    - [Proyectos](#proyectos)
    - [Exámenes](#exámenes)
  - [Tutoriales de `R`](#tutoriales-de-r)
    - [Fundamentos de `R`](#fundamentos-de-r)
    - [Cargar datos (csv, xlsx) en R con RStudio](#cargar-datos-csv-xlsx-en-r-con-rstudio)
    - [Data wrangling con `{dplyr}` y `{tidyr}`](#data-wrangling-con-dplyr-y-tidyr)
    - [Visualización con `{ggplot}`](#visualización-con-ggplot)
    - [Documentos reproducibles con RMarkdown](#documentos-reproducibles-con-rmarkdown)
    - [Modelamiento con `{tidymodels}`](#modelamiento-con-tidymodels)
  - [Tutoriales de MML](#tutoriales-de-mml)
    - [Cálculo](#cálculo)

## Calendario del curso

Para ver el calendario del curso, revisa el siguiente enlace: [Calendario del curso](calendario_del_curso.md). Las fechas se pueden reajustar de acuerdo a cómo avancemos. Para este curso es más importante entender los conceptos que abarcar un temario.

Algunos recursos que he ido recopilando, como una recomendación que han hecho los propios alumnos, se encuentran en [Lecturas y recursos recomendados](lecturas_recursos.md). Estos mismos recursos y lecturas pueden ser usados para sus presentaciones.

## Temas del curso

1. Variables aleatorias multivariadas
   1. [Preliminares](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/tema_1/0-variables_cuantitativas.ipynb)
   2. [Correlaciónes y covarianzas](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/tema_1/1.1_correlaciones_covarianzas.ipynb)

2. Modelos de distribución multivariados
   
   1. [Preliminares](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/tema_2/2.0_preliminares.ipynb)
   2. [Funciones de distribución y densidad](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/tema_2/2.1_funciones_distribucion_densidad.ipynb)
   3. [Distribucion multinormal](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/tema_2/2.2_distribucion_multinormal.ipynb)

3. Teoría de la estimación

   1. [Función de verosimilitud](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/3_teoria_de_estimacion/3.1_funcion_verosimilitud.ipynb)
   2. [Prueba de verosimilitud](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/3_teoria_de_estimacion/3.2_prueba_verosimilitud.ipynb)
   3. [Prueba de hipótesis lineal (regresión lineal)](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/3_teoria_de_estimacion/3.3_prueba_hipotesis_lineal.ipynb)
   4. [Regresión logística](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/3_teoria_de_estimacion/3.4_regresion_logistica.ipynb)

4. Técnicas multivariadas

   1. [ANOVA, MANOVA, ANCOVA](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/4_tecnicas_multivariadas/4.1_anova_manova_ancova.ipynb)
   2. [Modelos log-lineal](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/4_tecnicas_multivariadas/4.2_modelos_log-lineal.ipynb)
   3. [Selección de variables](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/4_tecnicas_multivariadas/4.3_seleccion_de_variables)

5. Descomposición de datos y técnicas de análisis

   1. [Análisis de componentes principales](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/5_descomposicion_datos_tecnicas/5.1_analisis_de_componentes_principales.ipynb)
   2. [Análisis factorial](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/5_descomposicion_datos_tecnicas/5.2_analisis_factorial.ipynb)
   3. [Análisis de clúster](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/5_descomposicion_datos_tecnicas/5.3_analisis_de_cluster.ipynb)
   4. [Modelos de Mezclas Gaussianas]()
   5. [Análisis discriminante](https://nbviewer.org/github/jealcalat/AEM-ITESO/blob/main/5_descomposicion_datos_tecnicas/5.4_analisis_discriminante.ipynb)

---

## Bibliografía

- [_Applied Multivariate Statistical Analysis_](https://link.springer.com/content/pdf/10.1007/978-3-662-45171-7.pdf). Wolfgang H. and Simar. L. Springer, 2015
- _Applied Multivariate Statistical Concepts_. Hahs-Vaughn, D. Editorial Routledge, 2016.
- [_Applied Multivariate Statistics with R_](https://web.uniroma1.it/memotef/sites/default/files/file%20lezioni/102b_textbook.pdf). Zelterman, D. Editorial Springer, 2015.

## Evaluación

| RUBROS                                            | PORCENTAJE |
| ------------------------------------------------- | ---------- |
| 1. [Tareas. Una por tema](#tareas)                | 50%        |
| 2. [Exposición en grupo](#participación-en-clase) | 15%        |
| 3. [Proyecto final](#proyectos)                   | 25%        |
| 4. [Quizzes. Al final de cada tema.](#exámenes)   | 10%        |
| Total                                             | 100%       |

### Tareas

- [Tarea 1](tareas/tarea_1.md)
- [Tarea 2](tareas/tarea_2.md)
- [Tarea 3](tareas/tarea_3.md)
- [Tarea 4](tareas/tarea_4.md)
- [Tarea 5](tareas/tarea_5.md)

### Exposiciones

Una exposición por equipo. Las exposiciones estarán distribuidas de la siguiente manera:

| Equipo   | Tema                   |
| -------- | ---------------------- |
| Equipo 1 | Regresión logística    |
| Equipo 2 | PCA                    |
| Equipo 3 | Análisis factorial     |
| Equipo 4 | Análisis discriminante |

Organización sugerida de las exposiciones:

**Regresión logística**

1. Modelos lineales generalizados (énfasis en función de enlace).
2. Implementación y diagnóstico de modelo de regresión logística en R/Python.
3. Interpretación de resultados (efectos marginales, odds ratio, intervalos de confianza, etc).

**PCA**

1. Estructura matemática (combinación lineal).
2. Método de obtención con factorización matricial.
3. Implementación e interpretación en R/Python

### Proyectos

Contenido:

1. Introducción: describir un problema o una pregunta. 
2. Datos: describir los datos que se van a usar, sus variables, si se hizo un tratamiento o tranformación (e.g., ingeniería de características).
3. Presentación del análisis:
   1. Métodos: el análisis que harás. Debes describir formalmente dicho análisis (aquí me entero de que tienes una comprensión formal de dicho análisis).
   2. Resultados: gráficos principales y tablas de estadísticos, lo más refinado que puedas.
4. Conclusión: transmite tus hallazgos a una audiencia más amplia.


## Tutoriales de MML

Algunos tutoriales de matemáticas y estadística básica. El libro recomendable para matemáticas de ML es [Mathematics for Machine Learning](/refs/mml-book.pdf) de Deisenroth, Faisal y Ong.

### Cálculo

- [Este un curso de Cálculo para ML](https://www.youtube.com/watch?v=-J_GKa_2TPQ&list=PLiiljHvN6z193BBzS0Ln8NnqQmzimTW23&index=3). Para derivadas, es suficiente para tener la noción de derivada consultar los videos 3-8.
- [En este video explican algunas reglas de derivación útiles.](https://www.youtube.com/watch?v=aVNa-J8iB5I).
- [Este video es una introducción concisa de integración](https://www.youtube.com/watch?v=Ec-cGjh0Fr0)
