# instructions 

requires python 3.10, which comes with sqlite

clone repository and enter repository
```
git clone https://github.com/albert-hen/spodify.git
cd spodify
```

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

files written by me
```
flaskapp.py
generate_data.py
spodify_load_demo.py
spodify_query_demo.py
spodify.py
```

file with code not written by me
```
sqlite_setup.py
```

sqlite connection code used in ```sqlite_setup.py``` is from [python database tutorial](https://realpython.com/tutorials/databases/)

data downloaded from [here](https://corgis-edu.github.io/corgis/datasets/csv/music/music.csv) as ```music.csv```

```cracklib-small``` is a word list for username generation and is extracted from my ubuntu installation, source is likely [this](https://github.com/cracklib/cracklib/blob/master/src/dicts/cracklib-small)
