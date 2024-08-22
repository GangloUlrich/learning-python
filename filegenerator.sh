#!/bin/bash

for i in {17..60}
do 
 touch "exercice$i.py"
 chmod 666 "exercice$i.py"
done

echo "Tous les fichiers sont créés" 

