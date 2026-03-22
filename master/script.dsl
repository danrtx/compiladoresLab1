nodo1.run("backup.sh")
nodo2.run("backup.sh")
nodo3.run("deploy.sh")

deploy app1 to grupoA
deploy api to grupoB

grupoA.update()

sensor.temp > 30 -> alert()

parallel {
    nodo2.run("update.sh")
    nodo3.run("backup.sh")
}
