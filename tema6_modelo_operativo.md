# Tema 6: Modelo Operativo de Gobierno y Gestión de Datos en una Empresa Financiera

## 1. Introducción al Modelo Operativo

### 1.1 Contexto del Sector Financiero

El sector financiero tiene requisitos específicos para el gobierno y gestión de datos:
- Regulaciones estrictas (Basel III, GDPR, PSD2)
- Alta sensibilidad de datos
- Necesidad de tiempo real
- Gestión de riesgos
- Cumplimiento normativo

![Modelo Operativo](https://raw.githubusercontent.com/alarcon-osorio/images/main/modelo-operativo.png)

### 1.2 Componentes del Modelo Operativo

1. Estructura Organizacional
2. Procesos y Procedimientos
3. Tecnología y Herramientas
4. Métricas y KPIs
5. Cultura y Cambio Organizacional

## 2. Estructura Organizacional

### 2.1 Roles y Responsabilidades

#### Nivel Ejecutivo
- Chief Data Officer (CDO)
- Chief Risk Officer (CRO)
- Chief Information Security Officer (CISO)
- Chief Compliance Officer (CCO)

#### Nivel Táctico
- Data Governance Manager
- Data Quality Manager
- Data Security Manager
- Business Data Stewards

#### Nivel Operativo
- Data Analysts
- Data Engineers
- Data Scientists
- Database Administrators

### 2.2 Comités y Grupos de Trabajo

1. Comité Ejecutivo de Datos
2. Comité de Gobierno de Datos
3. Grupo de Trabajo de Calidad
4. Grupo de Trabajo de Seguridad

## 3. Procesos y Procedimientos

### 3.1 Procesos Core

1. Gestión de Datos Maestros
2. Gestión de Calidad de Datos
3. Gestión de Seguridad
4. Gestión de Cambios
5. Gestión de Incidentes

### 3.2 Procedimientos Específicos

- Onboarding de Datos
- Clasificación de Datos
- Control de Acceso
- Monitoreo y Reporting
- Auditoría y Compliance

## 4. Caso Práctico: Sistema de Gestión de Riesgos de Datos

### Ejercicio: Implementación de un Sistema de Monitoreo de Riesgos

```python
from datetime import datetime
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import logging
import json
from enum import Enum

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class RiskIndicator:
    name: str
    description: str
    threshold: float
    current_value: float
    risk_level: RiskLevel
    category: str
    owner: str
    last_updated: datetime = field(default_factory=datetime.now)

class RiskMonitoringSystem:
    def __init__(self):
        self.indicators = {}
        self.risk_matrix = {}
        self.alerts = []
        self.mitigation_plans = {}
        
    def add_indicator(self, indicator: RiskIndicator):
        """Añade un nuevo indicador de riesgo"""
        self.indicators[indicator.name] = indicator
        logger.info(f"Indicador {indicator.name} añadido al sistema")
        
    def update_indicator(self, indicator_name: str, new_value: float):
        """Actualiza el valor de un indicador y evalúa el riesgo"""
        if indicator_name not in self.indicators:
            raise ValueError(f"Indicador {indicator_name} no encontrado")
            
        indicator = self.indicators[indicator_name]
        indicator.current_value = new_value
        indicator.last_updated = datetime.now()
        
        # Evaluar nivel de riesgo
        self._evaluate_risk(indicator)
        
    def _evaluate_risk(self, indicator: RiskIndicator):
        """Evalúa el nivel de riesgo basado en el valor actual y umbral"""
        value_ratio = indicator.current_value / indicator.threshold
        
        if value_ratio <= 0.5:
            new_level = RiskLevel.LOW
        elif value_ratio <= 0.8:
            new_level = RiskLevel.MEDIUM
        elif value_ratio <= 1.0:
            new_level = RiskLevel.HIGH
        else:
            new_level = RiskLevel.CRITICAL
            
        # Si el nivel de riesgo cambió, generar alerta
        if new_level != indicator.risk_level:
            self._generate_alert(indicator, new_level)
            indicator.risk_level = new_level
            
    def _generate_alert(self, indicator: RiskIndicator, new_level: RiskLevel):
        """Genera una alerta por cambio en nivel de riesgo"""
        alert = {
            'timestamp': datetime.now().isoformat(),
            'indicator': indicator.name,
            'previous_level': indicator.risk_level.value,
            'new_level': new_level.value,
            'current_value': indicator.current_value,
            'threshold': indicator.threshold
        }
        self.alerts.append(alert)
        logger.warning(f"Alerta generada para {indicator.name}: "
                      f"{indicator.risk_level.value} -> {new_level.value}")
        
    def add_mitigation_plan(self, indicator_name: str, plan: Dict):
        """Añade un plan de mitigación para un indicador"""
        if indicator_name not in self.indicators:
            raise ValueError(f"Indicador {indicator_name} no encontrado")
            
        self.mitigation_plans[indicator_name] = plan
        logger.info(f"Plan de mitigación añadido para {indicator_name}")
        
    def generate_risk_report(self) -> pd.DataFrame:
        """Genera un reporte de estado de riesgos"""
        report_data = []
        
        for name, indicator in self.indicators.items():
            report_data.append({
                'Indicator': name,
                'Category': indicator.category,
                'Current Value': indicator.current_value,
                'Threshold': indicator.threshold,
                'Risk Level': indicator.risk_level.value,
                'Owner': indicator.owner,
                'Last Updated': indicator.last_updated.isoformat()
            })
            
        return pd.DataFrame(report_data)
    
    def export_system_state(self, filename: str):
        """Exporta el estado del sistema a JSON"""
        state = {
            'indicators': {name: {
                **vars(indicator),
                'risk_level': indicator.risk_level.value,
                'last_updated': indicator.last_updated.isoformat()
            } for name, indicator in self.indicators.items()},
            'alerts': self.alerts,
            'mitigation_plans': self.mitigation_plans
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)

# Ejemplo de uso
risk_system = RiskMonitoringSystem()

# Añadir indicadores
indicators = [
    RiskIndicator(
        "data_quality_score", 
        "Puntuación general de calidad de datos",
        threshold=0.95,
        current_value=0.92,
        risk_level=RiskLevel.MEDIUM,
        category="Data Quality",
        owner="Data Quality Team"
    ),
    RiskIndicator(
        "security_incidents",
        "Número de incidentes de seguridad por mes",
        threshold=5,
        current_value=2,
        risk_level=RiskLevel.LOW,
        category="Security",
        owner="Security Team"
    ),
    RiskIndicator(
        "data_availability",
        "Porcentaje de disponibilidad de datos críticos",
        threshold=0.99,
        current_value=0.995,
        risk_level=RiskLevel.LOW,
        category="Operations",
        owner="Operations Team"
    )
]

for indicator in indicators:
    risk_system.add_indicator(indicator)

# Añadir planes de mitigación
risk_system.add_mitigation_plan("data_quality_score", {
    "actions": [
        "Realizar limpieza de datos",
        "Actualizar reglas de validación",
        "Revisar procesos de ingesta"
    ],
    "responsible": "Data Quality Team",
    "timeline": "2 weeks"
})

# Simular actualizaciones
risk_system.update_indicator("data_quality_score", 0.88)
risk_system.update_indicator("security_incidents", 6)

# Generar reporte
print("\nReporte de Riesgos:")
print(risk_system.generate_risk_report())

# Exportar estado
risk_system.export_system_state("risk_monitoring_state.json")
```

### Ejercicio Propuesto:
1. Extiende el sistema para incluir:
   - Análisis de tendencias
   - Predicción de riesgos
   - Correlación entre indicadores
2. Implementa un dashboard en tiempo real
3. Añade integración con sistemas externos

## 5. Métricas y KPIs

### 5.1 Métricas de Gobierno de Datos

1. Calidad de Datos
   - Precisión
   - Completitud
   - Consistencia
   - Puntualidad

2. Seguridad
   - Incidentes
   - Tiempo de respuesta
   - Vulnerabilidades
   - Cumplimiento

3. Operaciones
   - Disponibilidad
   - Performance
   - Tiempo de resolución
   - SLAs

### 5.2 KPIs de Negocio

1. Financieros
   - ROI de iniciativas de datos
   - Costos operativos
   - Eficiencia

2. Operativos
   - Tiempo de procesamiento
   - Precisión de reportes
   - Satisfacción de usuarios

3. Regulatorios
   - Cumplimiento
   - Auditorías
   - Reportes regulatorios

## 6. Cultura y Gestión del Cambio

### 6.1 Programa de Cultura de Datos

1. Concientización
2. Capacitación
3. Comunicación
4. Incentivos

### 6.2 Gestión del Cambio

- Evaluación de impacto
- Plan de comunicación
- Programa de capacitación
- Medición de adopción

## Referencias

1. "Financial Services Data Governance" - EDM Council
2. "Data Management in Banking" - DAMA International
3. "Risk Data Aggregation and Risk Reporting" - Basel Committee

## Recursos Adicionales

- [EDM Council](https://edmcouncil.org/)
- [BCBS 239](https://www.bis.org/publ/bcbs239.pdf)
- [Financial Data Quality Management](https://www.gleif.org/) 