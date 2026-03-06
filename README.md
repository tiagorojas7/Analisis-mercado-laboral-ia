# # Análisis de Estrategia de Talento y Salarios en IA 🚀
<img width="871" height="490" alt="image" src="https://github.com/user-attachments/assets/009d84bf-7a00-4d9c-bb30-2d3bb63cfd4f" />

# 🎯 Objetivo del Proyecto
Este proyecto nace de la necesidad de entender las dinámicas salariales y la demanda de habilidades en el mercado global de Inteligencia Artificial. Como **Analista de Datos**, mi objetivo fue transformar datos crudos en una herramienta de decisión que permita a empresas y profesionales identificar oportunidades estratégicas basándose en datos reales.

---

## 💼 Contexto de Negocio
En el ecosistema tecnológico actual, la IA es el área de mayor crecimiento. Sin embargo, para un departamento de Recursos Humanos o un profesional en formación, surgen preguntas críticas que no siempre son fáciles de responder con una simple búsqueda:
* ¿Qué tecnologías pagan mejor y cuánta presencia tienen en el mercado?
* ¿Estamos compitiendo por talento masivo o de nicho?
* ¿Es factible contratar perfiles Junior o el mercado exige exclusivamente expertos?
* Flexibilidad Laboral: ¿Existe un equilibrio entre las modalidades de trabajo (Remoto, Híbrido y Presencial) o el sector de IA muestra una inclinación predominante hacia alguna de ellas?
* Identificación de Nichos de Valor: Utilizando la relación Salario vs. Presencia, ¿qué herramientas se categorizan como "nichos de alta rentabilidad" (poca oferta pero pago elevado) frente a herramientas de "dominio masivo"?

Este análisis busca cerrar esa brecha de información utilizando un flujo de trabajo profesional de datos.

## ❓ Preguntas de Negocio
Para guiar el análisis, definí 4 preguntas clave que el proyecto debe responder:
1. **Remuneración:** ¿Cuáles son las habilidades tecnológicas con el salario promedio más alto?
2. **Relación Valor/Presencia:** ¿Existe una correlación entre lo que paga una skill y qué tan común es en las vacantes?
3. **Penetración de Mercado:** ¿Qué herramientas dominan el volumen total de ofertas laborales?
4. **Viabilidad de Contratación:** ¿Cuál es el mix de experiencia (Seniority) requerido para las tecnologías top?

---

---
## 🛠️ Fase 1: Extracción, Limpieza y Enriquecimiento (Python)

El éxito de cualquier análisis depende de la calidad de los datos. En esta fase, utilicé **Python (Pandas)** para transformar un dataset crudo en una estructura relacional optimizada para MySQL y Power BI.

### 1. Limpieza y Normalización
Para garantizar la integridad de los resultados, realicé las siguientes tareas:
* **Tratamiento de valores nulos:** Identifiqué y gestioné registros vacíos en salarios y localizaciones para evitar sesgos en los promedios.
* **Estandarización de nombre de trabajos :** Identifique valores con el mismo significado pero diferente nombre y los remplace por un unico nombre (primary data scientist, a data scientist)
* **Conversión de Monedas:** Aseguré que todos los salarios estuvieran en una métrica uniforme (**USD**) para permitir comparaciones lobales.

### 2. Enriquecimiento de Datos
Añadí valor al dataset mediante:
* **Mapeo de Seniority:** Clasifiqué los niveles de experiencia en etiquetas estandarizadas: **EN** (Entry), **MI** (Mid), **SE** (Senior) y **EX** (Executive).
* **Categorización de Trabajo:** Creé dimensiones para segmentar las vacantes en **Remoto, Híbrido y Presencial**.

### 3. Creación del Modelo Relacional
Para optimizar el rendimiento y seguir las mejores prácticas de bases de datos, dividí el dataset original en 4 tablas lógicas:
* **`companies`**: Información de las empresas y su ubicación.
* **`jobs`**: Detalles de las vacantes y modalidad de trabajo.
* **`salaries`**: Datos financieros y compensación anual.
* **`skills`**: Relación detallada de las habilidades técnicas requeridas por puesto.

