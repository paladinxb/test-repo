@echo off
cd /d D:\Coding\work\test-repo

:: Добавляем все изменения
git add .

:: Фиксируем изменения с сообщением
git commit -m "auto commit"

:: Отправляем изменения в удалённый репозиторий
git push origin main

pause