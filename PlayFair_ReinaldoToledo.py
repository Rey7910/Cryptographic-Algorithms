''''
Rey 7910

Playfair Algorithm 
Introduction to criptography and security of information
2023-1

'''


alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

matrix = [
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
    ['0','0','0','0','0'],
]



splited_message =[]
encrypted_blocks = []
decrypted_blocks = []

encrypted_message = ''

print("********\n\nRey 7910\nPlayfair Algorithm \nIntroduction to criptography and security of information\n2023-1\n\n********")

option = int(input("Welcome to the Playfair cipher programm, to encrypt a message please press 0, if you want to decrypt a message please press 1 (0/1): "))

if(option!=0 and option !=1):
  print("That was not a valide option")

if(option == 0):

 message = input("Enter the message you want to encrypt: ")

elif(option == 1):

 message = input("Enter the message you want to decrypt: ")


key = input("Enter the key for the playfair algorithm: ")
size = len(key)

index=0
out=False
j_i_found = False;
current_i = 0
current_j = 0



def print_encrypted_message(encrypted_blocks):

  print("\nYour encrypted message is:  ", end="")
  for i in encrypted_blocks:

    if(i[0]=='i' or i[0]=='j'):

      print("ij"+i[1],end="  ")

    elif(i[1]=='i' or i[1]=='j'):

      print(i[0]+"ij",end="  ")

    else:      

      print(i, end= "  ")


def print_decrypted_message(encrypted_blocks):

  print("\nYour decrypted message is:  ", end="")
  for i in encrypted_blocks:

    if(i[0]=='i' or i[0]=='j'):

      print("ij"+i[1],end="  ")

    elif(i[1]=='i' or i[1]=='j'):

      print(i[0]+"ij",end="  ")

    else:      

      print(i, end= "  ")

def print_matrix(matrix):

  print("\n\nThe cipher matrix is: \n")
  for i in range(5):

    for j in range(5):

      if(matrix[i][j]=='i' or matrix[i][j]=='j'):
        print('ij',end=" ")
      else:

        print(matrix[i][j],end = " ")

    print()



def split_message(message):
  index = 0;

  message = message.replace(' ','')
  
  while(index<len(message)):

    if(index == len(message)-1):
      splited_message.append(message[index]+'x')
      break
    elif(message[index]==message[index+1]):
      splited_message.append(message[index]+'x')
      index+=1
    
    else:
      splited_message.append(message[index]+message[index+1])
      index+=2

def decrypte_message(cipher_message):
  

  for y in cipher_message:

    for i in range(5):
      for j in range(5):
        
        if(matrix[i][j]==y[0]):
          index_column_1 = i
          index_row_1 = j
        
        elif(matrix[i][j]==y[1]):
          index_column_2 = i
          index_row_2 = j

        elif((y[0]=='i' or y[0]=='j') and (matrix[i][j]=='i' or matrix[i][j]=='j')):
          
          index_column_1 = i
          index_row_1 = j

        elif((y[1]=='i' or y[1]=='j') and (matrix[i][j]=='i' or matrix[i][j]=='j')):
          
          index_column_2 = i
          index_row_2 = j

    #print("block: ",y[0],y[1])
    #print("block 1 located in: ",index_column_1,' ',index_row_1)
    #print("block 2 located in: ",index_column_2,' ',index_row_2)

    index_new_column_1=0
    index_new_row_1 = 0

    index_new_column_2=0
    index_new_row_2 = 0

    if(index_row_1==index_row_2):

      index_new_column_1 = index_column_1-1
      index_new_column_2 = index_column_2-1
      if(index_new_column_1==-1):
        index_new_column_1=4
      if(index_new_column_2==-1):
        index_new_column_2=4
      
      #print("new encrypte value for block[0]: ",matrix[index_new_column_1][index_row_1])
      #print("new encrypte value for block[0]: ",matrix[index_new_column_2][index_row_2])

      decrypted_blocks.append(matrix[index_new_column_1][index_row_1]+matrix[index_new_column_2][index_row_2])
    
    
    elif(index_column_1==index_column_2):
      index_new_row_1 = index_row_1-1
      index_new_row_2 = index_row_2-1
      if(index_new_row_1==-1):
        index_new_row_1=4
      if(index_new_row_2==-1):
        index_new_row_2=4
      
      #print("new encrypte value for block[0]: ",matrix[index_column_1][index_new_row_1])
      #print("new encrypte value for block[0]: ",matrix[index_column_2][index_new_row_2])

      decrypted_blocks.append(matrix[index_column_1][index_new_row_1]+matrix[index_column_2][index_new_row_2])
    
    
    else:
      index_new_row_1 = index_row_2
      index_new_row_2 = index_row_1

      #print("new encrypte value for block[0]: ",matrix[index_column_1][index_new_row_1])
      #print("new encrypte value for block[1]: ",matrix[index_column_2][index_new_row_2])
      decrypted_blocks.append(matrix[index_column_1][index_new_row_1]+matrix[index_column_2][index_new_row_2])

