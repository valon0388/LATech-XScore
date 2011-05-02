/*
* Author: Hamad Borresly
* CWDI : 1000-6937
*	gcc server.c -o server
*
*	How to run?:
*	./server port
*
*
*/


#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <error.h>
#include <strings.h>
#include <unistd.h>
#include <arpa/inet.h>

#define ERROR    -1
#define MAX_CLIENTS    2 //maximum of two clients
#define MAX_DATA    1024


main(int argc, char **argv)
{
    struct sockaddr_in server;
    struct sockaddr_in client;
    int sock;
    int new,i;
    int sockaddr_len = sizeof(struct sockaddr_in);
    int data_len;
    char data[MAX_DATA];
    char temp[MAX_DATA];
    //the Request Attributes
    int id;
    int difficulty;
    char state;
    char category;
    char description[200];
    int bluepts;
    int redpts;
    //primary key(id) check bytes and process // check the bytes for in char in buffer
    
    
    
    if((sock = socket(AF_INET, SOCK_STREAM, 0)) == ERROR)
    {
        perror("server socket: ");
        exit(-1);
    }
        
    server.sin_family = AF_INET;
    server.sin_port = htons(atoi(argv[1])); //convert port to int
    server.sin_addr.s_addr = INADDR_ANY;
    bzero(&server.sin_zero, 8);
            
    if((bind(sock, (struct sockaddr *)&server, sockaddr_len)) == ERROR)
    {
        perror("bind : ");
        exit(-1);
    }
    
    if((listen(sock, MAX_CLIENTS)) == ERROR)
    {
        perror("listen");
        exit(-1);
    }
    printf("\nServer Waiting for client on port # %d\n",ntohs(server.sin_port));
        fflush(stdout);
    
    while(1) 
    {
        if((new = accept(sock, (struct sockaddr *)&client, &sockaddr_len)) == ERROR)
        {
            perror("accept");
            exit(-1);
        }
        
        printf("New Client has connected from port # %d and its IP is %s\n", ntohs(client.sin_port), inet_ntoa(client.sin_addr));

        data_len = 1;
    
                
        while(data_len)
        {
            data_len = recv(new, data, MAX_DATA, 0);
            printf("\n The mesg recieved from client is: %s", data);
            //change format for Decyrtion??
            	//decrepty here..
            //
            /*
            data[1] = 	1	;	//type cast to int
            data[2] =	2	;	//type cast to int
            data[3] =	3	;	//char this is the state
            data[4] =	3	;	//char hidden
            data[5] =	4	;	//char category
            data[6] =	4	;	// Description an array of char
            data[7] =	4	;	// type cast to int
            data[8] =	4	;	// type cast to int
            data[9] =   4	;	//new field
            */
            char checker[100];
            checker[1] = data[6];	//possible use of "memcopy"
            if (checker[1] == 'k')
            {
            	int n;
            	n = 2;
            
            }
            
            
            
            if(data_len)
            {
                
                send(new, data, data_len, 0);
                data[data_len] = '\0';
                printf("\n The msg sent to the client is: %s", data); //msj sent back to the client
            }
            
        }
        

        printf("The client has disconnected\n");
        
        close(new);
        
    }

    close(sock);
    

        
}


