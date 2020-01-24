def transformer(*args, **kwargs):
    def rabbitmq_transformer(args, **kwargs):
        print("I'm going to use RabbitMQ as my scheduler")
        return args

    def kafka_transformer(args, **kwargs):
        print("I'm going to use Kafka as my scheduler")
        return args

    def microservice(args, **kwargs):
        print("No scheduler defined so I'll be a microservice")
        return args

    if not args:
        return microservice(args)
    elif args[0] == "rabbitmq":
        return rabbitmq_transformer(args)
    elif args[0] == "kafka":
        return kafka_transformer(args)


rabbitmq_transformer = transformer()
print(rabbitmq_transformer)
