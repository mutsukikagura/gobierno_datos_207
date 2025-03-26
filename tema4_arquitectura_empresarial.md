# Tema 4: Arquitectura Empresarial y de Información

## 1. Diseño de la Arquitectura Empresarial

### 1.1 Fundamentos de Arquitectura Empresarial

La arquitectura empresarial (EA) es un enfoque holístico para gestionar y alinear los activos de TI de una organización, procesos, inversiones y estrategias con los objetivos operativos.

![Enterprise Architecture Framework](https://raw.githubusercontent.com/alarcon-osorio/images/main/enterprise-architecture.png)

### 1.2 Marcos de Arquitectura Empresarial

#### TOGAF (The Open Group Architecture Framework)
- Método de Desarrollo de Arquitectura (ADM)
- Continuum Empresarial
- Repositorio de Arquitectura
- Marco de Capacidades

#### Zachman Framework
- Contextual (Planificador)
- Conceptual (Propietario)
- Lógico (Diseñador)
- Físico (Constructor)
- Detallado (Programador)
- Funcional (Usuario)

### 1.3 Componentes de la Arquitectura Empresarial

1. Arquitectura de Negocio
   - Procesos de negocio
   - Organización
   - Funciones
   - Estrategia

2. Arquitectura de Datos
   - Modelos de datos
   - Flujos de información
   - Gobierno de datos
   - Calidad de datos

3. Arquitectura de Aplicaciones
   - Sistemas
   - Interfaces
   - Integraciones
   - Servicios

4. Arquitectura Tecnológica
   - Infraestructura
   - Redes
   - Plataformas
   - Seguridad

## 2. Arquitectura de Información de las Empresas

### 2.1 Componentes Clave

#### Gestión de Datos Maestros
- Clientes
- Productos
- Empleados
- Ubicaciones

#### Gestión de Datos de Referencia
- Códigos
- Clasificaciones
- Taxonomías
- Jerarquías

#### Gestión de Metadatos
- Técnicos
- Empresariales
- Operacionales

### 2.2 Patrones de Arquitectura de Información

1. Centralizado
2. Federado
3. Híbrido
4. Distribuido

## 3. Caso Práctico: Modelado de Arquitectura Empresarial

### Ejercicio: Sistema de Mapeo de Arquitectura Empresarial

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import json
import networkx as nx
import matplotlib.pyplot as plt
from datetime import datetime

@dataclass
class ArchitectureComponent:
    name: str
    type: str
    description: str
    owner: str
    dependencies: List[str] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)
    created_date: str = field(default_factory=lambda: datetime.now().isoformat())

class EnterpriseArchitecture:
    def __init__(self):
        self.components = {}
        self.relationships = nx.DiGraph()
        
    def add_component(self, component: ArchitectureComponent):
        """Añade un nuevo componente a la arquitectura"""
        self.components[component.name] = component
        self.relationships.add_node(component.name, 
                                  type=component.type,
                                  owner=component.owner)
        
    def add_dependency(self, from_component: str, to_component: str, 
                      relationship_type: str):
        """Establece una dependencia entre componentes"""
        if from_component in self.components and to_component in self.components:
            self.relationships.add_edge(from_component, to_component, 
                                     type=relationship_type)
            self.components[from_component].dependencies.append(to_component)
            
    def visualize_architecture(self):
        """Visualiza la arquitectura empresarial"""
        plt.figure(figsize=(15, 10))
        
        # Crear layout
        pos = nx.spring_layout(self.relationships)
        
        # Dibujar nodos por tipo
        node_colors = {
            'business': 'lightblue',
            'data': 'lightgreen',
            'application': 'lightcoral',
            'technology': 'lightyellow'
        }
        
        for node_type in node_colors:
            nodes = [n for n, attr in self.relationships.nodes(data=True) 
                    if attr.get('type') == node_type]
            nx.draw_networkx_nodes(self.relationships, pos, 
                                 nodelist=nodes,
                                 node_color=node_colors[node_type],
                                 node_size=2000,
                                 label=node_type.capitalize())
        
        # Dibujar etiquetas y bordes
        nx.draw_networkx_labels(self.relationships, pos)
        nx.draw_networkx_edges(self.relationships, pos, edge_color='gray', 
                             arrows=True)
        
        # Añadir leyenda
        plt.legend()
        plt.title("Arquitectura Empresarial")
        plt.axis('off')
        plt.show()
        
    def export_architecture(self, filename: str):
        """Exporta la arquitectura a JSON"""
        architecture_dict = {
            'components': {name: vars(comp) 
                         for name, comp in self.components.items()},
            'relationships': list(self.relationships.edges(data=True))
        }
        
        with open(filename, 'w') as f:
            json.dump(architecture_dict, f, indent=4)
            
    def analyze_impact(self, component_name: str):
        """Analiza el impacto de cambios en un componente"""
        if component_name not in self.components:
            return None
            
        downstream = list(nx.descendants(self.relationships, component_name))
        upstream = list(nx.ancestors(self.relationships, component_name))
        
        return {
            'component': component_name,
            'downstream_impact': downstream,
            'upstream_dependencies': upstream,
            'total_impact': len(downstream) + len(upstream)
        }

# Ejemplo de uso
ea = EnterpriseArchitecture()

# Añadir componentes
components = [
    ArchitectureComponent("Sales Process", "business", 
                         "Core sales business process", "Sales Department"),
    ArchitectureComponent("Customer Data", "data", 
                         "Customer master data", "Data Team"),
    ArchitectureComponent("CRM System", "application", 
                         "Customer Relationship Management", "IT Department"),
    ArchitectureComponent("Cloud Infrastructure", "technology", 
                         "AWS Cloud Platform", "Infrastructure Team")
]

for component in components:
    ea.add_component(component)

# Añadir dependencias
ea.add_dependency("Sales Process", "CRM System", "uses")
ea.add_dependency("CRM System", "Customer Data", "manages")
ea.add_dependency("CRM System", "Cloud Infrastructure", "runs on")

# Visualizar arquitectura
ea.visualize_architecture()

# Analizar impacto
impact = ea.analyze_impact("CRM System")
print("\nAnálisis de Impacto para CRM System:")
print(json.dumps(impact, indent=2))

# Exportar arquitectura
ea.export_architecture("enterprise_architecture.json")
```

### Ejercicio Propuesto:
1. Extiende el sistema para incluir:
   - Versionado de componentes
   - Gestión de cambios
   - Análisis de riesgos
2. Implementa validaciones de arquitectura basadas en reglas
3. Crea una interfaz web para visualizar y gestionar la arquitectura

## Referencias

1. TOGAF 9.2 - The Open Group Architecture Framework
2. "Enterprise Architecture As Strategy" - Jeanne W. Ross
3. "Building an Enterprise Architecture Practice" - Martin van den Berg

## Recursos Adicionales

- [The Open Group](https://www.opengroup.org/)
- [Zachman Framework](https://www.zachman.com/about-the-zachman-framework)
- [ArchiMate Specification](https://pubs.opengroup.org/architecture/archimate3-doc/) 