# Challenge 1: Frontier Exposed

## Description

A routine patrol through the Frontier Cluster's shadowy corners uncovered a sinister file embedded in a bounty report—one targeting Jack Colt himself. The file’s obfuscated layers suggest it's more than a simple message; it’s a weaponized codNote: Ensure all domains discovered in the challenge resolve to your Docker instance, including the appropriate port when accessing URLs.e from the Frontier Board, aiming to tighten their grip on the stars. As a trusted ally, it's your task to peel back the layers of deception trace its origin, and turn their tools against them. Every domain found in the challenge should resolve to your docker instance. Do not forget to add the port when visiting the URLs.

## Environment Setup

1. **Docker Instance**: 
  To access the Docker instance, click on spawn docker .

## Steps to Solve
In this forensics challenge, we are tasked with analyzing a potentially malicious `.hta` (HTML Application) file. The goal is to investigate the contents of the file, decode obfuscated data, and trace the malicious actions it attempts to perform.

### Step 1: Inspect the `.HTA` File
We start by opening the `.hta` file to examine its contents. Running the following command in the terminal reveals a long URL-encoded string:
cat wanted.hta

### Step 2: Decode the URL-Encoded Data
The file contains URL-encoded data that is not immediately readable. Using CyberChef, we decode the string multiple times (5 times) to uncover its contents. After decoding, we find a <script> tag containing JavaScript code with embedded malicious code.

### Step 3: Analyze the JavaScript Code
Inside the decoded <script> tag, we identify nested JavaScript and VBScript. The VBScript is a key component of the attack and is designed to execute a PowerShell command silently. Here's what the VBScript does:

Obfuscated VBScript: The script constructs a PowerShell command using obfuscated variable names. It utilizes WScript.Shell to run a PowerShell command that bypasses execution policies, disables profiles, and runs the script in hidden mode.

PowerShell Command: The PowerShell command decodes a Base64-encoded payload and executes it using Invoke-Expression (iex). This payload is likely used to download and execute additional malicious instructions.
The obfuscation techniques used in the VBScript help to evade detection and make analysis harder.

### Step 4: Decode the Base64 Payload
The Base64-encoded payload is decoded to reveal a PowerShell script. This script imports a function from a DLL (uRLmON.dll) and uses it to download a malicious .vbs file from a remote server (http://wanted.alive.htb/35/wanted.tIF). The file is saved to the user's APPDATA directory and executed after a brief pause.

After decoding the Base64 payload, we can see the PowerShell script that downloads the file:
URL: http://wanted.alive.htb/35/wanted.tIF
- Download Location: The file is saved in the user's APPDATA directory.
- Execution: The downloaded .vbs file is executed after a 3-second pause to ensure the download completes.

### Step 5: Execute the Downloaded VBS Script
To execute the downloaded .vbs script, we need to modify the system’s etc/hosts file to associate the malicious domain with the Docker IP. Just type in your terminal 'sudo nano /etc/hosts' after that add the domain associated with the given ip .
After this, we use curl to fetch the .vbs file from the provided URL : curl http://wanted.alive.htb:port/35/wanted.tIF
This retrieves the malicious .vbs file, which we then analyze.

### Step 6: Deconstruct the VBS Script
Upon inspecting the downloaded .vbs file, we find multiple Base64-encoded strings. These strings, when decoded, reveal executable commands and system-level actions. The script is designed to run these commands in the background, avoiding detection. Here's a breakdown of the script's components:

- Base64 Decoding: The script uses Base64 encoding to hide its commands. After decoding, we observe:
- Command Construction: The decoded strings are concatenated to form a command line, which is then executed using incentiva.Run.
- Obfuscation: Various techniques are used to obfuscate the real actions of the script. This helps evade analysis and detection by antivirus tools.
- Background Execution: The incentiva.Run command runs the constructed command in the background, ensuring no user interaction is required and avoiding detection.

### Step 7: Decode Additional Payloads
Inside the VBS script, we spot a suspicious Base64-encoded string (latifoliado).When we try to decode it we get nothing but we notice there is a repetitive string 'd2FudGVkCg' After cleaning up the repetitive sections, we decode it to reveal another PowerShell script. This new PowerShell script does the following:

- Disables Security: The script bypasses SSL validation and sets the execution policy to Bypass, which allows further execution of potentially harmful code.
- Downloads Another Payload: The script downloads a Base64-encoded string from a URL (http://wanted.alive.htb/cdba/_rp) and decodes it into a PowerShell script. This script is then executed using Invoke-Expression (iex).
The use of Base64 encoding and obfuscation techniques ensures that each payload is hidden and not easily detected by standard security tools.

### Step 8: Retrieve the Flag
After performing all necessary steps and decoding the final payload, we use curl to fetch the last script : curl http://wanted.alive.htb:port/cdba/_rp
and then we get the flag : HTB{c4tch3d_th3_m4lw4r3_w1th_th3_l4ss0_9829c8ef2650507eed3f7a63361074ae}

## Conclusion
Through this forensics analysis, we successfully traced a multi-layered malware attack hidden within an .hta file. The process involved decoding multiple layers of obfuscated data, identifying malicious PowerShell and VBScript payloads, and eventually extracting the flag. This case highlights the importance of careful file inspection and decoding techniques to uncover hidden malicious behavior.

Tools Used :
CyberChef: For URL and Base64 decoding.
Curl: For fetching URLs associated with the malware payloads.
Text Editors: To inspect and analyze the contents of the files.
Linux Terminal: To interact with the system and manipulate files.
 
The final flag extracted from the malware analysis :
HTB{c4tch3d_th3_m4lw4r3_w1th_th3_l4ss0_9829c8ef2650507eed3f7a63361074ae}

