# Production_Grade_Coding
These is not a real project, but a simple production grade code using functional &amp; modular programming or Oops (Object Oriented Programming) 

1. Password should be in encrypted format.
2. Connection details, API keys, API secrets, etc should in config file in config.ini. 
3. Create clear function through which we can call function & return the value.
4. Write code in folder structure to access in another file easily.
5. Create main method for code & use main method to call it.

### Folder Structure
Production_coding/
└── src/
    ├── main/
    │   ├── database/
    │   │   └── mysql_connector.py
    │   ├── encrypt_decrypt/
    │   │   └── encrypt_decrypt.py
    │   ├── resources/
    │   │   └── config.ini
    │   └── main.py
    └── test/
        └── scratch_pad.py
        
* **📁 main/**: The core application folder, where the real work happens. Think of it as the engine room.
* **📄 main.py**: Startup logic that imports modules and kicks off the workflow—connects to DB, loads config, decrypts passwords, and runs processes.
* **📁 database/mysql_connector.py**: Python module responsible for establishing connection with MySQL, running queries, and handling exceptions.
* **📁 encrypt_decrypt/encrypt_decrypt.py**: Includes functions to encrypt sensitive data (e.g. passwords) and decrypt it when needed, possibly using cryptography or Fernet
* **📁 resources/config.ini**: Stores parameters such as database credentials, file paths, API keys, or custom settings. It’s parsed at runtime using configparser.
* **📁 test/**: The testing folder, where you experiment and validate code before it goes live.



### ✨ How to Create This Structure via Terminal (Git Bash)
* mkdir -p Production_coding/src/main/database
* mkdir -p Production_coding/src/main/encrypt_decrypt
* mkdir -p Production_coding/src/main/resources
* mkdir -p Production_coding/src/test

* touch Production_coding/src/main/database/mysql_connector.py
* touch Production_coding/src/main/encrypt_decrypt/encrypt_decrypt.py
* touch Production_coding/src/main/resources/config.ini
* touch Production_coding/src/main/main.py
* touch Production_coding/src/test/scratch_pad.py

### Push Local Project to GitHub Using Git Bash
* 1️⃣ Initialize Git in Your Project Folder: sets up your folder as a Git repository "git init"
* 2️⃣ Stage and Commit Your Files: "git add ." & git commit -m "Initial commit"
* 3️⃣ Add the Remote Repository: "git remote add origin https://github.com/shreeram0912/Production_Grade_Coding.git"
* 4️⃣ Push Your Code to GitHub: "git branch -M main" & "git push -u origin main"
* If Error = ! [rejected]
* ✅ Fix: Pull Remote Changes Before Pushing: "git pull origin main --rebase" & "git push -u origin main"
