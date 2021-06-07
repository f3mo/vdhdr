# vdhdr
vdhdr determines the MME type of video contained in a file or byte stream. It's based on python's imghdr

| formats|
|---|
| mp4 |
| wmv |
| mov |
| mkv |
| ogg |
| avi |
| flv |

```python
import vdhdr
vdhdr.what('test.flv')

'flv'

```
