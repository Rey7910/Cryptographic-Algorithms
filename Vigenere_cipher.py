''''
Rey 7910
Vigenere Cipher 
Introduction to criptography and security of information
2023-1

'''


from copy import deepcopy


alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
aux_alfabet = alfabet

vigenere_matrix = []
# we are going to generate to generate the Blaise the Vigenere Matrix

def generate_matrix():
  for i in range(26):
    for j in range(1):
    
      vigenere_matrix.append(deepcopy(aux_alfabet))
      move_char = aux_alfabet.pop(0)
      aux_alfabet.append(move_char)


  print("\n\n\nHere you have the vigenere Matrix\n\n")

  for i in range(len(vigenere_matrix)):
    for j in range(len(vigenere_matrix[0])):
      print(vigenere_matrix[i][j], end= " ")

    print("")

  print("\n\n\n")

# encrypte function

def encrypte(message, key):

  encrypted_message = ""
  message = message.replace(" ","")
  key = key.replace(" ","")

  j = 0
  for i in range(len(message)):

    index_message = alfabet.index(message[i])
    index_key = alfabet.index(key[j])

    j+=1
    if(j == len(key)):
      j=0
  
    encrypted_message= encrypted_message + vigenere_matrix[index_message][index_key]

  print("Here is the encrypted message: ",end="")
  for i in range(len(encrypted_message)):
    if i%5==0 and i!=0:
      print(" ",end="")
    print(encrypted_message[i],end="")


def decrypte(message,key):
  decrypted_message = ""
  message = message.replace(" ","")
  key = key.replace(" ","")
  j=0

  for i in range(len(message)):
    index_message = 0
    for y in range(26):
      if( vigenere_matrix[y][alfabet.index(key[j])] == message[i] ):
        index_message = y
        break
    
    decrypted_message+=vigenere_matrix[index_message][0]


    j+=1
    if(j == len(key)):
      j=0
    
  print("Here is the decrypted message: ",end="")
  for i in range(len(decrypted_message)):
    if i%5==0 and i!=0:
      print(" ",end="")
    print(decrypted_message[i],end="")


print("********\n\nRey 7910\nVigenere Cipher \nIntroduction to criptography and security of information\n2023-1\n\n********")
option = int(input("\nWelcome to the vigenere cipher, Press 0 if you want to encrypte a message, if you want to decrypte a message please press 1 (0/1): "))
message = input("Enter the message that you want to encrypte/decrypte, please write it in capital letters: ")
key = input("Please enter the key for the cipher algorithm, write it in capital letters: ")

generate_matrix()

if(option == 0):
  encrypte(message,key)
elif(option == 1):
  decrypte(message,key)
else:
  print("you choosed an incorrect option")
