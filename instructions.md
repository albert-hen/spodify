# instructions 

requires python 3.10

install requirements

```
pip install -r requirements.txt
```

download and generate data and load the database (takes about 90 seconds)

```
python3 spodify_load_demo.py
```

run demo script (this script runs the report queries implemented in spodify.py)

```
python3 spodify_query_demo.py
```

to run interactive web interface run the following command and open (a web interface to explore the data, view some report queries, and add song plays)

```
python3 flaskapp.py
```

to reset the database please run ```rm spodify.sqlite``` (or manually delete file) to remove the old database file then again run ```python3 spodify_load_demo.py```

# references

[python database tutorial](https://realpython.com/tutorials/databases/)