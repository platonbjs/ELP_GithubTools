#!/bin/bash
INPUT=data.csv
# data.csv debe estar en formato https://github.com/user/repo
TEXTO=texto
LICENSE=LICENSE
DATE=$(date +"%m%d%Y%H%M%S")
RESULT=result.$DATE
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read REPO FOLDER
do
  echo "*** REPO $REPO ***"
   if git clone $REPO&>/dev/null&&cd $FOLDER&&git checkout -b license&>/dev/null&&cp ../$LICENSE .&&git add LICENSE&>/dev/null  ; then
     echo "Creado repo"
     if git commit -m "Add license"&>/dev/null&&hub fork --remote-name=origin&>/dev/null&&git push origin license&>/dev/null&&hub pull-request -F ../$TEXTO &>/dev/null;then
       echo "Creado fork"
       date +"%d/%m/%Y" >> ../$RESULT
     else
       echo "Fallo al crear fork"
       echo "-" >> ../$RESULT
     fi
     cd ..
     rm -rf $FOLDER
   else
     echo "Fallo al crear repo"
     echo "-" >> ./$RESULT
   fi
  #

done < ./$INPUT
