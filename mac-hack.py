from subprocess import call as shell

print("welcome to /\/\\ak  C|-|ANGER")
mac = input("введите новый мак-адресс: ")

shell("sudo ifconfig eth0 down", shell=True)
shell("sudo ifconfig eth0 ether "+str(mac), shell=True)
shell("sido ifconfig eth0 up", shell=True)
