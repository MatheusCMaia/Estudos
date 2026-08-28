import subprocess

resultado = subprocess.run(
    ["ipconfig"],
    capture_output=True,
    text=True
)

print(resultado.stdout)



resultado_ping = subprocess.run(
    ["ping","8.8.8.8"],
    capture_output=True,
    text=True
)


with open('resultado-ping.txt','w',encoding='utf-8') as logping:
    logping.write(resultado_ping.stdout)


