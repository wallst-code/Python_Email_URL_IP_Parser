from dataclasses import replace
import re
import email


class EmailParser:
    def __init__(self, inputFile):
        self.inputFile = inputFile              
              
    def processEmailFile(self):
        url_regex = r'(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
        ip_regex = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
            
        # Open the .eml file
        with open(inputFile, 'rb') as file:
            message = email.message_from_bytes(file.read())

        # Convert bytes to text
        toText = str(message)

        # Uses the email file name and adds .txt and writes to a txt file.
        with open(f'{inputFile}.txt', 'w' ) as file:
            file.write(toText)

        # Opens the txt file and searches for URLs and IP Addresses, and then writes to the "output.txt" file.
        with open(f'{inputFile}.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
            text = input_file.read()

        # Find all URLs and IP addresses in the text
            urls = re.findall(url_regex, text)
            ips = re.findall(ip_regex, text)

            output_file.write('URLs:\n')
            output_file.write('\n'.join(urls))
            output_file.write('\n\nIP addresses:\n')
            output_file.write('\n'.join(ips))                      

            # Print the URLs and IP addresses to the console.
            print('URLs:')
            print('\n'.join(urls))
            print('\n\nIP addresses:')
            print('\n'.join(ips))        
                
    

class DefangURL_IPs:
    def __init__(self, input):   
        self.input = input
            
    # Open input and output files
    def defangFile(self):
       
        # Define regular expression for matching URLs and IP addresses
        regex = r'\.'
        replacement = r'[.]'
        input_file = self.input
        output_file = 'defanged_output.txt'

        with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
           
            defanged_output = []
          
            for line in input_file:
               defanged_line = line.replace('.', '[.]')
               defanged_output.append(defanged_line)
              
            for line in defanged_output:
                output_file.writelines(line)



if __name__ == "__main__":
           
    # File must be in an .eml format.
    inputFile = "your_email_file.eml"


    parse = EmailParser(inputFile)  
    parse.processEmailFile()

    # Leave all of this alone.
    defangInput = "output.txt"
    defang = DefangURL_IPs(defangInput)  
    defang.defangFile()
   
