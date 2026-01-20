#-limpieza inicial, convertimos fechas a formato datetime y eliminamos duplicados
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
