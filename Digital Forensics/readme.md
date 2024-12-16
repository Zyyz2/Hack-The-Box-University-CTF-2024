# Challenge 1: Frontier Exposed

## Description

The chaos within the Frontier Cluster is relentless, with malicious actors exploiting vulnerabilities to establish footholds across the expanse. During routine surveillance, an open directory vulnerability was identified on a web server, suggesting suspicious activities tied to the Frontier Board. Your mission is to thoroughly investigate the server and determine a strategy to dismantle their infrastructure. Any credentials uncovered during the investigation would prove invaluable in achieving this objective. Spawn the docker and start the investigation!

## Environment Setup

1. **Docker Instance**: 
  To access the Docker instance, click on spawn docker .

## Steps to Solve

### 1. Access the Server

- To access the Docker instance, copy the provided IP address and port into your web browser's URL bar

### 2. Directory Listing

Upon accessing the server, the following files were found in the directory listing:
  - .bash_history
  - .bash_logout
  - .bashrc
  - .profile
  - dirs.txt
  - exploit.sh
  - nmap_scan_results.txt
  - vulmap-linux.py


### 3. Analyze the Files

#### a. `.bash_history`

- Open the `.bash_history` file to check for any commands that may reveal sensitive information.
- Found a base64 encoded string: `SFRCe0MyX2NyM2QzbnQxNGxzXzN4cDBzM2R9`.

#### b. Decoding the Flag

- Decode the base64 string using a command like:

  
  just type in your terminal  : echo "SFRCe0MyX2NyM2QzbnQxNGxzXzN4cDBzM2R9" | base64 --decode or drop it to Cyberchef

-The decoded flag is: HTB{C2_cr3d3nt14ls_3xp0s3d}.


### Notes:
- The added section at the end informs readers that you will provide the files for further exploration or exploitation.
- Feel free to customize the wording or add any additional information as needed!
