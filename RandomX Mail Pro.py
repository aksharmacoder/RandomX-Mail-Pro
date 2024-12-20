#RandomX Email Pro
import random
import string

# Function to generate random names based on Indian states
def generate_random_name(state):
    names = {
        'Punjabi': ['Amrit', 'Harpreet', 'Jaspreet'],
        'Gujarati': ['Aarav', 'Vivaan', 'Anaya'],
        'Rajasthani': ['Raj', 'Kiran', 'Suman'],
        'Assamese': ['Rohit', 'Priya', 'Nirmal'],
        'Bengali': ['Sourav', 'Maya', 'Deb'],
        'Manipuri': ['Biren', 'Chitra', 'Ningthou'],
        'Haryanvi': ['Rajesh', 'Sunita', 'Vikram']
    }
    return random.choice(names.get(state, ['John', 'Doe']))

# Function to generate a random email address
def generate_random_email(first_name, middle_name, last_name, provider, domain):
    username = f"{first_name}{middle_name}{last_name}{random.randint(1000, 9999)}"
    return f"{username}@{provider}{domain}"

# Main function to run the app
def main():
    print("Welcome to RandomX Mail Pro!")

    
    # User inputs for names
    
    first_name = input("Enter First Name (letters and numbers only): ")
    middle_name = input("Enter Middle Name (optional, letters and numbers only): ")
    last_name = input("Enter Last Name (letters and numbers only): ")
    
    
    # User selects email provider
    print("Choose an email provider:")
    providers = ['gmail.com', 'yahoo.com', 'outlook.com']
    custom_provider = input("Enter custom provider (or press Enter to skip): ")
    
    if custom_provider:
        providers.append(custom_provider)
    
    provider = random.choice(providers)

    # User selects domain ending
    print("Choose a domain ending:")
    domains = ['.com', '.in', '.us', '.gov', '.uk', '.shop']
    custom_domain = input("Enter custom domain ending (or press Enter to skip): ")
    
    if custom_domain:
        domains.append(custom_domain)
    
    domain = random.choice(domains)

    # Optional: User can choose a state for name generation
    state_choice = input("Choose a state for names (Punjabi, Gujarati, Rajasthani, Assamese, Bengali, Manipuri, Haryanvi): ")
    
    if state_choice in ['Punjabi', 'Gujarati', 'Rajasthani', 'Assamese', 'Bengali', 'Manipuri', 'Haryanvi']:
        first_name = generate_random_name(state_choice)

    # Generate the random email
    random_email = generate_random_email(first_name, middle_name, last_name, provider, domain)
    
    print(f"Generated Random Email: {random_email}")

if __name__ == "__main__":
    main()
