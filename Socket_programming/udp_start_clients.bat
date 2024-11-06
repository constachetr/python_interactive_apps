@echo off
for /L %%i in (1,1,10) do (
    start py udp_client.py < udp_input_file.txt
)