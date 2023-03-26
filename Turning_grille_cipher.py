''''
Rey 7910
Turning grille cipher 
Introduction to criptography and security of information
2023-1
'''

from copy import deepcopy

grille = []

grille_time_2 = deepcopy(grille)
grille_time_3 = deepcopy(grille)
grille_time_4 = deepcopy(grille)


def process_message_for_decrypting(message,size):

  while (len(message)< size**2 ):
    message+="X"

  return message

def process_message(message):
  message = message.replace(" ","")
  message = message.upper()
  return message

def print_matrix(matrix,size):
   
   for i in range(size):
     for j in range(size):
       print(matrix[i][j], end=" ")
     print("\n",end="") 


def not_clock_wise_rotation(size):
  for i in range(size):
    for j in range(size):
      grille_time_2[(size-1)-i][(size-1)-j]=grille[(size-1)-j][i]

  for i in range(size):
    for j in range(size):
      grille_time_3[(size-1)-i][(size-1)-j]=grille_time_2[(size-1)-j][i]

  for i in range(size):
    for j in range(size):
      grille_time_4[(size-1)-i][(size-1)-j]=grille_time_3[(size-1)-j][i]


def clock_wise_rotation(size):
  for i in range(size):
    for j in range(size):
      grille_time_2[i][j]=grille[(size-1)-j][i]


  for i in range(size):
    for j in range(size):
      grille_time_3[i][j]=grille_time_2[(size-1)-j][i]


  for i in range(size):
    for j in range(size):
      grille_time_4[i][j]=grille_time_3[(size-1)-j][i]


def encrypte(message,cipher_grille,size):
    message_index = 0
    out = False

    for i in range(size):
      if(out==True):
        break
      for j in range(size):

        if(grille[i][j]==1):
          cipher_grille[i][j]=message[message_index]
          message_index+=1

          if(message_index==len(message)):
            out=True
            break


    for i in range(size):
      if(out==True):
        break
      for j in range(size):

        if(grille_time_2[i][j]==1):
          cipher_grille[i][j]=message[message_index]
          message_index+=1

          if(message_index==len(message)):
            out=True
            break


    for i in range(size):
      if(out==True):
        break
      for j in range(size):

        if(grille_time_3[i][j]==1):
          cipher_grille[i][j]=message[message_index]
          message_index+=1

          if(message_index==len(message)):
            out=True
            break

    for i in range(size):
      if(out==True):
        break
      for j in range(size):

        if(grille_time_4[i][j]==1):
          cipher_grille[i][j]=message[message_index]
          message_index+=1

          if(message_index==len(message)):
            out=True
            break


    for i in range(size):
      for j in range(size):
        if(cipher_grille[i][j]==0):
          cipher_grille[i][j]='X'

    return cipher_grille


def print_encrypted_message(cipher_grille,size):
  print("\n\nYour encrypted message is: ")
  for i in range(size):
      for j in range(size):
        print(cipher_grille[i][j]+" ",end="")



def decrypte(cipher_grille, message, size):
    print("Your decrypted message is: ",end="")

    message_index=0
    for i in range(size):
      for j in range(size):
        cipher_grille[i][j]=message[message_index]
        message_index+=1

    for i in range(size):
      for j in range(size):
        
        if(grille[i][j]==1):
          print(cipher_grille[i][j],end=" ")

    for i in range(size):
      for j in range(size):
        
        if(grille_time_2[i][j]==1):
          print(cipher_grille[i][j],end=" ")


    for i in range(size):
      for j in range(size):
        
        if(grille_time_3[i][j]==1):
          print(cipher_grille[i][j],end=" ")


    for i in range(size):
      for j in range(size):
        
        if(grille_time_4[i][j]==1):
          print(cipher_grille[i][j],end=" ")


# header
print("********\n\nRey 7910\nTurning Grille Cipher \nIntroduction to criptography and security of information\n2023-1\n\n********")
# Parameters that we should top receive

# size of the matrix

size = int(input("Enter the size of the square matrix: "))

# rotation direction cipher

rotation = int(input("Press 1 if you want a clock rotation cipher, if you want a rotation against the clock please enter 0: "))

#  encrypte or decrypte

option= int(input("If you want to encrypte please enter 0, if you want to decrypte please enter 1: "))

# message

message = input("Please enter the message: ")

message = process_message(message)

# We build the grill matrix according tothe first parameter

for i in range(size):
  line = []
  for j in range(size):
    line.append(0)
  grille.append(line)


# We select the paths we are going to use for encryptin
path_number = int(input("Select the number of paths you will use for the cipher: "))

rows=[]
columns=[]

for i in range(path_number):
  path_row = int(input("Select the row of the path "+str(i+1)+": "))
  path_column = int(input("Select the column of the path "+str(i+1)+": "))

  rows.append(path_row)
  columns.append(path_column)

  print("Output: ",path_row, " ", path_column)


grille_time_2 = deepcopy(grille)
grille_time_3 = deepcopy(grille)
grille_time_4 = deepcopy(grille)

cipher_grille = deepcopy(grille)

print("---------")


for i in range(path_number):
  grille[rows[i]][columns[i]]=1


if(rotation == 0):

  not_clock_wise_rotation(size)

elif(rotation == 1):

 clock_wise_rotation(size)
else:
  print("You entered a not valid option of rotation cipher")
  exit()

if(option == 0):

    cipher_grille = encrypte(message,cipher_grille,size)

    print_matrix(cipher_grille,size)


    print("----------")

    print_encrypted_message(cipher_grille,size)

elif(option == 1):
  message = process_message_for_decrypting(message,size)

  decrypte(cipher_grille, message, size)


else:
  print("You entered an invalid option for the message processing")

