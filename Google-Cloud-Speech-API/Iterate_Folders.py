from google.cloud import storage

bucket = storage.Client().get_bucket('bucket')
blobs = list(bucket.list_blobs())

for blob in blobs:
    if blob.name.startswith("12345/wav/"):
        if not blob.name.endswith("_norm.wav"):
            print(blob.name)
