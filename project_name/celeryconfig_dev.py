import os

host = redis_host = rabbitmq_host = '127.0.0.1'   # Windows бачить Redis через localhost
redis_port = '12000'
rabbitmq_port = '13000'
broker_url = f'amqp://guest:guest@{rabbitmq_host}:{rabbitmq_port}//'
# broker_url = f'redis://{redis_host}:{redis_port}/0'

broker_transport_options = {'visibility_timeout': 3600}

# accept_content = ['application/json']
accept_content = ['pickle', 'json']
task_serializer = 'json'###тут відбувається балячка з pickle сереалізатором 
result_serializer = 'json'##тобто ці параметри працють саме глобально для всього і не можна окремо ізолювати до кожної таски інший серелізатор 

result_backend = f'redis://{redis_host}:{redis_port}/0'

enable_utc = True
timezone = 'Europe/London'

celery_trace_app = 1

# task_ignore_result = True

# Flower settings
os.environ['flower_unauthenticated_api'] = 'True'

# result_expires = 300
# task_always_eager = True
# task_eager_propagates = True