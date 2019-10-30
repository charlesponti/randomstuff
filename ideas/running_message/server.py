import grpc
from concurrent import futures
import time
from google.protobuf.empty_pb2 import Empty

# import the generated classes
from definitions.running_message_pb2 import RunningMessageResponse
from definitions.running_message_pb2_grpc import RunningMessageServicer, add_RunningMessageServicer_to_server

# import running_message function
import running_message

import db

database = db.Database()

database.add_table('running_metrics')


# create a class to define the server functions, derived from
# running_message_pb2_grpc.RunningMessageServicer
class RunningMessageServer(RunningMessageServicer):

    # running_message.get_message is expose here
    # the request and resposne are of the data type
    # running_message_p2.RunningMessage
    def GetRunningMessage(self, request, context):
        response = RunningMessageResponse()
        response.message = running_message.return_message(request.distance, request.time)
        return response

    def LogRunningMetrics(self, request, context):
        for running_metric in request:
            database.add_to_table('running_metrics', running_metric)
        return Empty

    def GetRunningMetrics(self, request, context):
        metrics = database.get_table('running_metrics')
        for metric in metrics:
            yield metric

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

add_RunningMessageServicer_to_server(RunningMessageServer(), server)

print('Starting server. Listening on port 50051')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
