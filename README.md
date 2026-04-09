# PDF ExtractText

Sistema que permite extraer texto de archivos PDF y, mediante el uso de inteligencia artificial, convertir dicho contenido a formato Markdown (.md).

---

## Tecnología

El sistema está diseñado con un enfoque en el rendimiento y la escalabilidad. Su arquitectura permite la incorporación de nuevas funcionalidades.

- Python  
- UV (gestión de dependencias y entornos virtuales)  
- Modelo de Inteligencia Artificial: Kimi  
- MongoDB (base de datos NoSQL)  

---

## Metodología

Metodologías y buenas prácticas aplicadas durante el desarrollo para garantizar la calidad y la mantenibilidad del sistema.

- Desarrollo guiado por pruebas (TDD):
  - Red: pruebas que inicialmente fallan  
  - Green: implementación mínima para que las pruebas pasen  
  - Refactor: mejora continua del código manteniendo las pruebas en verde  

- Aplicación de principios de Clean Code:
  - Nombres descriptivos que reflejan la intención del código  
  - Principio de responsabilidad única (SRP)  
  - Aplicación del principio DRY (Don't Repeat Yourself)  
  - Funciones pequeñas y bien organizadas, con responsabilidades claras
  - Código orientado a la legibilidad y mantenibilidad  

- Implementación parcial de Twelve-Factor App:
  - I. Codebase: una única base de código versionada  
  - II. Dependencies: declarar y aislar las dependencias  
  - III. Configuraciones: guardar la configuracion en el entorno 
  - IV. Backing Services: servicios tratados como recursos conectables 
  - V. Construir, desplegar, ejecutar: separar la construccion de la ejecución
  - VI. Processes: ejecución como procesos sin estado  
