

    /*

     * C program to perform matrix multiplication using iterative

     */

    #include<stdio.h>    
    #include<stdlib.h>
    #include<time.h>
    #define SIZE 1000
    static int m1[SIZE][SIZE],m2[SIZE][SIZE],mul[SIZE][SIZE] = {0};
    int main()

    {

        int r1,r2,c1,c2;
        time_t seconds1,seconds2,diff;

            for(int i=0;i<SIZE;i++)    

            {    

                for(int j=0;j<SIZE;j++)    

                {    
                    int temp = rand()%100 + 1;
                    m1[i][j]=temp;  

                }    

            }    
 

            for(int i=0;i<SIZE;i++)    

            {    

                for(int j=0;j<SIZE;j++)    

                {    

                    int temp = rand()%100 + 1;
                    m2[i][j]=temp;
                }    

            }    

            //int 
            seconds1=time(NULL);
            for(int i=0;i<SIZE;i++)    

            {    

                for(int j=0;j<SIZE;j++)    

                {    

                    mul[i][j]=0; 

     

                    // Multiplying i’th row with j’th column

                    for(int k=0;k<SIZE;k++)    

                    {    

                        mul[i][j]+=m1[i][k]*m2[k][j];    

                    } 

                }    

            }    
            seconds2=time(NULL);
            diff=seconds2-seconds1;
       /*     printf("Multiplied matrix\n");     

            for(int i=0;i<SIZE;i++)    

            {    

                for(int j=0;j<SIZE;j++)    

                {    

                    printf("%d\t",mul[i][j]);    

                }    

                printf("\n");    

            } 
        */
            printf("Time taken for multiplication is - %ld\n",diff);

       // }

        return 0;  

    }