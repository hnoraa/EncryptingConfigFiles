# Fernet Encrytion
Uses the cryptography library (see: requirements.txt).

This utilizes .json files for configuration

## Flow
1. Encrypt the config file
2. On program load, open the encrypted config file
3. Decrypt config file
4. Load the data into an object