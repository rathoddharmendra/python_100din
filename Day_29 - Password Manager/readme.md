# LPM - Local Password Manager 
> a GUI based password manager

## Problem Statement:
Design a local password manager to local disk file, with following features:
* Store credentials to local file.
Credentials would include parameters, such as:
  * passwords
  * username
  * website
* Allows to generate a strong password
* auto populates the default email address
* Has validation against wrong input

## Design:
![design-lpm](<Screenshot 2025-01-16 at 10.16.55 AM.png>)


### venv
```
  537  python3 -m venv lpm
  538  source ./lpm/bin/activate
  539  pip3 install clipboard
  540  pip3 freeze
  541  deactivate
  542  history
```