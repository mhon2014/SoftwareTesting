
#!/bin/bash

> output.txt #empty text file
> runtime.txt #empty text file

USAGE="Usage: $0 "
if [ "$#" == "0" ]; then
    echo "$USAGE" please enter Username
    exit 1
fi

TESTSITE=$1@code01.fit.edu #using argument 1 for user
TESTPATH=kgallagher/sampleprogs/ #sampleprogs path in my udrive
TARGETPATH=kgallagher/oracles/ #oracles path in my udrive

GENERATORS=$(ssh $TESTSITE ls $TESTPATH) #list of all the files in the path
# TARGETS=$(ssh $TESTSITE ls $TARGETPATH) #couldn't figure how to do it wihtout using ugly one liner

TARGETS=(
        onetoone
        onto  #I don't know why onto in the oracles takes so long.....
        reflex
        func
        sym
        trans
        eq
        )

arguments=(
          0
          5
          )

for ((II = 0; II < ${#arguments[@]}; ++II)) #for each argument 
do
    for JJ in $GENERATORS #for each file in the testpath
    do
        # echo'' 
        # echo $JJ`
        # echo $II
	      echo $TESTPATH$JJ ${arguments[II]} | tee -a output.txt #ignore the ugly one liner on the next line
        ssh $TESTSITE $TESTPATH$JJ $II | tee >(
          gtime --quiet -o runtime.txt -a -f 'Oracles onetoone runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[0]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Oracles onto runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[1]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Oracles reflex runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[2]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Oracles func runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[3]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Oracles sym runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[4]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Oracles trans runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[5]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Oracles eq runtime: %e & memory: %K' ssh $TESTSITE $TARGETPATH${TARGETS[6]} >>output.txt
          ) >(
            gtime --quiet -o runtime.txt -a -f 'Local Program runtime %e & memory: %K' python3 Assignment3Test.py >>output.txt) >/dev/null
        echo''
        sleep 1
    done
done


#http://man7.org/linux/man-pages/man1/time.1.html gtime -f