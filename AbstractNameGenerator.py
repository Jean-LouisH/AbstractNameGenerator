import random

RANDOM_SYLLABLE_COUNT = -1

def print_names(quantity, syllables_count, min_syllables_count, max_syllables_count):
        
        # The following consonants were removed; 'c' for 'k' or 's'; 'q' for 'k'
        # Other consonant sounds that are not suited for both beginning and ending are also removed
        
        consonant_sounds = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t",
                            "v", "w", "y", "z", "ch", "sk", "sh", "sm", "sp", "st", "th"]
        beginning_only_consonant_sounds = []
        end_only_consonant_sounds = []
        vowel_sounds = ["ay", "ee", "eye", "oh", "oo", "aa", "eh", "ih", "ah", "uh", "aw"]
        
        print(" ")
        for current_name_count in range(0, quantity, 1):
                name = ""
                
                if syllables_count == RANDOM_SYLLABLE_COUNT:
                        syllables_loop_count = random.randint(min_syllables_count, max_syllables_count)
                else:
                        syllables_loop_count = syllables_count
                        
                for syllable in range (0, syllables_loop_count, 1):

                        #Every syllable has 0 or 1 beginning consonants
                        consonant_beginning_count = random.randint(0, 1)
                        
                        for j in range(0, consonant_beginning_count, 1):
                                consonant_index = random.randint(0, len(consonant_sounds) - 1)
                                name += consonant_sounds[consonant_index]
                                if j == consonant_beginning_count - 1:
                                        name += "-"

                        #Every syllable has 1 vowel
                        vowel_index = random.randint(0, len(vowel_sounds) - 1)
                        name += vowel_sounds[vowel_index]

                        #Every syllable has 0 to 2 ending consonants
                        consonant_end_count = random.randint(0, 2)
                        for j in range(0, consonant_end_count, 1):
                                if j == 0:
                                        name += "-"
                                consonant_index = random.randint(0, len(consonant_sounds) - 1)
                                name += consonant_sounds[consonant_index]

                        if syllable != syllables_loop_count - 1:
                                name += "-"
                                
                print("\t" + name)
                
                        
def command_print(tokens, syllables_count, min_syllables_count, max_syllables_count):
        quantity = 0
        
        if len(tokens) == 2:
                try:
                        quantity = int(tokens[1])
                        if quantity < 1:
                                print("The number given is not more than 0")
                except:
                        print("The value '" + tokens[1] + "' is not a valid quantifier")

                if quantity >= 1:
                        print_names(quantity, syllables_count, min_syllables_count, max_syllables_count)
        else:
                print("This command has too many parameters")

def command_min_max_syllables(tokens):
        min_max_syllables = [1, 2]
        
        if len(tokens) == 3:
                for i in range(0, 2, 1):
                        quantity = int(tokens[i + 1])
                        if quantity >= 1:
                                min_max_syllables[i] = quantity
                        else:
                                print("The number given is not more than 0")
                                min_max_syllables[i] = 1

                if min_max_syllables[0] >=  min_max_syllables[1]:
                        min_max_syllables[1] = min_max_syllables[0] + 1

                return min_max_syllables
        else:
                print("This command has too many or too little parameters")


def command_syllables(tokens):
        if len(tokens) == 2:
                if tokens[1] == "random":
                        return RANDOM_SYLLABLE_COUNT
                else:
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

def get_command_examples():
        return "'syllables 4' \n'syllables random' \n'min_max_syllables 2 3' \n'print 5'"

def get_supported_commands():
        return "'exit' \n'commands' \n'syllables <quantity>' \n'print <quantity>'"

def command_commands():
        print("\nMenu commands;\n\n" + get_supported_commands())
        print("\nCommand examples;\n\n" + get_command_examples())
        print("\nNote: The default syllable count is random.")

def main():
        syllables_count = RANDOM_SYLLABLE_COUNT
        min_syllables_count = 1
        max_syllables_count = 4

        print("\t\tAbstract Name Generator")
        command_commands()

        menu_input = ""
        is_exiting = False
        while not is_exiting:
                
                menu_input = input("\nEnter a command: ")
                tokens = menu_input.split(" ")
                command = tokens[0]
                
                if command == "syllables":
                        syllables_count = command_syllables(tokens)
                elif command == "min_max_syllables":
                        min_max_syllables = command_min_max_syllables(tokens)
                        min_syllables = min_max_syllables[0]
                        max_syllables = min_max_syllables[1]
                elif command == "print":
                        command_print(tokens, syllables_count, min_syllables_count, max_syllables_count)
                elif command == "exit":
                        is_exiting = True
                elif command == "commands":
                        command_commands()
                else:
                        print("'" + tokens[0] + "' is not a valid command")
	
if __name__ == "__main__":
        main()