def split_cipher_message(message):
  index = 0

  cipher_message = message.split("  ")

  

  for i in range(len(cipher_message)):

    if len(cipher_message[i])==3:
      cipher_message[i]=cipher_message[i].replace("j","")
      

  decrypte_message(cipher_message)
    

  

    



def encrypte(splited_message, matrix):

  index_row_1 = 0
  index_column_1 = 0

  index_row_2 = 0
  index_row_2 = 0


  for y in splited_message:

    for i in range(5):
      for j in range(5):
        
        if(matrix[i][j]==y[0]):
          index_column_1 = i
          index_row_1 = j
        
        elif(matrix[i][j]==y[1]):
          index_column_2 = i
          index_row_2 = j

        elif((y[0]=='i' or y[0]=='j') and (matrix[i][j]=='i' or matrix[i][j]=='j')):
          
          index_column_1 = i
          index_row_1 = j

        elif((y[1]=='i' or y[1]=='j') and (matrix[i][j]=='i' or matrix[i][j]=='j')):
          
          index_column_2 = i
          index_row_2 = j

    #print("block: ",y[0],y[1])
    #print("block 1 located in: ",index_column_1,' ',index_row_1)
    #print("block 2 located in: ",index_column_2,' ',index_row_2)

    index_new_column_1=0
    index_new_row_1 = 0

    index_new_column_2=0
    index_new_row_2 = 0

    if(index_row_1==index_row_2):

      index_new_column_1 = index_column_1+1
      index_new_column_2 = index_column_2+1
      if(index_new_column_1==5):
        index_new_column_1=0
      if(index_new_column_2==5):
        index_new_column_2=0
      
      #print("new encrypte value for block[0]: ",matrix[index_new_column_1][index_row_1])
      #print("new encrypte value for block[0]: ",matrix[index_new_column_2][index_row_2])

      encrypted_blocks.append(matrix[index_new_column_1][index_row_1]+matrix[index_new_column_2][index_row_2])
    
    
    elif(index_column_1==index_column_2):
      index_new_row_1 = index_row_1+1
      index_new_row_2 = index_row_2+1
      if(index_new_row_1==5):
        index_new_row_1=0
      if(index_new_row_2==5):
        index_new_row_2=0
      
      #print("new encrypte value for block[0]: ",matrix[index_column_1][index_new_row_1])
      #print("new encrypte value for block[0]: ",matrix[index_column_2][index_new_row_2])

      encrypted_blocks.append(matrix[index_column_1][index_new_row_1]+matrix[index_column_2][index_new_row_2])
    
    
    else:
      index_new_row_1 = index_row_2
      index_new_row_2 = index_row_1

      #print("new encrypte value for block[0]: ",matrix[index_column_1][index_new_row_1])
      #print("new encrypte value for block[1]: ",matrix[index_column_2][index_new_row_2])
      encrypted_blocks.append(matrix[index_column_1][index_new_row_1]+matrix[index_column_2][index_new_row_2])
    

for i in range(5):

  if(out):
    break;

  for j in range(5):

    
    while(key[index] in matrix[0] or key[index] in matrix[1] or key[index] in matrix[2] or key[index] in matrix[3] or key[index] in matrix[4] or key[index]==' ' or key[index]== 'i' and j_i_found==True or key[index]== 'j' and j_i_found==True):
      
      index +=1

      if(index == size):
        break;
    
    if(index==size):
      
      out=True;
      current_i = i
      current_j = j
      break;

      
    else:

      if(j_i_found==False and key[index]=='i' or key[index]=='j'):
        j_i_found=True

      matrix[i][j]=key[index]





alfabet_index = 0

out=False

for i in range(current_i,5):

  if(out):
    break;

  for j in range(5):

    if(i==current_i and j<current_j):
      continue
    
    while(alfabet[alfabet_index] in matrix[0] or alfabet[alfabet_index] in matrix[1] or alfabet[alfabet_index] in matrix[2] or alfabet[alfabet_index] in matrix[3] or alfabet[alfabet_index] in matrix[4]  or alfabet[alfabet_index]== 'i' and j_i_found==True or alfabet[alfabet_index]== 'j' and j_i_found==True):
      alfabet_index+=1

      if(alfabet_index==27):
        break
    
    if(alfabet_index==27):
     
      out=True;
      current_i = i
      current_j = j
      break;
    
    else:

      if(j_i_found==False and alfabet[alfabet_index]=='i' or alfabet[alfabet_index]=='j'):
        j_i_found=True

      matrix[i][j]=alfabet[alfabet_index]



print_matrix(matrix)


if(option == 0):

  split_message(message)

  encrypte(splited_message, matrix)

  print_encrypted_message(encrypted_blocks)

elif(option == 1):


  split_cipher_message(message)

  print_decrypted_message(decrypted_blocks)
  

  


  