* ### 📊 Flujo de Transformación de Datos
| Etapa | Archivo Fuente | Destino Final |
| :--- | :--- | :--- |
| **Ingesta** | `ai_job_dataset.csv` (Raw) | DataFrame Pandas |
| **Procesamiento** | Script Python | 4 Tablas Normalizadas (Processed) |
| **Carga** | CSVs Procesados | Base de Datos MySQL |

> [!NOTE]
> Esta estructura permite una mayor escalabilidad y facilita el análisis de relaciones complejas (uno a muchos) entre vacantes y habilidades.
---
## 🔍 Fase 2: Análisis Exploratorio con SQL

Una vez conectada mediante la libreria mysqlachademy desde python y estructurada la base de datos en MySQL, realicé un **EDA (Exploratory Data Analysis)** profundo para validar la consistencia de la información y extraer los primeros hallazgos.

### Validaciones Clave:
* **Integridad Referencial:** Verifiqué que cada `job_id` en la tabla de salarios y habilidades coincidiera con la tabla maestra de empleos.
* **Descubirmiento de insights:** Al definir las preguntas de negocio, busque las respuestas a traves de diferentes consultas que luego me serviran como validacion al momento de plasmarlas en PowerBi.
### Ejemplo de Consulta Estratégica:
Utilicé SQL para cruzar el promedio salarial con el volumen de vacantes, permitiéndome identificar las 10 habilidades que realmente mueven el mercado.

```sql
-- Validación de presencia de la 5 habilidades mejor pagadas
SELECT 
    s.skill_name, 
    COUNT(DISTINCT s.job_id) AS total_vacantes,
    AVG(sal.salary_usd) AS promedio_salarial
FROM skills 
JOIN salaries ON skills.job_id = salaries.job_id
GROUP BY skills.skill_name
ORDER BY promedio_salarial DESC
limit 5;
```
---
## 📊 Fase 3: Visualización e Insights (Power BI)
El resultado final son dos dashboards interactivos diseñados para diferentes perfiles (Recursos Humanos y Candidatos).

### 1. Dashboard: Salary Intelligence Report
Enfocado en la distribucion geografica y el promedio salarial.

<img width="871" height="490" alt="image" src="https://github.com/user-attachments/assets/0f365dd6-bbf6-4f04-802e-9535a29dcfd2" />

Insight Clave: La brecha salarial entre un perfil Junior (EN) y un Experto (EX) es de casi el 200%, con una fuerte concentración de companias de alto salario en Estados Unidos y Europa.

### 2. Dashboard: Strategic Talent & Technology Report
Enfocado en la relación entre demanda y valor.
<img width="871" height="490" alt="image" src="https://github.com/user-attachments/assets/009d84bf-7a00-4d9c-bb30-2d3bb63cfd4f" />

Insight Clave: Identifiqué que herramientas como docker y Deep Learning, scala son habilidades de "nicho de alto valor", mientras que Python y SQL son habilidades base esenciales con mayor volumen pero salarios más estandarizados.

> [!NOTE]
> Estos dos dashboards cuentan con diferentes segmentadores por categoria para que el usuario pueda visualizar la informacion que necesite fluida y comodamente.


💡 Conclusiones y Recomendaciones Especializadas
Para profesionales: La especialización en herramientas de despliegue y nube (como Docker o deep leraning ) ofrece el mejor retorno de inversión salarial.

Para empresas: El mercado de IA está altamente distribuido; ofrecer modalidades remotas o híbridas (que cubren el 67% de las vacantes analizadas) es clave para atraer talento competitivo.

---
## 📬 Contacto
¡Gracias por visitar mi proyecto! Estoy en búsqueda activa de mi primera oportunidad como Analista de Datos.

LinkedIn: [Tiago Rojas ](https://www.linkedin.com/in/tiago-rojas/)

Email: Tiagorojas1602@gmail.com

Portfolio: https://github.com/tiagorojas7?tab=repositories
