
# import operator and pprint classes for later use
import operator
import pprint


#open first test file
file = open("test01b_caesar_shift_ciphertext.txt","r")

# Encryption function

def encrypt_caesar(plaintext):

#set an empty ciphertext string in order to concatenate it with different letters as we go 
    ciphertext = ""
    #iterate thru each letter in the given argument
    for l in plaintext:
        #check to see that the letter is a lowercase alphabetic character
        if (ord(l) >=97) & (ord(l) <=122):
            #check to see if the letter is x, y, or z:
            if (ord(l) >=120):
                #set a new ordinance value that will reflect the letters "wrapped" around to the front of the alphabet
                new_ord = ord(l)-23
                #set letter to the letter with the above specified ord value
                l = chr(new_ord)
                #add this new letter to the ciphertext
                ciphertext +=l
                
            else:
                #shift the ordinance value of the letter to that of the letter to its right by 3
                new_lett = ord(l)+3
                #Set letter to the letter with the above specified ord value
                l = chr(new_lett)
                #add this new letter to the ciphertext
                ciphertext +=l

        else:
            #if the letter is not alpha, then simply just add it to the ciphertext
            ciphertext += l

    #return ciphertext
    return ciphertext

# Decryption function
def decrypt_caesar(ciphertext):

    #Exactly the same as the encrypt function, but everything is being shifted to the left instead
    plaintext = ""
    for l in ciphertext:

        if (ord(l)>=97) & (ord(l) <=122):

            if (ord(l) <= 99):
                new_ord = ord(l)+23
                l = chr(new_ord)
                plaintext += l

            else:
                new_lett = ord(l)-3
                l = chr(new_lett)
                plaintext += l
        #We also account for capital letters for later use
        elif (ord(l) >=65) & (ord(l) <= 90):

            if (ord(l) <=67):
                new_cap = ord(l)+23
                l = chr(new_cap)
                plaintext +=l

            else:
                new_big = ord(l)-3
                l = chr(new_big)
                plaintext +=l

        else:
            plaintext += l

    return plaintext


plaintext_list = [
    "this is a test",
    "caesar’s wife must be above suspicion",
    "as shatner would say: you, should, also, be, able, to, handle, punctuation.",
    "to mimic chris walken: 3, 2, 1, why must you, pause, in strange places?",
]

ciphertext_list = [
    "wklv lv d whvw", 
    "fdhvdu’v zlih pxvw eh deryh vxvslflrq", 
    "dv vkdwqhu zrxog vdb: brx, vkrxog, dovr, eh, deoh, wr, kdqgoh, sxqfwxdwlrq.", 
    "wr plplf fkulv zdonhq: 3, 2, 1, zkb pxvw brx, sdxvh, lq vwudqjh sodfhv?",
]


# Iterate through the lists above and encrypt/decrypt
sampleCount = len(plaintext_list)
for i in range(sampleCount):
    
    # Get the actual plain and cipher texts
    actual_plaintext = plaintext_list[i]
    actual_ciphertext = ciphertext_list[i]
    
    # Compute the encrypted and decrypted forms
    computed_ciphertext = encrypt_caesar(actual_plaintext)
    computed_plaintext = decrypt_caesar(actual_ciphertext)
    
    # Ensure the encrypted version matches what we expect
    assert(computed_ciphertext == actual_ciphertext)
    
    # Ensure the decrypted version matches what we expect
    assert(computed_plaintext == actual_plaintext)

#Decryot the test file
for line in file.readlines():

    line = decrypt_caesar(line)
    print(line)
    
file.close()


# Encryption function

