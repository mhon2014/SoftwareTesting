all:
	@echo "Test"

# load:
# 	@module @load @gcc

compilecpp: Assignment1Test.cpp
	g++ -o Assignment1Test Assignment1Test.cpp

compile: Assignment1Test.c Assignment1Cases.cpp
	gcc -o Assignment1Test Assignment1Test.c && gcc -o Assignment1Cases Assignment1Cases.c

run:
	./Assignment1Test

clean:
	rm ./Assignment1Test ./Assignment1Cases

cleancpp:
	rm ./Assignment1Test