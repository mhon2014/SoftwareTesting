# #!/bin/bash
# # Script to compile and execute a c program in one step.

# # Get file name without the .c extension
# file_name=$(echo $1|sed 's/\(.*\)\.c/\1/')

# # Compile the program with -o option to specify the name of the binary
# gcc -o $file_name.out $1

# # If there were no compilation errors, run the program
# if [[ $? -eq 0 ]]; then
#         ./$file_name.out
# fi

#!/bin/bash 
USAGE="Usage: $0"
if [ "$#" == "0" ]; then
echo "$USAGE Please Enter Username"
exit 1
fi

user=$1@code01.fit.edu
sampleprogs=kgallagher/sampleprogs/
oraclesprogs=kgallagher/oracles/
localprogram=./Assignment2Test.py

# echo $TESTSITE

GENERATORS=(
             func
             reflex
             onetoone
             onto
            )
TARGETS=( 
            func
	          reflex
            onetoone 
            onto
         )

arguments=(
            0
            100
            500
)

for ((II=0; II < ${#GENERATORS[@]}; ++II)) do

  for ((J = 0; J < ${#arguments[@]}; ++J)) do

    echo $user~/$sampleprogs${GENERATORS[II]} ${arguments[J]}
    ssh $user $sampleprogs${GENERATORS[II]} ${arguments[J]} | $localprogram
  done

##  ssh $TESTSITE $SAMPLEPROGS${GENERATORS[II]} $1 $2  | /usr/bin/time --verbose  ./${TARGETS[II]}  

done

#ssh andrew.cs.fit.edu public_html/sampleprogs/ref.trans  100 20 |  tee >(ssh andrew.cs.fit.edu  public_html/oracles/ref.sym) >(./ref.sym)  >(./ref.trans) > /dev/null