def encrypt_rotation(keyValue, plaintext):

    #set an empty ciphertext string in order to concatenate it with different letters as we go 
    ciphertext = ""
    #iterate thru each letter in the given argument
    for l in plaintext:
        #check to see that the letter is a lowercase alphabetic character
        if (ord(l) >=97) & (ord(l) <=122):
            #check to see if the letter must be wrapped around to the front of the alphabet
            if ((ord(l) + keyValue) > 122):
                #set an int value that will reflect the number of letters to be "wrapped" around to the front of the alphabet
                to_wrap = 26 - keyValue
                #set a new ordinance value that will reflect the letters "wrapped" around to the front of the alphabet
                new_ord = ord(l) - to_wrap
                #Set letter to the letter with the above specified ord value
                l = chr(new_ord)
                #add this new letter to the ciphertext
                ciphertext +=l
                
            else:
                #shift the ordinance value of the letter to that of the letter to its right by keyValue
                new_lett = ord(l)+keyValue
                #Set letter to the letter with the above specified ord value
                l = chr(new_lett)
                #add this new letter to the ciphertext
                ciphertext +=l
        
        #Exactly the same as the lowercase, but accounting for uppercase letters
        elif (ord(l) >=65) & (ord(l) <= 90):

            if ((ord(l) + keyValue) > 90):
                to_wrap = 26-keyValue
                new_ord = ord(l) - to_wrap
                l = chr(new_ord)
                ciphertext +=l

            else:
                new_big = ord(l) + keyValue
                l = chr(new_big)
                ciphertext +=l

        else:
            ciphertext += l
    #Return ciphertext
    return ciphertext

# Decryption function

#Exactly the same as the encrypt function, but everything is being shifted to the left instead
def decrypt_rotation(keyValue, ciphertext):

    plaintext = ""
    
    for l in ciphertext:

        if (ord(l)>=97) & (ord(l) <=122):

            if ((ord(l) + keyValue) < 97):
                to_unwrap = 26 + keyValue
                new_ord = ord(l)+ to_unwrap
                l = chr(new_ord)
                plaintext += l

            else:
                new_lett = ord(l) + keyValue
                l = chr(new_lett)
                plaintext += l

        elif (ord(l) >=65) & (ord(l) <= 90):

            if ((ord(l) + keyValue) < 65):
                new_cap = 26 + keyValue
                new_capOrd = ord(l)+new_cap
                l = chr(new_capOrd)
                plaintext +=l

            else:
                new_big = ord(l) + keyValue
                l = chr(new_big)
                plaintext +=l

        else:
            plaintext += l

    return plaintext

plaintext_list = [
    "to mimic chris walken: 3, 2, 1, why must you, pause, in strange places?",
    "don't take life too seriously. you'll never get out alive",
    ]

rotation_keys = [
    3,
    13,
]

ciphertext_list = [
    "wr plplf fkulv zdonhq: 3, 2, 1, zkb pxvw brx, sdxvh, lq vwudqjh sodfhv?",
    "qba'g gnxr yvsr gbb frevbhfyl. lbh'yy arire trg bhg nyvir"
]

# Iterate through the lists above and encrypt/decrypt
sampleCount = len(plaintext_list)
for i in range(sampleCount):
    
    # Get the actual plain and cipher texts and key
    actual_plaintext = plaintext_list[i]
    rotation_key = rotation_keys[i]
    actual_ciphertext = ciphertext_list[i]
    
    # Compute the encrypted and decrypted forms
    computed_ciphertext = encrypt_rotation(rotation_key, actual_plaintext)
    computed_plaintext = decrypt_rotation(-rotation_key, actual_ciphertext)
    
    # Ensure the encrypted version matches what we expect
    assert(computed_ciphertext == actual_ciphertext)
    
    # Ensure the decrypted version matches what we expect
    assert(computed_plaintext == actual_plaintext)


#Function to return a dictionary with the letters in the text, and how often they appear
def most_common_letters(text):

    #Set an empty dictionary for letter use, and set all letters of the given text to lowercase
    lower_text = text.lower()
    lett_dict = {}

    #Iterate thru each character in the text
    for l in lower_text:
        #Check to see that it is alphabetical
        if (l.isalpha()):
            #Use the count function to store the number of times the letter appears in the text in a variable
            lett_count = lower_text.count(l)
            #add to the dictionary, with the letter as the key and its frequency as the value
            lett_dict[l] = lett_count

    #Using the operator (imported from earlier), sort the dictionary's values in ascending order
    sorted_dict = sorted(lett_dict.items(), key=operator.itemgetter(1))
    #format the dictionary using the pformat function of pprint to make each key-value pair neatly print out on a new linen
    formatted_dict = pprint.pformat(sorted_dict)

    #return the formatted dictionary
    return formatted_dict

    
