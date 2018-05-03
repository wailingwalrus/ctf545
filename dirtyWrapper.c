#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(int argc, int *argv[]){
	if(argc > 1){
		//printf("%s\n",argv[1]);
		int i;
		int alert = 0;
		for(i=1;i<argc;i++){
			if(strchr(argv[i],'|') == NULL){
				if(strchr(argv[i],'\\') == NULL){
					if(strchr(argv[i],';') == NULL){
						if(strchr(argv[i],'^') == NULL){
							if(strchr(argv[i],'&') == NULL){
								if(strchr(argv[i],'!') == NULL){
									if(strchr(argv[i],'(') == NULL){
										if(strchr(argv[i],')') == NULL){
											if(strchr(argv[i],'{') == NULL){
												if(strchr(argv[i],'}') == NULL){
													if(strchr(argv[i],'\x90') == NULL){
													}
													else{alert = 1;}
												}
												else{alert = 1;}
											}
											else{alert = 1;}
										}
										else{alert = 1;}
									}
									else{alert = 1;}
								}
								else{alert = 1;}
							}
							else{alert = 1;}
						}
						else{alert = 1;}
					}
					else{alert = 1;}
				}
				else{alert = 1;}
			}
			else{alert = 1;}
			if (alert == 1){
				printf("sorry goons don't get to execute stuff\n");
				exit(0);
			}
		}
		if(alert == 0){
			execv("/home/kyle/Zephyrus/Documents/Google Drive/School/CSE 545/CTF 4/helloworld_real",argv);
		}
	}
	else {
		execv("/home/kyle/Zephyrus/Documents/Google Drive/School/CSE 545/CTF 4/helloworld_real",argv);
	}
	printf("sorry goons don't get to execute stuff\n");	
}