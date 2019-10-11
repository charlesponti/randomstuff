from pandas import DataFrame


def kensho_s3_client(data: DataFrame) -> str:
    """
    :param data:
    :return: The
    """
    # aws.s3.store(data)
    # Return ID for dataset
    return "some-dataset-id"


class Airlock():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create_dataset(self, df: DataFrame):
        return df

    @classmethod
    def store(self, df: DataFrame) -> str:
        url = kensho_s3_client(df)
        return url


airlock = Airlock()
df = DataFrame([1,2,3,4])
print(airlock.create_dataset(df))
