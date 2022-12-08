# spodify

individual project for cs 6400 @ gatech

this is a music social media database application

# how to run

install requirements

```
pip install -r requirements.txt
```

download and generate data and load the database (takes about 90 seconds)

```
python3 spodify_load_demo.py
```



to run demo script

```
python3 spodify_query_demo.py
```


to reset the database please run ```rm spodify.sqlite``` to remove the old database file then run ```python3 spodify_load_demo.py```