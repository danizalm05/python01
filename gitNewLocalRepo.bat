cls
 
@echo off
del .git 
pause
git init

pause
git remote add origin https://github.com/danizalm05/python01.git

git remote -v
pause 
cls
git pull   origin master
pause
