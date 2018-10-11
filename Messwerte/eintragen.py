x = input( "in welche Messdatei sollen die Daten rein ?" )
kl=open( "messwerte" +x+ ".csv" , "w+" )
while True:
    n = input()
    if n == "exit" :
        break
    else:
        kl.write(n+ "," + "\n" )
