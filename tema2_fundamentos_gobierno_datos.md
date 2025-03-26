# Tema 2: Fundamentos de Gestión y Gobierno de Datos

## 1. Fundamentos de Gestión y Gobierno de Datos

### 1.1 Definiciones Clave

#### Gestión de Datos
La gestión de datos comprende el desarrollo, ejecución y supervisión de planes, políticas, programas y prácticas que controlan, protegen, entregan y mejoran el valor de los datos y los activos de información.

#### Gobierno de Datos
El gobierno de datos es el ejercicio de autoridad y control (planificación, monitoreo y ejecución) sobre la gestión de los activos de datos.

![Gobierno de Datos](https://raw.githubusercontent.com/alarcon-osorio/images/main/gobierno-datos.png)

### 1.2 ¿Para qué Gestión y Gobierno?

#### Objetivos Principales:
- Asegurar la calidad de los datos
- Garantizar la seguridad y privacidad
- Maximizar el valor de los datos
- Reducir riesgos operacionales
- Asegurar el cumplimiento normativo

### 1.3 Control por Excepción

El control por excepción es un principio de gestión donde solo las desviaciones significativas del estándar requieren atención y acción.

#### Componentes clave:
- Establecimiento de estándares
- Monitoreo continuo
- Detección de anomalías
- Gestión de excepciones
- Acciones correctivas

## 2. Lineamientos e Indicadores

### 2.1 Tipos de Indicadores

#### Indicadores de Calidad de Datos
- Precisión
- Completitud
- Consistencia
- Puntualidad
- Unicidad

#### Indicadores de Proceso
- Tiempo de respuesta
- Eficiencia operativa
- Cumplimiento de SLAs
- Tasa de errores

#### Ratios Clave
- ROI de iniciativas de datos
- Costo por registro
- Tasa de adopción
- Índice de calidad de datos

### 2.2 ¿Qué Medir?

#### Dimensiones críticas:
1. Calidad de Datos
2. Seguridad y Cumplimiento
3. Eficiencia Operacional
4. Valor del Negocio
5. Madurez del Gobierno

### 2.3 Análisis de Indicadores

#### Metodología de Análisis:
1. Recolección de datos
2. Validación
3. Análisis estadístico
4. Interpretación
5. Acción

## Caso Práctico: Análisis de Calidad de Datos

### Ejercicio: Sistema de Monitoreo de Calidad de Datos

```python
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

class DataQualityMonitor:
    def __init__(self, df):
        self.df = df
        self.results = {}
    
    def check_completeness(self):
        """Calcula el porcentaje de completitud por columna"""
        completeness = (1 - self.df.isnull().mean()) * 100
        self.results['completeness'] = completeness
        return completeness
    
    def check_uniqueness(self):
        """Calcula el porcentaje de valores únicos por columna"""
        uniqueness = (self.df.nunique() / len(self.df)) * 100
        self.results['uniqueness'] = uniqueness
        return uniqueness
    
    def check_consistency(self, date_columns):
        """Verifica la consistencia de fechas"""
        consistency = {}
        for col in date_columns:
            try:
                dates = pd.to_datetime(self.df[col])
                valid_dates = dates.notna().mean() * 100
                consistency[col] = valid_dates
            except:
                consistency[col] = 0
        self.results['consistency'] = consistency
        return consistency
    
    def generate_report(self):
        """Genera un reporte visual de calidad de datos"""
        plt.figure(figsize=(15, 10))
        
        # Gráfico de completitud
        plt.subplot(2, 1, 1)
        self.results['completeness'].plot(kind='bar')
        plt.title('Completitud por Columna')
        plt.xlabel('Columnas')
        plt.ylabel('Porcentaje de Completitud')
        plt.xticks(rotation=45)
        
        # Gráfico de unicidad
        plt.subplot(2, 1, 2)
        self.results['uniqueness'].plot(kind='bar', color='green')
        plt.title('Unicidad por Columna')
        plt.xlabel('Columnas')
        plt.ylabel('Porcentaje de Valores Únicos')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()

# Ejemplo de uso
# Crear datos de ejemplo
np.random.seed(42)
data = {
    'ID': range(1000),
    'Nombre': ['Cliente_' + str(i) for i in range(1000)],
    'Fecha': pd.date_range(start='2023-01-01', periods=1000),
    'Valor': np.random.normal(1000, 100, 1000),
    'Categoria': np.random.choice(['A', 'B', 'C', None], 1000)
}

df = pd.DataFrame(data)
# Introducir algunos valores nulos
df.loc[np.random.choice(df.index, 50), 'Valor'] = None
df.loc[np.random.choice(df.index, 30), 'Categoria'] = None

# Crear monitor de calidad
monitor = DataQualityMonitor(df)

# Ejecutar checks
completeness = monitor.check_completeness()
uniqueness = monitor.check_uniqueness()
consistency = monitor.check_consistency(['Fecha'])

# Generar reporte
monitor.generate_report()

# Imprimir resultados detallados
print("\nReporte de Calidad de Datos:")
print("\nCompletitud:")
print(completeness)
print("\nUnicidad:")
print(uniqueness)
print("\nConsistencia de Fechas:")
print(consistency)
```

### Ejercicio Propuesto:
1. Extiende el monitor de calidad para incluir más métricas:
   - Validación de rangos
   - Detección de outliers
   - Patrones de formato (emails, teléfonos, etc.)
2. Implementa un sistema de alertas cuando las métricas caen por debajo de umbrales definidos
3. Crea un dashboard interactivo usando Streamlit o Dash

## Referencias

1. DAMA DMBOK 2.0 - Capítulos sobre Calidad de Datos y Gobierno de Datos
2. "Data Governance: How to Design, Deploy and Sustain an Effective Data Governance Program" - John Ladley
3. ISO/IEC 38505-1:2017 - Governance of data

## Recursos Adicionales

- [Data Quality Assessment Framework - World Bank](https://datatopics.worldbank.org/statisticalcapacity/files/DQAF_0207.pdf)
- [Data Management Association (DAMA) International](https://www.dama.org/)
- [Data Governance Institute](http://www.datagovernance.com/) 