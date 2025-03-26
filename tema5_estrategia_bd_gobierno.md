# Tema 5: Estrategia de Base de Datos y Gobierno de Datos

## 1. Diseño de Estrategia de Base de Datos

### 1.1 Tipos de Bases de Datos

#### Bases de Datos Relacionales (RDBMS)
- MySQL
- PostgreSQL
- Oracle
- SQL Server

#### Bases de Datos NoSQL
- Documentos (MongoDB)
- Clave-Valor (Redis)
- Columnares (Cassandra)
- Grafos (Neo4j)

#### Data Warehouses
- Amazon Redshift
- Snowflake
- Google BigQuery
- Azure Synapse

### 1.2 Estrategias de Implementación

1. On-Premises vs Cloud
2. Híbrido
3. Multi-Cloud
4. Distribuida

## 2. Modelo de Gobierno de Datos

### 2.1 Estructura Organizacional

#### Roles y Responsabilidades
- Chief Data Officer (CDO)
- Data Stewards
- Data Owners
- Data Custodians
- Data Users

#### Comités y Grupos de Trabajo
- Comité de Gobierno de Datos
- Grupo de Calidad de Datos
- Equipo de Seguridad de Datos
- Comité de Arquitectura

### 2.2 Políticas y Procedimientos

1. Gestión de Datos Maestros
2. Calidad de Datos
3. Seguridad y Privacidad
4. Retención y Archivado
5. Metadata Management

## 3. Seguridad de Datos

### 3.1 Principios de Seguridad

- Confidencialidad
- Integridad
- Disponibilidad
- Autenticación
- Autorización
- Auditoría

### 3.2 Implementación de Seguridad

#### Control de Acceso
- RBAC (Role-Based Access Control)
- ABAC (Attribute-Based Access Control)
- DAC (Discretionary Access Control)
- MAC (Mandatory Access Control)

#### Encriptación
- En reposo
- En tránsito
- End-to-end

## 4. Integración e Interoperabilidad de Datos

### 4.1 Patrones de Integración

1. ETL (Extract, Transform, Load)
2. ELT (Extract, Load, Transform)
3. Streaming
4. API-based

### 4.2 Herramientas y Tecnologías

- Apache Kafka
- Apache NiFi
- Talend
- Informatica

## 5. Caso Práctico: Sistema de Gobierno y Seguridad de Datos

### Ejercicio: Implementación de un Sistema de Control de Acceso y Auditoría

