@echo off
for /L %%i in (1,1,100) do (
    start py client.py < input_file.txt
)
