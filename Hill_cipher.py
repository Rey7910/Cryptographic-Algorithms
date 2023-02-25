''''
Rey 7910
Hill Cipher 
Introduction to criptography and security of information
2023-1
'''

alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

encrypted_message=""

def decrypt(message, matrix):
    decrypted_message = ""

    det = find_det(matrix)
    inv_det = 0
    for i in range(1, 26):
        if (det * i) % 26 == 1:
            inv_det = i
            break

    inv_matrix = [[0, 0], [0, 0]]
    inv_matrix[0][0] = (matrix[1][1] * inv_det) % 26
    inv_matrix[1][1] = (matrix[0][0] * inv_det) % 26
    inv_matrix[0][1] = (-matrix[0][1] * inv_det) % 26
    inv_matrix[1][0] = (-matrix[1][0] * inv_det) % 26

    for i in range(0, len(message), 2):
        vector = [[alfabet.index(message[i])], [alfabet.index(message[i+1])]]
        decrypted_vector = mul_matrix2x2(inv_matrix, vector)

        decrypted_message += decrypted_vector[0][0] + decrypted_vector[1][0]+" "

    return decrypted_message

def mul_matrix2x2(matrix,vector):
  encrypted_message=""

  final_vector =[[0],[0]]

  final_vector[0][0] = (matrix[0][0]*vector[0][0])+(matrix[0][1]*vector[1][0])
  final_vector[1][0] = (matrix[1][0]*vector[0][0])+(matrix[1][1]*vector[1][0])

  if(final_vector[0][0]>25):
    final_vector[0][0]=final_vector[0][0]%26
  
  elif(final_vector[0][0]<0):
    while(final_vector[0][0]<0):
      final_vector[0][0]+=26
  
  if(final_vector[1][0]>25):
    final_vector[1][0]=final_vector[1][0]%26
  elif(final_vector[1][0]<0):
    while(final_vector[1][0]<0):
      final_vector[1][0]+=26

  encrypted_message+=alfabet[final_vector[0][0]]+alfabet[final_vector[1][0]]+" "
  return encrypted_message

def process_message(message):
  
  message = message.replace(" ","")
  
  if(len(message)%2!=0):
    message+="X"
  
  return message


def find_det(matrix):
  # a11 * a22 - a12*a21
  return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])

def print_matrix(matrix):

  print("\nHere is the key matrix: \n")

  for i in range(2):
    for j in range(2):
      print(matrix[i][j],end=" ")
    print()

def mcd(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a

def encrypte(message,encrypted_message):
  encrypted_message=""
  for i in range(0,len(message),2):
    vector = [[alfabet.index(message[i])],[alfabet.index(message[i+1])]]
    encrypted_message+=mul_matrix2x2(matrix,vector)
  
  print("\nThe encrypted message is: ",encrypted_message)




matrix = [['0','0'],['0','0']]
print("********\n\nRey 7910\nHill Cipher \nIntroduction to criptography and security of information\n2023-1\n\n********")

option = int(input("Welcome to the hill cipher, please press 0 to encrypte a message, if you want to decrypte a message please press 1 (0/1): "))

message = input("Enter the message you want to encrypte/decrypte: ")

message = process_message(message)

col1_row1 = int(input("Enter the value of row 1 column 1 for the matrix key: "))
col2_row1 = int(input("Enter the value of row 1 column 2 for the matrix key: "))

col1_row2 = int(input("Enter the value of row 2 column 1 for the matrix key: "))
col2_row2 = int(input("Enter the value of row 2 column 2 for the matrix key: "))


matrix[0][0] = col1_row1
matrix[0][1] = col2_row1
matrix[1][0] = col1_row2
matrix[1][1] = col2_row2

print_matrix(matrix)
print("\nThe determinant of the matrix is: ",find_det(matrix),end="\n")
vector = [[12],[0]]
mul_matrix2x2(matrix,vector)

if(mcd(find_det(matrix),26)==1 and find_det(matrix)!=0):

  if(option == 0):
    encrypte(message,encrypted_message)

  elif(option == 1):
    message = process_message(message)
    
    print("The decrypted message is: ",decrypt(message,matrix))


else:
  print("The key is not approved, determinant of the matrix must be diffetent of cero and it must be co-prime of 26")



