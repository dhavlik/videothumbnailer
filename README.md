Jugend hackt youtube thumbnail creator
====

Installation
----

```bash
git clone https://github.com/dhavlik/videothumbnailer.git
cd videothumbnailer
python3 -m venv .
bin/pip install opencv-python pillow youtube-dl
```

Usage:
----

edit the list of youtube urls in mkthumbs.py 

```bash
bin/python mkthumbs.py
```

Then select the desired frame you want to use (you can use mouse and cursor keys), choose monster overlay with space key and press "s" to save and proceed to the next video.

Todo:
----

Automatic uploading of created thumbnails via youtube api.
