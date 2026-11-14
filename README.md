# Predicción del precio del gasóleo en las gasolineras de España

Proyecto completo de Machine Learning — Máster de FP en Inteligencia Artificial y Big Data.

**Autora:** Lorena Herranz Pascual

- **Vídeo explicativo:** [ver en YouTube]https://www.youtube.com/watch?v=J1HzpghMQ2o
- **Cuaderno en Google Colab:** [abrir en Colab]https://colab.research.google.com/drive/11miEskv_PQzkX-pj4CTP5LDn_TkTAfwk#scrollTo=fcQFfi_4f8wy

## Objetivo

Predecir el precio del gasóleo A de una gasolinera a partir de su ubicación, su marca, su horario y el margen de la carretera.
Es un problema de aprendizaje supervisado y de regresión múltiple.

## Resultados

| Modelo | Error medio (RMSE, validación cruzada) | R² |
|---|---|---|
| Random forest ajustado | 0,060 €/l | 0,647 |
| Random forest | 0,061 €/l | 0,634 |
| Regresión lineal | 0,064 €/l | 0,598 |
| Árbol de decisión | 0,079 €/l | 0,382 |

El modelo elegido (random forest ajustado) obtiene en los datos de prueba un error medio de **5,7 céntimos por litro**
y explica el **68 %** de las diferencias de precio. La marca y la ubicación son las características más importantes.

## Contenido

| Archivo | Descripción |
|---|---|
| `Proyecto_ML_LorenaHerranz.ipynb` | Cuaderno con el proyecto completo |
| `gasolineras_2026-11-09.csv` | Dataset: precios de 11.479 gasolineras de España a fecha 9/11/2026, 9:42 h |
| `descargar_gasolineras.py` | Script de Python que descargó los datos del servicio REST del Ministerio |

## Fuente de los datos

Ministerio para la Transición Ecológica y el Reto Demográfico (MITECO), servicio REST de precios de carburantes
en estaciones de servicio terrestres:
https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/
