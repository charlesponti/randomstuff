from pandas import DataFrame

def kensho_s3_client(data):
  # aws.s3.store(data)

class Airlock():
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def store(df: DataFrame) -> str:
    url = kensho_s3_client()
    return url