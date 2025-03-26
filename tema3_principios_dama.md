# Tema 3: Principios DAMA, Normativa y Buenas Prácticas

## 1. Marco DAMA-DMBOK

### 1.1 Introducción al DAMA-DMBOK

El DAMA-DMBOK (Data Management Body of Knowledge) es la guía definitiva para la gestión de datos, proporcionando un marco estándar para entender y aplicar las prácticas de gestión de datos.

![DAMA Wheel](https://raw.githubusercontent.com/alarcon-osorio/images/main/dama-wheel.png)

### 1.2 Áreas de Conocimiento DAMA

#### 1. Gobierno de Datos
- Planificación, supervisión y control
- Establecimiento de políticas
- Roles y responsabilidades
- Gestión del valor de los datos

#### 2. Arquitectura de Datos
- Modelos de datos empresariales
- Arquitectura de datos empresarial
- Estándares de datos
- Integración y interoperabilidad

#### 3. Modelado y Diseño de Datos
- Modelado conceptual
- Modelado lógico
- Modelado físico
- Normalización y desnormalización

#### 4. Almacenamiento y Operaciones
- Base de datos y gestión del almacenamiento
- Tecnología de bases de datos
- Operaciones de bases de datos
- Respaldo y recuperación

#### 5. Seguridad de Datos
- Políticas de seguridad
- Clasificación de datos
- Control de acceso
- Auditoría y monitoreo

#### 6. Integración e Interoperabilidad
- ETL y ELT
- Integración de datos
- Servicios de datos
- Consolidación de datos

#### 7. Gestión de Documentos y Contenido
- Gestión de contenido empresarial
- Metadatos de documentos
- Ciclo de vida de documentos
- Archivado

#### 8. Datos de Referencia y Maestros
- MDM (Master Data Management)
- Datos de referencia
- Datos maestros
- Calidad de datos maestros

#### 9. Data Warehousing y Business Intelligence
- Arquitectura DW/BI
- Diseño dimensional
- ETL para DW
- Reporting y análisis

#### 10. Metadata
- Gestión de metadatos
- Repositorio de metadatos
- Estándares de metadatos
- Integración de metadatos

#### 11. Calidad de Datos
- Evaluación de calidad
- Perfilado de datos
- Limpieza de datos
- Monitoreo continuo

## 2. Caso Práctico: Implementación de Gestión de Metadatos

### Ejercicio: Sistema de Gestión de Metadatos

```python
import pandas as pd
import json
from datetime import datetime
import networkx as nx
import matplotlib.pyplot as plt

class MetadataManager:
    def __init__(self):
        self.metadata_registry = {}
        self.lineage_graph = nx.DiGraph()
        
    def register_dataset(self, dataset_name, metadata):
        """Registra un nuevo conjunto de datos con sus metadatos"""
        metadata['registration_date'] = datetime.now().isoformat()
        self.metadata_registry[dataset_name] = metadata
        
    def add_lineage(self, source_dataset, target_dataset, transformation):
        """Agrega información de linaje entre datasets"""
        self.lineage_graph.add_edge(source_dataset, target_dataset, 
                                  transformation=transformation)
        
    def get_dataset_info(self, dataset_name):
        """Obtiene información de un dataset"""
        return self.metadata_registry.get(dataset_name, None)
    
    def visualize_lineage(self):
        """Visualiza el grafo de linaje de datos"""
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.lineage_graph)
        nx.draw(self.lineage_graph, pos, with_labels=True, 
                node_color='lightblue', node_size=2000, font_size=10)
        
        edge_labels = nx.get_edge_attributes(self.lineage_graph, 'transformation')
        nx.draw_networkx_edge_labels(self.lineage_graph, pos, 
                                   edge_labels=edge_labels)
        plt.title("Linaje de Datos")
        plt.show()
        
    def export_metadata(self, filename):
        """Exporta el registro de metadatos a JSON"""
        with open(filename, 'w') as f:
            json.dump(self.metadata_registry, f, indent=4)
            
    def generate_report(self):
        """Genera un reporte de metadatos"""
        report = []
        for dataset, metadata in self.metadata_registry.items():
            report.append({
                'Dataset': dataset,
                'Columns': len(metadata.get('columns', [])),
                'Last Updated': metadata.get('last_updated', 'Unknown'),
                'Owner': metadata.get('owner', 'Unknown'),
                'Quality Score': metadata.get('quality_score', 'N/A')
            })
        return pd.DataFrame(report)

# Ejemplo de uso
metadata_mgr = MetadataManager()

# Registrar datasets
metadata_mgr.register_dataset('raw_sales', {
    'owner': 'Data Team',
    'source': 'CRM System',
    'columns': ['date', 'product_id', 'quantity', 'price'],
    'update_frequency': 'daily',
    'quality_score': 0.95
})

metadata_mgr.register_dataset('processed_sales', {
    'owner': 'Analytics Team',
    'source': 'Data Warehouse',
    'columns': ['date', 'product_id', 'total_revenue', 'region'],
    'update_frequency': 'daily',
    'quality_score': 0.98
})

# Agregar linaje
metadata_mgr.add_lineage('raw_sales', 'processed_sales', 
                        'Agregación por región y cálculo de ingresos')

# Visualizar linaje
metadata_mgr.visualize_lineage()

# Generar reporte
report = metadata_mgr.generate_report()
print("\nReporte de Metadatos:")
print(report)

# Exportar metadatos
metadata_mgr.export_metadata('metadata_catalog.json')
```

### Ejercicio Propuesto:
1. Extiende el gestor de metadatos para incluir:
   - Validación de esquemas
   - Versionado de metadatos
   - Búsqueda y filtrado avanzado
2. Implementa un sistema de notificaciones para cambios en los metadatos
3. Crea una interfaz web simple usando Flask para gestionar los metadatos

## 3. Buenas Prácticas DAMA

### 3.1 Principios Fundamentales
1. Los datos son un activo
2. Los datos deben ser accesibles
3. Los datos deben ser seguros
4. Los datos deben ser gestionados
5. Los datos deben tener custodios
6. Los datos deben tener calidad conocida
7. Los datos deben ser definidos y entendibles
8. Los datos deben ser gestionados con rendición de cuentas

### 3.2 Implementación de Buenas Prácticas
- Establecer un programa de gobierno de datos
- Definir roles y responsabilidades claras
- Implementar políticas y procedimientos
- Medir y monitorear la efectividad
- Mantener documentación actualizada
- Realizar auditorías regulares
- Proporcionar capacitación continua

## Referencias

1. DAMA International Guide to the Data Management Body of Knowledge (DAMA-DMBOK)
2. "The DAMA Dictionary of Data Management" - DAMA International
3. "Data Management: A Guide to Implementing Data Management" - Mark Mosley

## Recursos Adicionales

- [DAMA International](https://www.dama.org/)
- [Data Governance Institute Framework](http://www.datagovernance.com/framework/)
- [ISO/IEC 38505-1:2017](https://www.iso.org/standard/56639.html) 