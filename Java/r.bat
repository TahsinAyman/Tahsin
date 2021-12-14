cls
cd src\root
javac App.java
cls
cd..
cd..
copy src\root\App.class bin\root
copy src\root\App.class out\production\Java\root\
del src\root\App.class
cd bin
cls
java root.App
pause
cd..
cls
