# vdhdr

vdhdr determines the MME type of video contained in a file or byte stream. It's based on python's imghdr

| formats|
|-------|
| mp4 |
| wmv |
| mov |
| mkv |
| ogg |
| avi |
| flv |

## Installation 

```bash
git clone https://github.com/f3mo/vdhdr.git
cd vdhdr
python3 setup.py install

```

## usage


```python
import vdhdr
vdhdr.what('test.flv') # returns string

vdhdr.what('test.gif') # returns None

```
