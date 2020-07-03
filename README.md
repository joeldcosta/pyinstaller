# pyinstaller
creating exe and adding icon &amp; version code

Watch Youtube Video first to understand how it all works:- https://youtu.be/boISYDbVcjs

<div align="center">
  <a href="https://www.youtube.com/watch?v=boISYDbVcjs"><img src="https://img.youtube.com/vi/boISYDbVcjs/0.jpg" alt="FULL PYTHON TO EXE TUTORIAL A to Z in one video"></a>
</div>

Building Executable

Run > CMD > pip install pyinstaller

pyinstaller.exe app.py

pyinstaller.exe --onefile app.py

pyinstaller.exe --onefile --windowed app.py

pyinstaller.exe --onefile --windowed --icon=app.ico app.py

pyinstaller.exe --onefile --windowed --icon=app.ico --version-file=version.txt app.py


Pyinstaller Error solutions:
https://stackoverflow.com/questions/37815371/pyinstaller-failed-to-execute-script-pyi-rth-pkgres-and-missing-packages

Q. How to put application run at startup?

Ans. 	a) Run > shell:startup [type enter]
	b) Create a shortcut and browse to your exe.

Note:- icon size should be 256x256


<p align="center">
  <img width="460" height="300" src="http://www.fillmurray.com/460/300">
</p>
