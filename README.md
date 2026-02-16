# Ejercicios Prácticos: Machine Learning Aplicado a Negocio

**Semana 6 — Dos sesiones de 2 horas**

Material docente para conectar **problema de negocio → formulación analítica → diseño de modelo ML**.

---

## Requisitos previos

- Python 3.8+
- Conocimientos: Python intermedio, pandas, numpy, matplotlib
- Conceptos básicos de IA y redes neuronales

## Dependencias

```bash
pip install pandas numpy matplotlib seaborn jupyter
pip install statsmodels  # Para VIF (Variance Inflation Factor)
# Opcional:
pip install ydata-profiling  # Para EDA automático
```

## Estructura del repositorio

```
week-6/
├── data/
│   └── telco_churn.csv       # Dataset (descargar con script)
├── notebooks/
│   ├── sesion1_plantilla.ipynb   # Sesión 1: EDA y problema analítico
│   └── sesion2_plantilla.ipynb   # Sesión 2: Target formal y validación
├── soluciones/                   # Solo para instructor
│   ├── sesion1_solucion.ipynb
│   └── sesion2_solucion.ipynb
├── entregables/
│   ├── plantilla_informe_eda.md
│   ├── plantilla_tabla_kpis.md
│   └── plantilla_ficha_tecnica.md
├── scripts/
│   └── descargar_dataset.py      # Script para obtener el dataset
├── requirements.txt
└── README.md
```

## Obtención del dataset

El dataset **Telco Customer Churn** (IBM) debe descargarse antes de comenzar:

```bash
python scripts/descargar_dataset.py
```

O manualmente desde:
- [IBM Sample Datasets - Telco](https://community.ibm.com/community/user/businessanalytics/blogs/jessica-rosenberg/2019/04/18/telco-customer-churn-1113)
- [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

El archivo se guardará en `data/telco_churn.csv`.

## Sesión 1 — Del dato crudo al problema analítico (2h)

| Actividad | Duración | Entregable |
|-----------|----------|------------|
| 1. EDA técnico estructurado | 50 min | Informe EDA (plantilla en `entregables/`) |
| 2. Tipología de preguntas analíticas | 25 min | Tabla pregunta-técnica |
| 3. KPIs y formalización matemática | 25 min | Tabla KPIs |
| 4. Error conceptual intencional | 20 min | Identificación de 3 errores |

## Sesión 2 — Del KPI al modelo formal (2h)

| Actividad | Duración | Entregable |
|-----------|----------|------------|
| 1. Definición formal del target | 20 min | Target, horizonte, unidad, tipo |
| 2. Selección de variables | 25 min | Matriz de clasificación (≥10 variables) |
| 3. Validación empírica con código | 35 min | Correlación, VIF, desbalanceo |
| 4. Simulación de fuga de datos | 20 min | Explicación leakage |
| 5. Mini Ficha Técnica | 20 min | Ficha completa (plantilla en `entregables/`) |

## Criterios de evaluación

| Actividad | Peso |
|-----------|------|
| EDA + Informe | 25% |
| Tipología + KPIs | 20% |
| Error conceptual | 15% |
| Target + Variables | 20% |
| Validación + Ficha | 20% |

## Uso

1. Descargar el dataset con `python scripts/descargar_dataset.py`
2. Abrir `notebooks/sesion1_plantilla.ipynb` en Jupyter
3. Completar las celdas siguiendo las instrucciones
4. Usar las plantillas en `entregables/` para los informes
