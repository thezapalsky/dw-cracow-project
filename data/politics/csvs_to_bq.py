

from google.cloud import bigquery

client = bigquery.Client.from_service_account_json('dataworkshop/dw-cracow-project/data/politics/secrets/dw-project-politics-bq-credentials.json')

def load_bq_table_from_csv(client, dataset_id, table_id, filename, skip_leading_rows=0):
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = skip_leading_rows
    job_config.autodetect = True

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    try:
        job.result()  # Waits for table load to complete.
    except Exception as err:
        print(err)

    print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))

    return job

#if __name__ == 'main':
load_bq_table_from_csv(
    client, 
    filename = '/Users/piotr.jodko/Google Drive/currents/votings/voting-8_1_3.csv', 
    dataset_id = 'politics', 
    table_id = 'votings'
    )