#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open ("./Input/Names/invited_names.txt", "r") as names:
    name_list = names.readlines()

txt = "[name]"

with open ("./Input/Letters/starting_letter.txt", "r") as letters:
    template_letter = letters.read()

for name in name_list:
    new_letter = template_letter.replace(txt, name.strip())

    output_file_path = f"./Output/ReadyToSend/letter_for_{name.lower().strip()}.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(new_letter)