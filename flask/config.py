from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8000))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)

# 2 workers per cpu plus 1
workers = multiprocessing.cpu_count() * 2 + 1

# 2 threads per cpu
threads = 2 * multiprocessing.cpu_count()