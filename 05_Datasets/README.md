# Evolución de los Datos: De Raw a Relacional

En esta carpeta se documenta la transformación del dataset original hacia una estructura de **Modelo en Estrella (Star Schema)**.

### 1. Dataset Original (Raw)
* **Archivo:** `ai_job_dataset.csv`
* **Estado:** Datos desnormalizados, con valores nulos, duplicados y formatos de fecha/moneda inconsistentes.

<p align="center">
  <img src="https://github.com/user-attachments/assets/5f0b22ce-c706-4166-91a1-2418d64c93d2" width="90%" alt="Dataset Original Raw">
</p>

---

### 2. Datasets Procesados (Processed)
Para optimizar el rendimiento y evitar la redundancia, el dataset original se dividió en **4 tablas relacionales**. Esta estructura normalizada garantiza la integridad de los datos y eficiencia en las consultas.

| Tabla | Contenido |
| :--- | :--- |
| **`1. companies.csv`** | Información única de empresas y ubicaciones. | 
| **`2. jobs.csv`** | Detalles de puestos y modalidades de trabajo. |
| **`3. skills.csv`** | Relación de habilidades por cada vacante (N:M). |
| **`4. salaries.csv`** | Datos transaccionales de compensación y seniority. |

#### 📁 Vista Previa de Tablas Procesadas

| 1. Companies | 2. Jobs |
| :---: | :---: |
| <img src="https://github.com/user-attachments/assets/5ea1272a-ab30-471b-9615-14c5c81d7025" width="100%"> | <img src="https://github.com/user-attachments/assets/81166320-dd3f-488b-b4bd-8acc04e0d3a0" width="100%"> |
| **3. Skills** | **4. Salaries** |
| <img src="https://github.com/user-attachments/assets/c494468d-c172-42eb-a44b-2fd122b32773" width="100%"> | <img src="https://github.com/user-attachments/assets/0b378e99-2d4f-4406-a062-eae01e3c636f" width="100%"> |

> [!TIP]
> Esta división permite que el reporte de Power BI sea más ligero y que las consultas SQL sean mucho más rápidas al evitar la redundancia de datos.
