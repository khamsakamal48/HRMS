
# HRMS Auto-Login & Check-in tool

Will auto-login to IITB DRF's HRMS portal and mark your attendance

- The script will login to HRMS, wait for anywhere between 1 minute to 60 minutes, and then checks-in or check-out for you. This way your in and out are random in a given time frame.
- The script will not run if,
  - The day is a Saturday or Sunday
  - Is a Holiday (as per the dates mentioned in the Holiday_List.csv)


## Prerequisites

- Google Chrome & MS Edge
- Python 3

## Deployment

To deploy this project, you need to install some modules first after fulfilling the pre-requisites.

Copy below commands in your terminal

```bash
  sudo apt install python3-pip
  
  pip install selenium
  pip install webdriver-manager
  pip install python-dotenv
```

Clone the project

```bash
  git clone https://github.com/khamsakamal48/HRMS.git
```

Add the HRMS URL, Username & Password for HRMS, Email server URL, port and credentials in the .env file

```bash
  URL=
  LOGIN=
  PASSWORD=
  SMTP_SERVER=
  SMTP_PORT=
  IMAP_PORT=
  SMTP_LOGIN=
  SMTP_PASSWORD=
  EMAIL_TO=
```
Make sure your Leaves and Holiday list in updated in the Holiday_list.csv file
## Run Locally

Go to the project directory

```bash
  cd your_server_path/HRMS
```

Manually start the script

```bash
  python3 Login.py
```

Set a scheduler via cron
```bash
  crontab -e

  # Run at 9:30 AM
  30 9 * * * cd your_server_path/HRMS/ && python3 Login.py

  # Run at 5:30 AM
  30 17 * * * cd your_server_path/HRMS/ && python3 Login.py

```
## Notes

Since, HRMS is hosted on the internet - If the internet at the campus goes down then this won't work for obvious reasons. Under such circumstances, you need to log into HRMS using your phone and check-in or out.

## Disclaimer
I am just providing you a script so that you don't have to worry about this silly attendance routine and focus on our work. With that said, I hold no responsibility for the misuse of this tool. 
