# Forensics Binary Challenge - Writeup
## Challenge Overview
- In this forensics challenge, we are tasked with analyzing a file named wanted.msc, which, when executed, doesn't provide any visible output. By inspecting the file contents, we uncover several layers of obfuscation, including Base64 encoded JavaScript and VBScript. Our goal is to reverse engineer the obfuscation and uncover the hidden flag.

## Steps to solve :
### Step 1: Initial Analysis of wanted.msc
- When we executed the wanted.msc file, it yielded no visible output. Upon opening it in a text editor, we discovered large amounts of obfuscated JavaScript code and other data. Our primary focus shifted toward the JavaScript section.

### Step 2: Deobfuscating the JavaScript
- The JavaScript was heavily obfuscated, but after deobfuscating it, we found a string that appeared to be VBScript. By further analyzing the VBScript, we identified a function that handled a specific string. We then proceeded to convert the VBScript function into Python.

### Step 3: Transforming VBScript to Python
- After converting the VBScript function to Python, we executed the script, which revealed a deobfuscated VBScript. 

### Step 4: Downloading Files
-We used curl to download the following files:
    -csrss.exe
    - csrss.exe.config
    - wanted.pdf
    - csrss.dll
### Step 5: XOR Operation
- Next, we XOR each of the downloaded files using csrss.dll as the key. This process involved XORing the contents of each file with the key file.

- After the XOR operation, the PDF file (wanted.pdf) was no longer corrupted and displayed an image of a cowboy. However, there was no hidden data or flag inside the PDF.

### Step 6: Executing the XOR'd Executable
- We then focused on the XOR'd executable csrss.exe. After analyzing it using tools like strings, we found keywords such as "AES", "crypto", and others. This led us to believe that further analysis of the executable was needed.

### Step 7: Reverse Engineering the Executable
- We used dnSpy to decompile the csrss.exe and obtained the real script hidden within it. The script contained a new domain:

- http://windowsupdate.htb/ec285935b46229d40b95438707a7efb2282f2f02.xml
Step 8: Retrieving the Flag
Then using curl, we found the flag:
HTB{mSc_1s_b31n9_s3r10u5ly_4buSed}

# Conclusion
- By deobfuscating the JavaScript, reversing the XOR operation, and analyzing the executable with dnSpy, we were able to uncover the hidden flag. This challenge required a multi-layered approach, involving cryptographic analysis, reverse engineering, and web requests.
- This concludes the writeup for the forensics_binary_Badresources challenge.
- You will find the files found in the challenge attached to understand the writeup better.

