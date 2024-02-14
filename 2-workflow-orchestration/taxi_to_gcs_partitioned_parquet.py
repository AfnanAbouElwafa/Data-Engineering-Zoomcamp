import pyarrow as pa
import pyarrow.parquet as pq
from pandas import DataFrame
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/logical-pathway-413019-945ddc47643c.json'
project_id = 'logical-pathway-413019'
bucket_name = 'mage-zoomcamp-ted'
object_key = 'ny_green_taxi_data.parquet'
table_name = 'ny_green_taxi_data'
root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #create pyarrow table
    table = pa.Table.from_pandas(data)

    #find gcp object
    gcs = pa.fs.GcsFileSystem()

    #parquet to dataset
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
