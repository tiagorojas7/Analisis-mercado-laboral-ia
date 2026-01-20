# Importamos librerias
import pandas as pd 
from sqlalchemy import create_engine
import os 
import datetime as dt 

#-1 definimos ruta de acceso a la carpeta 
ruta = r"C:\Users\santr\OneDrive\Escritorio\Tiago Facu\Archivos proyectos analisis trabajos IA"
os.chdir(ruta)

#-2 cargar el dataset 
df = pd.read_csv("ai_job_dataset.csv")
# obtenemos una vista previa de los 5 primeros registros 
print(df.head(5))

#-4 limpieza inicial, convertimos fechas a formato datetime y eliminamos duplicados
df["posting_date"]=pd.to_datetime(df["posting_date"])
df["application_deadline"]= pd.to_datetime(df["application_deadline"])
#Eliminamos cualquier tipo de duplicado que haya
df = df.drop_duplicates(subset=["job_id"],keep="first")
#Verificamos si hay valores nulos
print("valores nulos por columna:")
print(df.isnull().sum())
#Analizamos si hay errores de escritura en las columnas 
categorias = ['experience_level', 'employment_type', 'company_size', 'industry',"company_name","education_required","employee_residence","company_location"]
for col in categorias:
    print(f"--- Valores únicos en {col} ---")
    print(df[col].unique())
    print("\n")
# Verificamos si hay fechas imposible 
errores_fecha = df[df["application_deadline"]<df["posting_date"]]
print(f"registros con fechas que no coinciden: {len(errores_fecha)}")
# Remplamos valores ya que consideramos necesario para su correcto analisis.
df["job_title"]= df["job_title"].replace("Principal Data Scientist","Data Scientist")

#Enrequecimiento del dataset con metricas
#-1 calcular los dias que esta abierta la vacante 
df["time_to_apply"]=df["application_deadline"]-df["posting_date"]
df['time_to_apply'] = df['time_to_apply'].dt.days
# Segmentamos los tipos de salarios en tres categorias. 
df['salary_segment'] = pd.qcut(df['salary_usd'], q=3, labels=["low", 'Medium', 'high'])
# Identificamos si el trabajo es internacional o local 
df["is_international"]=df["company_location"]!=df["employee_residence"]
# convertimos habilidades en una LISTA para un analisis mas facil
df["skills_list"]=df["required_skills"].apply(lambda x:[s.strip()for s in str(x).split(",")])


#Convertimos el CSV en un modelo estrella (creamos tablas relacionales)
#Vamos a crear 4 tablas diferentes. 
#-1 Tabla Empleos 
dim_jobs=df[["job_id","job_title","experience_level","employment_type","education_required"]].copy()
#-2 Tabla compania
dim_company=df[["job_id","company_name","company_location","company_size","industry","is_international"]].copy()
#-3 Tabla skills 
real_job_skills = df[['job_id', 'skills_list']].explode('skills_list') #explotamos la lista de skills para que esten en una fila individual
real_job_skills = real_job_skills.rename(columns={'skills_list': 'skill_name'}) #renombramos la columna
# Limpiamos posibles espacios en blanco residuales
real_job_skills['skill_name'] = real_job_skills['skill_name'].str.strip()
fact_salaries = df[['job_id', 'salary_usd', 'remote_ratio', 'benefits_score', "time_to_apply", "years_experience", 'salary_segment']].copy()
# Convertimos la columna time_to_apply en entera para que sea mejor su manipulacion.
fact_salaries['time_to_apply'] = fact_salaries['time_to_apply'].astype(int)

#Verificamos la normalizacion de nuestro datasets
print("TABLA EMPLEOS")
print(dim_jobs.head(5))
print("TABLA EMPRESAS")
print(dim_company.head(5))
print("TABLA SKILLS")
print(real_job_skills.head(5))
print("TABLA SALARIOS Y BENEFICIOS")
print(fact_salaries.head(5))

#Exportamos nuestros DATASETS a MYSQL 
database = {
    'host': '127.0.0.1',          
    'user': 'root',                
    'password': 'root',     
    'database': 'ai_job_analitics',
    'port': 3306                   
}

connection_string = f"mysql+mysqlconnector://{database['user']}:{database['password']}@{database['host']}:{database['port']}/{database['database']}"
con=create_engine(connection_string)

print("EXPORTANDO ARCHIVOS A TU BASE DE DATOS SQL...")

dim_jobs.to_sql("jobs", con=connection_string, if_exists='replace', index=False)
dim_company.to_sql('companies', con=connection_string, if_exists='replace', index=False)
real_job_skills.to_sql('skills', con=connection_string, if_exists='replace', index=False)
fact_salaries.to_sql("salaries", con=connection_string, if_exists='replace', index=False)

print("Archivos exportados correctamente a tu base de datos Sql")

