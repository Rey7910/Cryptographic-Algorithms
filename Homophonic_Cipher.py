''''
Rey 7910
Hill Cipher 
Introduction to criptography and security of information
2023-1
'''

import random as rand

alfabet_layer = { 'a': [9,12,33,47,53,67,78,92],'b':[48,81],'c':[13,41,62],'d':[1,3,45,79],'e':[14,16,24,44,46,55,57,64,74,82,87,98]
                 , 'f':[10,31],'g':[6,25],'h':[23,39,50,56,65,68],'i':[32,70,73,83,88,93],'j':[15],'k':[4],'l':[26,37,51,84],'m':[22,27],
                 'n':[18,58,59,66,71,91],'o':[0,5,7,54,72,90,99],'p':[38,95],'q':[94],'r':[29,35,40,42,77,80],'s':[11,19,36,76,86,96],'t':[17,20,30,43,49,69,75,85,97],
                 'u':[8,61,63],'v':[34],'w':[60,89],'x':[28],'y':[21,52],'z':[2]}


def cipher_homphonic(plane_text):

  cipher_text = ""
  plane_text= plane_text.replace(' ','')

  for i in plane_text:
    range = rand.randint(0,len(alfabet_layer[i])-1)

    cipher_text= cipher_text + str(alfabet_layer[i][range]) + "  "

  print("Here is the cipher message: ",cipher_text)



def decrypter(cipher_message):
  decrypted_message = ""
  encrypted_blocks = cipher_message.split('  ')

  for i in encrypted_blocks:
    for key in alfabet_layer:
      if int(i) in alfabet_layer[key]:
        
        decrypted_message = decrypted_message + str(key)+ " "
        break

  print(decrypted_message)
    

print("********\n\nRey 7910\nHomophonic Cipher \nIntroduction to criptography and security of information\n2023-1\n\n********")
option = int(input("Press 0 if you want to encrypte, press 1 if you want to decrypte: "))

if(option == 0):

  plane_text = input("Please the message in plane text: ")
  cipher_homphonic(plane_text)

else:
  cipher_message = input(" Please enter the encrypted message: ")
  decrypter(cipher_message)




