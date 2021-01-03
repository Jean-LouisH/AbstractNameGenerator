import random

def command_print(name_output_list, tokens):
        quantity = 0
        if len(tokens) >= 2 and len(tokens) <= 3:
                if tokens[1] == "all":
                        quantity = len(name_output_list)
                else:
                        try:
                                quantity = int(tokens[1])
                                if quantity < 1:
                                        print("The number given is not more than 0")
                                elif quantity > len(name_output_list):
                                        quantity = len(name_output_list)
                        except:
                                print("The value '" + tokens[1] + "' is not a valid quantifier")

                if quantity > 0:
                        if len(tokens) == 2:
                                print(" ")
                                for i in range(0, quantity, 1):
                                        print("\t" + name_output_list[i])
                        elif len(tokens) == 3:
                                if tokens[2] == "shuffled":
                                        shuffled_names = name_output_list
                                        random.shuffle(shuffled_names)
                                        print(" ")
                                        for i in range(0, quantity, 1):
                                                print("\t" + shuffled_names[i])
                                else:
                                        print("'" + tokens[2] + "' is not a valid parameter")

def command_syllables(tokens):
        if len(tokens) == 2:
                try:
                        quantity = int(tokens[1])
                        if quantity >= 1:
                                return quantity
                        else:
                                print("The number given is not more than 0")
                except:
                        print("The parameter '" + tokens[1] + "' is not an integer")
        else:
                print("This command has too many parameters")

def command_commands():
        print("\nMenu commands;\n\n" + get_supported_commands())
        print("\nCommand examples;\n\n" + get_command_examples())
        print("\nNote: 1 to 4 syllables is recommended, anymore will take several minutes or more to process. The default at startup is 3.")

def convert_to_name(syllable_list, syllable_index_list):
        name_output = ""
        
        for i in syllable_index_list:
                name_output += syllable_list[i]

        return name_output

def are_all_indices_last(syllabary_count, syllable_index_list):
        return all(index == syllabary_count - 1 for index in syllable_index_list)

def create_name_output_list(syllable_list, syllable_index_list):
        syllable_count = len(syllable_index_list)
        syllabary_count = len(syllable_list)
        name_output_list = []
        
        while not are_all_indices_last(syllabary_count, syllable_index_list):
                name_output_list.append(convert_to_name(syllable_list, syllable_index_list))
                syllable_index_list[syllable_count - 1] += 1
                
                for i in range(syllable_count - 1, -1, -1):
                        if syllable_index_list[i] > syllabary_count - 1 and i - 1 >= 0:
                                syllable_index_list[i] = 0
                                syllable_index_list[i - 1] += 1

        name_output_list.append(convert_to_name(syllable_list, syllable_index_list))
        
        return name_output_list

def get_command_examples():
        return "'syllables 4' \n'print 5' \n'print 3 shuffled' \n'print all'"

def get_supported_commands():
        return "'exit' \n'commands' \n'syllables <quantity>' \n'print <quantity> (shuffled)'"

def create_syllable_index_list(syllables_count):
        syllable_index_list = []
        
        for i in range(syllables_count):
                syllable_index_list.append(0)

        return syllable_index_list

def create_syllable_list():
        syllable_list = []
        consonant_letters = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        consonants = consonant_letters
        vowels = ["a", "i", "u", "e", "o"]
        
        for consonant in consonants:
                for vowel in vowels:
                        syllable_list.append(consonant + vowel)

        for vowel in vowels:
                syllable_list.append(vowel)

        return syllable_list

def main():
        syllable_list = create_syllable_list()
        print("\t\tAbstract Name Generator")
        syllables_count = 3
        syllable_index_list = create_syllable_index_list(syllables_count)
        name_output_list = create_name_output_list(syllable_list, syllable_index_list)
        command_commands()

        menu_input = ""
        is_exiting = False
        while not is_exiting:
                
                menu_input = input("\nEnter a command: ")
                tokens = menu_input.split(" ")
                command = tokens[0]
                
                if command == "syllables":
                        syllables_count = command_syllables(tokens)
                        syllable_index_list = create_syllable_index_list(syllables_count)
                        name_output_list = create_name_output_list(syllable_list, syllable_index_list)
                elif command == "print":
                        command_print(name_output_list, tokens)
                elif command == "exit":
                        is_exiting = True
                elif command == "commands":
                        command_commands()
                else:
                        print("'" + tokens[0] + "' is not a valid command")
	
if __name__ == "__main__":
        main()
