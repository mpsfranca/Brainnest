# Automatic Email Sender
## Imports
```
import os
import json
import time
import logging
import schedule
from smtplib import SMTP
from datetime import datetime
from email.message import EmailMessage
```
> Libraries used in the code.
***
## Global
```
CWD = os.getcwd()
```
> This global constant is used to get the current working directory.
```
DAILY_TIME = "10:00"
```
> This global constant is used to set the time the email will be sent.
```
SRC_FOLDER = os.path.join(CWD, "src")
ATTACHMENT_FOLDER = os.path.join(CWD, "Reports")
```
> The SRC_FOLDER and ATTACHMENT_FOLDER are global constants that store the paths to folders used in the project.
```
FORMAT = "%(asctime)s : %(levelname)s - %(message)s"
```
> This global constant is used to store the format that is used by the logger.
***
## Logger Configuration
```
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
```
> This line of code uses the basicConfig function in the logging library to make messages with DEBUG level or higher appear in the log. It also sets the format the logger will use.
```
file_handler = logging.FileHandler(os.path.join(SRC_FOLDER, "Automatic Email.log"))
file_handler.setFormatter(logging.Formatter(FORMAT))
```
> This code sets a FileHandler to store the log events in a file.
```
logger = logging.getLogger("AES")
logger.addHandler(file_handler)
```
> This code creates the logger, gives it the name "AES" and associates the file_handler to it.