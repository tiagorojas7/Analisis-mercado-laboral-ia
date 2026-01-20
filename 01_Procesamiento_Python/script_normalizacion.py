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
