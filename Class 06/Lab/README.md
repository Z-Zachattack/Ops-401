<h2>**Lab: Data File Encryption and Hashing**</h2>


<h3>**Overview**</h3>


Encryption plays a vital role in the securing of data on computer systems, and can serve many purposes. Sometimes, encryption is used for good: Keeping confidential data out of the hands of criminals. Other times, encryption is used for more nefarious deeds, such as locking files with ransomware. If the organization needs to protect sensitive information, the security professional should be prepared with solutions to facilitate the confidentiality and integrity of a given data both at rest and in motion.

<h3>**Objectives**</h3>




* Host a SFTP server in AWS and securely share a file with a classmate
* Use SCP via terminal to copy a file from your local PC to the AWS instance
* Dump that hash of your Linux instance’s user credentials

<h3>**Resources**</h3>




* [Linux SFTP Command](https://www.computerhope.com/unix/sftp.htm)
* [How to set up an SFTP server on Linux](https://www.techrepublic.com/article/how-to-set-up-an-sftp-server-on-linux/)
* [SSH public key authentication on AWS EC2](https://repost.aws/knowledge-center/new-user-accounts-linux-instance)
* [How to Use Linux SCP Command](https://linuxhint.com/linux_scp_command/)
* [How to Un-shadow the file and dump Linux password Beginner’s Guide](https://www.cyberpratibha.com/unshadow-the-file-and-dump-linux-password/)
* [How to Crack Passwords with John the Ripper](https://medium.com/@sc015020/how-to-crack-passwords-with-john-the-ripper-fdb98449ff1)

<h3>**Tasks**</h3>


<h4>**Part 1: Staging**</h4>


Prepare the following operating systems for today’s lab:



1. Deploy a Linux EC2 instance in AWS. A recent version of Ubuntu works fine for this.
    1. **Note**: Make sure your EC2 instance is assigned a public IP address, otherwise you won’t be able to complete this lab.
2. In your Linux VM, install OpenSSH.
![alt_text](images/image1.png "image_tooltip")


<h4>**Part 2: Secure File Transmission with SCP and SFTP on Linux**</h4>




1. Deploy a SFTP server on your cloud Linux instance, carefully following these instructions: [How to set up an SFTP server on Linux](https://www.techrepublic.com/article/how-to-set-up-an-sftp-server-on-linux/)
2. Successfully perform a file upload and download from your local computer to your Linux cloud VM using the **<code>scp</code></strong> command.
    1. Upload some cybersecurity meme images to the sftp directory to share with your classmate.

<h4><strong>Part 3: SSH public key authentication on Linux</strong></h4>


On your Linux VM in the cloud:



1. Install OpenSSH.
2. Ask a classmate to authenticate into your server using SSH keys. **Steps:**
    1. Your classmate needs to generate a pair of SSH keys if they do not have one already.
    2. Ask your classmate to provide you with their **public key**.
    3. Connect to the instance using your existing private key (**<code>.pem</code></strong> key).


![alt_text](images/image2.png "image_tooltip")




    4. Navigate to the **<code>home</code></strong> directory of the user you created in Part 2. Example: <strong><code>/home/USERNAME</code></strong>.
    5. Using a text editor of your choice, open the <strong><code>.ssh/authorized_keys</code></strong> file on the instance. Paste the public key your classmate provided underneath the existing public key information. Save the file.


![alt_text](images/image3.png "image_tooltip")




    6. If the **<code>.ssh/authorized_keys</code></strong> file does not exist, create both the <strong><code>.ssh</code></strong> directory and the <strong><code>authorized_keys</code></strong> (no file extension) file.
    7. Disconnect from your instance, and test that your classmate can connect to your instance using their private key.
    8. Confirm that they have SFTP access, by having them prove they can download an image from your SFTP server.

<strong>Here I connect through sftp and pull the from awstopc.txt file. This is the file I made in the AWS instance</strong>


![alt_text](images/image4.png "image_tooltip")


**Since my partner gave up for the night, I used one of my home VMs to prove sftp works.**



    9. Confirm that they do NOT have full SSH shell access.


![alt_text](images/image5.png "image_tooltip")

![alt_text](images/image6.png "image_tooltip")


**I am a little confused by this bullet, but as you can see, there is a limited scope of commands available**



    10. Document your setup and file transmission process and confirmations with screenshots and descriptions.

<h4>**Part 4: Encryption and Decryption on Linux**</h4>


Let’s take a look at where Linux stores user credentials.


![alt_text](images/image7.png "image_tooltip")




1. As the administrator of the Ubuntu Linux VM, dump the password hash file or strings.


![alt_text](images/image8.png "image_tooltip")




2. Document your setup and process with screenshots and descriptions.


![alt_text](images/image9.png "image_tooltip")


**Ok, so I was able to pull the passwd file, but not shadow nor shadow- (at least not through sftp)**

**That said, what are you wanting here? We haven’t really touched password dumping yet, and it seems like a big ask to mimikatz or use john the ripper as it is a stretch goal? Anyways, I don’t think password dumping works when you know the password.LMFAO**

<h4>**Part 5: Report Via End-User Training**</h4>


Your CISO asked you to present what you learned at an all-team meeting, so all the employees who send files frequently can learn to do so safely. Conclude your submission with some brief end-user training to address the following:



1. Explain the need for secure data transmission as it relates to confidentiality.
    1. **Ensures confidentiality of data during transmission.**
    2. **Protects against unauthorized access, interception, and tampering.**
2. Explain the difference between FTP and SFTP.
    3. Do they use the same ports? 
        1. **Not typically**
    4. Do they use the same software? 
        2. **They can WinSCP FTW**
    5. What are some examples of software used to access FTP and SFTP servers?
        3. **FTP: FileZilla, Cyberduck, WinSCP.**
        4. **SFTP (SSH): OpenSSH, WinSCP, Bitvise SSH Client.**
3. How does SCP protect the data being transmitted?
    6. **encrypts data during transmission.**
4. How difficult was it to exfiltrate credentials from Linux system files?
    7. **… Depends, way too broad of a question**
    8. How might a threat actor (or a pentester) utilize insecure FTP access?
        5. **Man in the Middle comes to mind!**

**Importance of Secure Data Transmission (Confidentiality):**



1. **Secure data transmission is crucial to maintaining confidentiality. When files are sent insecurely, there's a risk of unauthorized access, interception, or tampering. Encrypting data during transmission ensures that only authorized parties can access and understand the information.**
2. **FTP vs. SFTP:**
    * **Difference: FTP (File Transfer Protocol) is insecure as it transmits data in plain text, while SFTP (Secure File Transfer Protocol) encrypts the data for secure transmission.**
    * **Ports: FTP typically uses ports 20 and 21, while SFTP uses port 22.**
    * **Software: FTP and SFTP use different software. Common FTP clients include FileZilla and WinSCP, while SFTP is often integrated into SSH-enabled tools.**
3. **Examples of Software for FTP and SFTP Servers:**
    * **FTP: FileZilla, Cyberduck, WinSCP**
    * **SFTP (SSH): OpenSSH, WinSCP, Bitvise SSH Client**

**How SCP Protects Data:**



4. **SCP (Secure Copy Protocol) encrypts data during transmission, ensuring the confidentiality and integrity of the transferred files. It uses the same authentication and security mechanisms as SSH.**

**Exfiltration of Credentials from Linux System Files:**



5. **Exfiltrating credentials from Linux system files can be challenging if proper security measures are in place. Regularly updating and patching systems, using strong passwords, and implementing multi-factor authentication significantly reduce the risk.**

**Threats Associated with Insecure FTP Access:**



6. **Threat actors or pentesters may exploit insecure FTP access by:**
    * **Intercepting sensitive data during transmission.**
    * **Gaining unauthorized access to confidential files.**
    * **Conducting brute force attacks to obtain login credentials.**
    * **Tampering with files in transit.**

**End-User Training:**



* **Use SFTP Instead of FTP: Always prefer SFTP over FTP for secure file transfer.**
* **Secure Passwords: Choose strong, unique passwords and consider multi-factor authentication where available.**
* **Regularly Update Software: Keep your FTP/SFTP client and operating system updated to patch security vulnerabilities.**
* **Be Cautious with Email Links: Avoid clicking on links in emails. Instead, use secure channels to share file transfer details.**
* **Encrypt Sensitive Files: Before transmission, consider encrypting sensitive files using tools like GPG.**