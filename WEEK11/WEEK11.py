# 05/14/2026  Honour Okhavhe CIS106-001


# PROBLEM 1: Name Parser

def get_name_input():
    """Handles input for Problem 1."""
    return input("\n[Problem 1] Enter a first and last name (e.g., Jane Doe): ")

def format_name(name_string):
    """Parses a first and last name into 'Lastname, F.' format."""
    # .split() automatically handles extra spaces between words
    parts = name_string.strip().split()
    
    # Handle missing parts error validation
    if len(parts) < 2:
        return "Error: Invalid input. Please ensure you enter at least a first and last name."
    
    first_initial = parts[0][0].upper()
    last_name = parts[-1].capitalize() # Takes the last item in case of middle names
    
    return f"{last_name}, {first_initial}."

def display_result(result):
    """Generic output function used across multiple problems."""
    print(f"Output: {result}")


# PROBLEM 2: Clean and Reverse String

def get_raw_text_input():
    """Handles input for Problem 2."""
    return input("\n[Problem 2] Enter a messy line of text with extra spaces: ")

def clean_and_reverse(text):
    """Deletes leading, trailing, and duplicate spaces, then reverses the string."""
    # .split() removes all extra whitespace, ' '.join() puts exactly one space between words
    cleaned_text = ' '.join(text.split())
    
    # [::-1] is Python's slicing trick to reverse a sequence
    reversed_text = cleaned_text[::-1]
    return reversed_text



# PROBLEM 3: CSV Parser

def get_csv_input():
    """Handles input for Problem 3."""
    return input("\n[Problem 3] Enter comma-separated values (e.g., apple, banana, cherry): ")

def parse_csv(csv_string):
    """Parses CSV string, removes extra spaces, and returns a list of items."""
    if not csv_string.strip():
        return []
    
    # Split by comma, then strip spaces from each individual item
    items = csv_string.split(',')
    cleaned_items = [item.strip() for item in items]
    return cleaned_items

def display_list_items(items_list):
    """Outputs a list of items, each on a new line."""
    print("Output:")
    if not items_list:
        print("No items to display.")
    for item in items_list:
        print(item)


# PROBLEM 4: Text Scroller

def get_scroller_inputs():
    """Handles multiple inputs for the scrolling text problem."""
    print("\n[Problem 4] Text Scroller Configuration")
    text = input("Enter a line of text: ")
    
    # Basic validation to ensure integer inputs
    try:
        chars_per_line = int(input("Enter number of characters to print per line: "))
        num_lines = int(input("Enter the number of lines to print: "))
    except ValueError:
        print("Invalid number entered. Defaulting to 20 chars and 5 lines.")
        chars_per_line, num_lines = 20, 5
        
    direction = input("Enter scroll direction ('left' or 'right'): ").strip().lower()
    return text, chars_per_line, num_lines, direction

def generate_scrolling_text(text, chars_per_line, num_lines, direction):
    """Generates the shifting text pattern."""
    if not text:
        return ["Error: Text cannot be empty."]
        
    # Duplicate the text enough times to easily cover the characters per line
    # Adding a space so the text doesn't mash together when repeated
    padded_text = text + " " 
    multiplier = (chars_per_line // len(padded_text)) + 2
    base_string = (padded_text * multiplier)[:chars_per_line]
    
    results = []
    current_string = base_string
    
    for _ in range(num_lines):
        results.append(current_string)
        
        # Shift the string
        if direction == 'left':
            # Take from index 1 to the end, and append the 1st character to the back
            current_string = current_string[1:] + current_string[0]
        elif direction == 'right':
            # Take the last character, and append everything up to the last character
            current_string = current_string[-1] + current_string[:-1]
        else:
            return ["Error: Invalid direction. Must be 'left' or 'right'."]
            
    return results

# MAIN EXECUTION (Testing)

def main():
    """Orchestrates the program to test all components."""
    print("--- Session 11 String Processing ---")
    
    # Test Problem 1
    p1_input = get_name_input()
    p1_processed = format_name(p1_input)
    display_result(p1_processed)
    
    # Test Problem 2
    p2_input = get_raw_text_input()
    p2_processed = clean_and_reverse(p2_input)
    display_result(p2_processed)
    
    # Test Problem 3
    p3_input = get_csv_input()
    p3_processed = parse_csv(p3_input)
    display_list_items(p3_processed)
    
    # Test Problem 4
    text, chars, lines, direction = get_scroller_inputs()
    p4_processed = generate_scrolling_text(text, chars, lines, direction)
    display_list_items(p4_processed)

# This ensures the code only runs if executed directly (standard Python practice)
if __name__ == "__main__":
    main()

