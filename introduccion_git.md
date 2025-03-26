# Introducción a Git: Guía Básica

## ¿Qué es Git?
Git es un sistema de control de versiones que te permite:
- Mantener un historial de cambios en tus archivos
- Trabajar en equipo de manera eficiente
- Revertir cambios cuando sea necesario
- Gestionar diferentes versiones de tu proyecto

## Configuración Inicial

### Configurar tu identidad
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Verificar la configuración
```bash
git config --list
```

## Comandos Básicos

### 1. Iniciar un Proyecto

#### Crear un nuevo repositorio
```bash
# Crear un nuevo directorio y entrar en él
mkdir mi_proyecto
cd mi_proyecto

# Inicializar un repositorio Git
git init
```

#### Clonar un repositorio existente
```bash
# Clonar un repositorio remoto
git clone https://github.com/usuario/nombre-repositorio.git
```

### 2. Trabajar con Archivos

#### Ver el estado de tu repositorio
```bash
# Muestra el estado de tus archivos
git status
```

#### Añadir archivos al staging area
```bash
# Añadir un archivo específico
git add nombre_archivo.txt

# Añadir todos los archivos
git add .
```

#### Crear un commit
```bash
# Crear un commit con un mensaje descriptivo
git commit -m "Añadido nuevo archivo de documentación"
```

### 3. Trabajar con Ramas

#### Crear y cambiar de rama
```bash
# Crear una nueva rama
git branch nueva-rama

# Cambiar a la nueva rama
git checkout nueva-rama

# Crear y cambiar de rama en un solo comando
git checkout -b nueva-rama
```

#### Fusionar ramas
```bash
# Cambiar a la rama principal
git checkout main

# Fusionar la rama nueva-rama en main
git merge nueva-rama
```

### 4. Trabajar con Repositorios Remotos

#### Conectar con un repositorio remoto
```bash
# Añadir un repositorio remoto
git remote add origin https://github.com/usuario/nombre-repositorio.git
```

#### Subir cambios al repositorio remoto
```bash
# Subir cambios a la rama principal
git push origin main

# Subir una nueva rama
git push -u origin nueva-rama
```

#### Obtener cambios del repositorio remoto
```bash
# Obtener cambios sin fusionar
git fetch

# Obtener y fusionar cambios
git pull
```

## Ejemplos Prácticos

### 1. Crear un Nuevo Proyecto
```bash
# Crear un nuevo proyecto
mkdir mi_web
cd mi_web

# Inicializar Git
git init

# Crear un archivo HTML
echo "<html><body><h1>Mi Web</h1></body></html>" > index.html

# Añadir y hacer commit del archivo
git add index.html
git commit -m "Creación inicial de la web"
```

### 2. Trabajar en una Nueva Característica
```bash
# Crear una rama para una nueva característica
git checkout -b feature/nuevo-diseno

# Hacer cambios en los archivos
echo "<style>body { background: blue; }</style>" >> index.html

# Guardar los cambios
git add index.html
git commit -m "Añadido nuevo diseño"

# Volver a la rama principal y fusionar
git checkout main
git merge feature/nuevo-diseno
```

### 3. Corregir un Error
```bash
# Crear una rama para la corrección
git checkout -b hotfix/error-ortografia

# Corregir el error
# (Editar el archivo)

# Guardar la corrección
git add .
git commit -m "Corregido error de ortografía"

# Fusionar la corrección
git checkout main
git merge hotfix/error-ortografia

# Eliminar la rama de corrección
git branch -d hotfix/error-ortografia
```

## Consejos Prácticos

1. **Haz commits frecuentes y pequeños**
   - Mejor: "Añadido botón de inicio de sesión"
   - Peor: "Actualizado todo el proyecto"

2. **Usa mensajes de commit descriptivos**
   - Mejor: "Corregido error de cálculo en el módulo de facturación"
   - Peor: "Arreglado bug"

3. **Mantén la rama principal limpia**
   - Trabaja en ramas separadas para nuevas características
   - Fusiona solo cuando el código esté probado

4. **Revisa tus cambios antes de hacer commit**
   ```bash
   # Ver cambios en archivos
   git diff
   
   # Ver cambios en archivos en staging
   git diff --staged
   ```

## Recursos Adicionales

- [Documentación oficial de Git](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf) 