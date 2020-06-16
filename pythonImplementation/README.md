# Briq Challenge

To run several packages need to be installed.

``` python
pip3 install spacy
pip3 install numpy
python -m spacy download en_core_web_lg
pip3 install flask
```

There also needs to be an env variable for flask. 
``` shell
export FLASK_APP=spacyver.py
```

This iteration went pretty well. Although flask was brand new it was pretty fun.
Only thing that does not work is the POST not returning TRUE for some reason. Other than that the page works and does
what it is supposed to. Although it does not look very pretty...
