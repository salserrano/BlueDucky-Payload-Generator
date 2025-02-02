# BlueDucky Payload Generator Ver 1.1 beta (Android) 🦆

This is a simple URL payload generator for [pentestfunctions's BlueDucky](https://github.com/pentestfunctions/BlueDucky).

The script will create a "Generated Payloads" folder and output the text file there. Once generated, move the payloads file into the "payloads" folder of BlueDucky.

I included a rickroll payload as example.

*** ***The generated scripts have been tested on a Samsung device. For other Android brands, there is no guarantee that the payload will work.*** ***	

## Discoveries I Made with Samsung Bluetooth Shortcuts:
- I found that the fastest way to open any link is to use Android's built-in Google app. By typing the URL into the Google app search, the Google app automatically opens the URL with the default browser on the device and any supported address of installed apps. This means that with just a URL, an app can be opened, assuming these apps are configured to "open supported links" in their app settings. For example, the YouTube app automatically opens when a YouTube URL is entered.
- For regular browser links that don't pertain to installed apps, I recommend setting Chrome as the default browser for opening these links.

Note:
- The output payload text file itself should work; any issues, such as technical errors, should be reported by opening an issue with the [main BlueDucky repository](https://github.com/pentestfunctions/BlueDucky/issues).
- The commands run fast when executing and work well if the phone is fast enough to opens apps quickly. If the phone is slow and takes too long to open apps, it might miss the chance to type the link.
- Possibly look into writing a more advanced payload beyond URL input in the future.


### Legal Disclaimer

*** ***The BlueDucky Payload Generator (the "Tool") is intended for educational purposes only. By using this Tool, you agree to use it legally and responsibly; the creators do not support any illegal activities, including unauthorized system access or cybercrime. Use of this Tool is at your own risk, and it is provided "as is" without any guarantees. If misused, you may be held responsible, and by using it, you agree to protect the creators from any claims related to your use. If you do not agree with this disclaimer, please refrain from using the Tool.*** ***	
