/*
Caesar Cipher
Rey 7910
Introduction to cryptography and security of information 
2023-1

*/

#include <iostream>
#include <cstring>

using namespace std;

char alfabet[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};           // We define our alfabet with a string data structure


void encrypter(int k, string message){
    
    cout<<"\n\nYour encrypted message is: ";
    
    int cipher_letter_index=0;
    
    
    for(int i=0;i<message.length();i++){
       
        for(int j = 0; j<27; j++){
            if(message[i]==alfabet[j]){
               
               cipher_letter_index = j+k;
               
               cipher_letter_index = cipher_letter_index%26;
               
               cout<<alfabet[cipher_letter_index]<<" ";
               
            }
        }
    }
}



void decrypter(int k, string message){
    
    cout<<"\n\nYour decrypted message is: ";
    
    int letter_index=0;
    
    
    for(int i=0;i<message.length();i++){
       
        for(int j = 0; j<27; j++){
            if(message[i]==alfabet[j]){
               
               letter_index = j-k;
               
               letter_index = letter_index%26;
               
               if(letter_index<0){
               	 while(letter_index<0){
               	 	letter_index=letter_index+26;
		  }
	  	}
               
               cout<<alfabet[letter_index]<<" ";
               
            }
        }
    }
}



int main() {
   
    int k = 0;
    
    string message;
    
    int option=0;
    
    
    
    cout<<"Welcome to the Caesar cipher "<<endl;
    cout<<"By Rey 7910 for the cryptography course at Universidad Nacional de Colombia\n"<<endl; 
    
    
    
    
   
   
    cout<<"Enter the message that you want to encrypt or decrypt with Caesar Algorithm: ";
    
    getline(cin,message);
    
    cout<<"Enter the encryption offset constant: ";
   
    cin>>k;
    
    
    cout<<"Please enter 0 if you want to encrypt a message, if you want to want to decrypt a message please enter 1: ";
    
    cin>>option;
    
    
    if(option!=0 and option!=1){
        cout<<"That was not a valid option"<<endl;
    }
    
    
    if(option==0){
        
        encrypter(k, message);
        
    }else if(option==1){
        
        decrypter(k, message);
        
    }
    
    
    
    
}
