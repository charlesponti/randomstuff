import grpc

from google.protobuf.empty_pb2 import Empty
from definitions.running_message_pb2 import RunningDetails, RunningMetrics
from definitions.running_message_pb2_grpc import RunningMessageStub

# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

stub = RunningMessageStub(channel)

running_details = RunningDetails(distance=4.74, time=37.4)


def generate_metrics():
    running_metrics = [
        RunningMetrics(
            distance=0.14, heart_rate=176, time_stamp="2019-10-09T07:14:30.000z"
        ),
        RunningMetrics(
            distance=0.20, heart_rate=186, time_stamp="2019-10-09T07:15:30.000z"
        ),
        RunningMetrics(
            distance=0.23, heart_rate=183, time_stamp="2019-10-09T07:16:30.000z"
        ),
    ]
    for metric in running_metrics:
        yield metric


response = stub.GetRunningMessage(running_details)

metrics_response = stub.LogRunningMetrics(generate_metrics())

get_metrics_response = stub.GetRunningMetrics(Empty())

# print(response)
# print(metrics_response)
for metric in get_metrics_response:
    print(metric)
