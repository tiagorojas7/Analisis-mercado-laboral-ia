# Metodología y Contexto del Proyecto

Este documento detalla el enfoque analítico y las fases técnicas aplicadas para transformar datos crudos en insights estratégicos sobre el mercado de IA.

## 🏢 Origen de los Datos
Los datos utilizados provienen de un dataset extraido de kaggle (aplicacion que ofrece daatsets para trabajar)  global de vacantes de Inteligencia Artificial (2024-2025), que incluye información de más de **15,000 posiciones**.

## 🛠️ Stack Tecnológico
Para este proyecto se utilizó un flujo de trabajo moderno de análisis de datos:
* **Python (Pandas/SQLAlchemy):** Extracción, limpieza profunda y normalización.
* **MySQL:** Almacenamiento bajo un modelo relacional (Snowflake/Star Schema).
* **Power BI:** Modelado de datos (DAX) y creación de reportes interactivos.

## 📈 Definición de KPIs y Métricas
Para asegurar la relevancia del análisis, se definieron los siguientes indicadores clave:
1. **Average Salary USD:** Promedio anual de compensación base.
2. **Market Skill Presence:** Porcentaje de aparición de una tecnología sobre el total de vacantes.
3. **Average Hiring Time:** Tiempo estimado de cierre de vacante por país/industria.
4. **Salary Gap by Seniority:** Diferencia porcentual entre niveles Entry y Expert.

## 🔄 Proceso de Análisis
1. **Limpieza:** Eliminación de duplicados y manejo de valores nulos en salarios.
2. **Normalización:** Estandarización de nombres de cargos (ej: "Junior Data Scientist" -> "Data Scientist").
3. **Validación:** Cruce de datos en SQL para asegurar que los promedios coincidan con las realidades del mercado.

> [!NOTE]
> Este proyecto fue guiado y se trabajo mucho de la mano de la inteligencia artificial, para potenciar mis habilidades tecnicas como blandas. Tambien para eficientar el proyecto y validar errores en el aprendizaje continuo. 
