#Q2. Devise a solution to the problem
#TOWER OF HANOI PUZZLE

def TowerOfHanoi(n,sor_rod,aux_rod,des_rod):
    if n==1:
        print("Move disk 1 from rod",sor_rod,"to rod",des_rod)
        return
    
    TowerOfHanoi(n-1,sor_rod,des_rod,aux_rod)
    
    print("Move disk",n,"from rod",sor_rod,"to rod",des_rod)
    
    TowerOfHanoi(n-1,aux_rod,sor_rod,des_rod)



print("Enter the number of disks")
n=int(input())

TowerOfHanoi(n,'A','B','C')
#n stands for number of disk
#A for source rod
#B for auxiliary rod or intermidiate rod
#C for destination rod
