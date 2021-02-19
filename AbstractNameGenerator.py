import random

RANDOM_SYLLABLE_COUNT = -1

def print_names(quantity, syllables_count, min_syllables_count, max_syllables_count, is_spacings_enabled):
        
        # The following consonants were removed; 'c' for 'k' or 's'; 'q' for 'k'
        # Other consonant sounds that are not suited for both beginning and ending are also removed
        
        consonant_sounds = ["b", "d", "f", "g", "j", "k", "l", "m", "n", "p", "r", "s", "t",
                            "v", "w", "y", "z", "ch", "sk", "sh", "sp", "st", "th"]
        beginning_only_consonant_sounds = ["h", "bl", "br", "dr", "dw", "fl", "fr", "gl", "gr", "kl", "kr", "kw", 
                            "pl", "pr", "tr", "tw", "vr", "sm"]
        end_only_consonant_sounds = ["x", "ft", "kt", "lt", "mp", "ng", "nk", "np",
                            "nt", "rk", "rl", "rm", "rn", "rp", "rt", "rv"]
        vowel_sounds = ["ay", "ee", "eye", "oh", "oo", "aa", "eh", "ih", "ah", "uh"]

        beginning_consonant_sounds = consonant_sounds + beginning_only_consonant_sounds
        end_consonant_sounds = consonant_sounds + end_only_consonant_sounds
        
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

                        if is_spacings_enabled:
                                if syllable != 0:
                                        name += " + "
                        
                        for j in range(0, consonant_beginning_count, 1):
                                index = random.randint(0, len(beginning_consonant_sounds) - 1)
                                name += beginning_consonant_sounds[index]
                                if is_spacings_enabled:
                                        name += "-"

                        #Every syllable has 1 vowel
                        index = random.randint(0, len(vowel_sounds) - 1)
                        name += vowel_sounds[index]

                        #Every syllable has 0 to 1 ending consonants
                        consonant_end_count = random.randint(0, 1)

                        for j in range(0, consonant_end_count, 1):
                                if is_spacings_enabled:
                                        name += "-"
                                index = random.randint(0, len(end_consonant_sounds) - 1)
                                name += end_consonant_sounds[index]
                                
                print("\t" + name)
                
                        
def command_print(tokens, syllables_count, min_syllables_count, max_syllables_count, is_spacings_enabled):
        quantity = 0
        
        if len(tokens) == 2:
                try:
                        quantity = int(tokens[1])
                        if quantity < 1:
                                print("The number given is not more than 0")
                except:
                        print("The value '" + tokens[1] + "' is not a valid quantifier")

                if quantity >= 1:
                        print_names(quantity, syllables_count, min_syllables_count, max_syllables_count, is_spacings_enabled)
        else:
                print("This command has too many parameters")

def validate_on_off_command(tokens):
        if len(tokens) == 2:
                if tokens[1] == "on":
                        return True
                elif tokens[1] == "off":
                        return False
                else:
                        print("The value '" + tokens[1] + "' is not valid")
        else:
                print("This command has too many parameters")

def command_spacings(tokens):        
        return validate_on_off_command(tokens)

        
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

        return min_max_syllables


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
        return "'syllables 4' \n'syllables random' \n'min_max_syllables 2 3' \n'spacings off' \n'print 5'"

def get_supported_commands():
        return "'exit' \n'commands' \n'syllables <quantity/'random'>' \n'min_max_syllables <min> <max>'" \
               "\n'spacings <'on'/'off'>' \n'print <quantity>'"

def command_commands():
        print("\nMenu commands;\n\n" + get_supported_commands())
        print("\nCommand examples;\n\n" + get_command_examples())
        print("\nNote: The default syllable count is random.")

def main():
        syllables_count = RANDOM_SYLLABLE_COUNT
        min_syllables_count = 2
        max_syllables_count = 3
        is_spacings_enabled = True

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
                elif command == "spacings":
                        is_spacings_enabled = command_spacings(tokens)
                elif command == "print":
                        command_print(tokens, syllables_count, min_syllables_count, max_syllables_count, is_spacings_enabled)
                elif command == "exit":
                        is_exiting = True
                elif command == "commands":
                        command_commands()
                else:
                        print("'" + tokens[0] + "' is not a valid command")
	
if __name__ == "__main__":
        main()
