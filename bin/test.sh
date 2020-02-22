MAIN=app/main

py -m coverage run --omit=env/** \
    --source=$MAIN/controller,$MAIN/service,$MAIN/model \
    -m pytest

py -m coverage html

open htmlcov/index.html