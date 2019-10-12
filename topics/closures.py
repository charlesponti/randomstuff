
def transaction_closure(fn):
  def wrapper(value, **kwargs):
    if not value:
      raise Exception(f"{value} is not truthy")
    return fn(value, **kwargs)
  return wrapper

@transaction_closure
def some_function(value):
  print(f"{value} is truthy")

some_function("Whattttt")
some_function(15)
some_function(True)


def transformer(*args, **kwargs):
  def rabbitmq_transformer(args, **kwargs):
    return "I'm going to use RabbitMQ as my Scheduler"

  def kafka_transformer(args, **kwargs):
    return "I'm going to use Kafka as my Scheduler"

  def microservice(args, **kwargs):
    print("I do not have a scheduler to control me so I'll be a microservice")
    return args

  if args[1] == "rabbitmq":
    return rabbitmq_transformer(args)
  elif args[0] == "kafka":
    return kafka_transformer(args)
  else:
    return microservice(args)

rabbitmq_transformer = transformer("rabbitmq", "kafka")
print(rabbitmq_transformer)