```python
from datetime import datetime
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
import logging
import hashlib

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class User:
    username: str
    role: str
    department: str
    permissions: List[str] = field(default_factory=list)
    attributes: Dict = field(default_factory=dict)

@dataclass
class DataAsset:
    name: str
    type: str
    classification: str
    owner: str
    location: str
    metadata: Dict = field(default_factory=dict)

class DataGovernanceSystem:
    def __init__(self):
        self.users = {}
        self.data_assets = {}
        self.access_logs = []
        self.policies = {}
        
    def add_user(self, user: User):
        """Añade un nuevo usuario al sistema"""
        self.users[user.username] = user
        logger.info(f"Usuario {user.username} añadido al sistema")
        
    def add_data_asset(self, asset: DataAsset):
        """Registra un nuevo activo de datos"""
        self.data_assets[asset.name] = asset
        logger.info(f"Activo de datos {asset.name} registrado")
        
    def add_policy(self, policy_name: str, policy_rules: Dict):
        """Define una nueva política de acceso"""
        self.policies[policy_name] = policy_rules
        logger.info(f"Política {policy_name} añadida")
        
    def check_access(self, username: str, asset_name: str, 
                    action: str) -> bool:
        """Verifica si un usuario tiene acceso a un activo de datos"""
        if username not in self.users or asset_name not in self.data_assets:
            return False
            
        user = self.users[username]
        asset = self.data_assets[asset_name]
        
        # Verificar políticas de acceso
        for policy_name, rules in self.policies.items():
            if asset.type in rules.get('asset_types', []):
                if user.role not in rules.get('allowed_roles', []):
                    return False
                if action not in rules.get('allowed_actions', []):
                    return False
                
        # Registrar intento de acceso
        self._log_access_attempt(username, asset_name, action, True)
        return True
        
    def _log_access_attempt(self, username: str, asset_name: str, 
                           action: str, success: bool):
        """Registra un intento de acceso"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'username': username,
            'asset': asset_name,
            'action': action,
            'success': success,
            'hash': self._generate_log_hash(username, asset_name, action)
        }
        self.access_logs.append(log_entry)
        
    def _generate_log_hash(self, username: str, asset_name: str, 
                          action: str) -> str:
        """Genera un hash para la entrada del log"""
        data = f"{username}{asset_name}{action}{datetime.now().isoformat()}"
        return hashlib.sha256(data.encode()).hexdigest()
        
    def generate_audit_report(self, start_date: Optional[datetime] = None, 
                            end_date: Optional[datetime] = None) -> List[Dict]:
        """Genera un reporte de auditoría"""
        filtered_logs = self.access_logs
        
        if start_date:
            filtered_logs = [log for log in filtered_logs 
                           if datetime.fromisoformat(log['timestamp']) >= start_date]
        if end_date:
            filtered_logs = [log for log in filtered_logs 
                           if datetime.fromisoformat(log['timestamp']) <= end_date]
            
        return filtered_logs
        
    def export_system_state(self, filename: str):
        """Exporta el estado del sistema a JSON"""
        state = {
            'users': {username: vars(user) for username, user in self.users.items()},
            'data_assets': {name: vars(asset) 
                          for name, asset in self.data_assets.items()},
            'policies': self.policies,
            'access_logs': self.access_logs
        }
        
        with open(filename, 'w') as f:
            json.dump(state, f, indent=4)

# Ejemplo de uso
governance_system = DataGovernanceSystem()

# Añadir usuarios
users = [
    User("john_doe", "data_analyst", "Analytics", 
         ["read", "analyze"], {"clearance": "level2"}),
    User("jane_smith", "data_scientist", "Research", 
         ["read", "write", "analyze"], {"clearance": "level3"})
]

for user in users:
    governance_system.add_user(user)

# Añadir activos de datos
assets = [
    DataAsset("customer_data", "personal", "confidential", 
             "Sales", "db01/customers"),
    DataAsset("sales_metrics", "metrics", "internal", 
             "Analytics", "db02/metrics")
]

for asset in assets:
    governance_system.add_data_asset(asset)

# Definir políticas
governance_system.add_policy("confidential_data", {
    "asset_types": ["personal"],
    "allowed_roles": ["data_scientist"],
    "allowed_actions": ["read", "analyze"]
})

# Probar acceso
print("\nVerificando acceso:")
print(f"John Doe -> customer_data: ", 
      governance_system.check_access("john_doe", "customer_data", "read"))
print(f"Jane Smith -> customer_data: ", 
      governance_system.check_access("jane_smith", "customer_data", "read"))

# Generar reporte de auditoría
print("\nReporte de Auditoría:")
audit_report = governance_system.generate_audit_report()
print(json.dumps(audit_report, indent=2))

# Exportar estado del sistema
governance_system.export_system_state("governance_system_state.json")
```

### Ejercicio Propuesto:
1. Extiende el sistema para incluir:
   - Encriptación de datos sensibles
   - Gestión de claves de acceso
   - Detección de anomalías
2. Implementa un sistema de notificaciones para violaciones de seguridad
3. Crea una interfaz web para la gestión del sistema de gobierno

## 6. Aplicaciones para el Servicio de Consumo de Datos

### 6.1 Tipos de Aplicaciones
- APIs REST
- GraphQL
- Data Lakes
- Data Marts
- Dashboards

### 6.2 Mejores Prácticas
1. Documentación
2. Versionado
3. Monitoreo
4. Escalabilidad
5. Seguridad

## Referencias

1. "Data Governance: How to Design, Deploy, and Sustain an Effective Data Governance Program" - John Ladley
2. "Database Design for Mere Mortals" - Michael J. Hernandez
3. "Data Security and Privacy" - David Knox

## Recursos Adicionales

- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [GDPR Guidelines](https://gdpr.eu/)
- [Cloud Security Alliance](https://cloudsecurityalliance.org/) 