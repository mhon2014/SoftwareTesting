
#!/bin/bash

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
        onto
        reflex
        func
        sym
        trans
        eq
        )

arguments=(
            # 0
            100
            # 500
)

for i in $GENERATORS #for each file in the testpath
do
    for j in $arguments #for each argument I made
    do
        sleep 1
        echo'' 
        echo $TESTSITE $TESTPATH$i $j #just to check what I'm running
	      echo $TESTPATH$i $j #ignore the ugly one liner on the next line
        ssh $TESTSITE $TESTPATH$i $j | tee >(ssh $TESTSITE $TARGETPATH${TARGETS[0]}) >(ssh $TESTSITE $TARGETPATH${TARGETS[1]}) >(ssh $TESTSITE $TARGETPATH${TARGETS[2]}) >(ssh $TESTSITE $TARGETPATH${TARGETS[3]}) >(ssh $TESTSITE $TARGETPATH${TARGETS[4]}) >(ssh $TESTSITE $TARGETPATH${TARGETS[5]}) >(ssh $TESTSITE $TARGETPATH${TARGETS[6]}) >(gtime -f 'Local Process:\nElapsed time: %e' python3 Assignment2Test.py) >/dev/null
        echo''
        sleep 1
    done
done

#http://man7.org/linux/man-pages/man1/time.1.html gtime -f