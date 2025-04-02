import sys
import logging
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType

# Configurar logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Parámetros del job
args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'input_path',    # Ruta de entrada en S3 
    'output_path',   # Ruta de salida en S3
    'file_format'    # Formato del archivo de salida (csv, parquet, etc.)
])

# Inicializar el contexto de Spark y Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Función para limpiar nombres de columnas
def clean_columns(df):
    """
    Limpia los nombres de las columnas:
    - Convierte a minúsculas
    - Reemplaza espacios por guiones bajos
    - Reemplaza barras por guiones bajos
    """
    df_cleaned = df
    new_columns = [str(col_name).lower().replace(" ", "_").replace("/","_") for col_name in df.columns]
    df_cleaned = df_cleaned.toDF(*new_columns)
    return df_cleaned

# Parámetros de entrada y salida
input_path = args['input_path']
output_path = args['output_path']
file_format = args.get('file_format', 'csv')  # Formato por defecto: CSV

logger.info(f"Iniciando procesamiento: {input_path} -> {output_path}")

# Leer datos desde S3
try:
    # Leer archivo CSV
    input_df = spark.read.option("header", "true") \
                         .option("inferSchema", "true") \
                         .csv(input_path)
    
    logger.info(f"Archivo leído correctamente. Filas: {input_df.count()}, Columnas: {len(input_df.columns)}")
    
    # Aplicar la limpieza de columnas
    cleaned_df = clean_columns(input_df)
    logger.info("Columnas normalizadas correctamente")
    
    # Escribir el resultado en S3
    if file_format.lower() == 'csv':
        cleaned_df.write.mode("overwrite") \
                       .option("header", "true") \
                       .csv(output_path)
    elif file_format.lower() == 'parquet':
        cleaned_df.write.mode("overwrite") \
                       .parquet(output_path)
    else:
        logger.warning(f"Formato no soportado: {file_format}. Guardando como CSV")
        cleaned_df.write.mode("overwrite") \
                       .option("header", "true") \
                       .csv(output_path)
    
    logger.info(f"Datos guardados exitosamente en: {output_path}")
    
except Exception as e:
    logger.error(f"Error durante el procesamiento: {str(e)}")
    raise

# Finalizar el job
job.commit()
logger.info(f"Job {args['JOB_NAME']} completado con éxito")