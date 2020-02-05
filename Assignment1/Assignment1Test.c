#include <stdio.h>
#include <stdlib.h> 
#include <sys/types.h>
#include <unistd.h> 
#include <sys/wait.h>

int main(){
	// pid_t pid;
	char *onetoone[]={"~/kgallagher/sampleprogs/onetoone", "4", NULL};
	char *onto[]={"kgallagher/sampleprogs/onto","4", NULL};


	// pid_t pid=fork();
    // if (pid==0) { /* child process */
	// 	printf("It fucking works\n");
    //     static char *argv[]={"onetoone","",NULL};
    //     execv("~/kgallagher/sampleprogs/onetoone",argv);
    //     exit(127); /* only if execv fails */
	// 	printf("bigrip");
    // }
    // else { /* pid!=0; parent process */
	// 	printf("rip\n");
    //     waitpid(pid,0,0); /* wait for child to exit */
    // }


	// switch ((pid = fork()))
	// {
	// 	case -1:
	// 	/* Fork() has failed */
	// 	perror ("fork");
	// 	break;
	// 	case 0:
	// 	/* This is processed by the child */
	// 	execv ("~/kgallagher/sampleprogs/onetoone", onetoone);
	// 	puts("Uh oh! If this prints, execv() must have failed");
	// 	exit(EXIT_FAILURE);
	// 	break;
	// 	default:
	// 	/* This is processed by the parent */
	// 	puts ("This is a message from the parent");
	// 	break;
	// }
	



	// printf("Hello World\n");
	
	
	system("~/kgallagher/sampleprogs/onetoone 4");
	// system("~/kgallagher/sampleprogs/onto 4 | ~/CSE4415/Assignment1/Assignment1Cases");
	// system("~/kgallagher/sampleprogs/func 4 | ~/CSE4415/Assignment1/Assignment1Cases");
	// system("~/kgallagher/sampleprogs/reflex 4 | ~/CSE4415/Assignment1/Assignment1Cases");

	return 0;
}
