import os, time, datetime, sys, ssl, smtplib, imaplib

# Set current directory
#os.chdir(os.path.dirname(sys.argv[0]))
os.chdir(os.getcwd())

from dotenv import load_dotenv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from random import *
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

# Textual month, day and year
todays_date = datetime.now().strftime("%d %B %Y")
todays_day = datetime.now().strftime("%A")

def send_email():
    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = os.getenv("SMTP_PORT")
    SMTP_LOGIN = os.getenv("SMTP_LOGIN")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
    EMAIL_TO =  os.getenv("EMAIL_TO")
    IMAP_PORT =  os.getenv("IMAP_PORT")
    
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = SMTP_LOGIN
    message["To"] = EMAIL_TO
    
    TEMPLATE = """<!DOCTYPE html>
    <html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">
    <head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
    <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 0;
            }

            a[x-apple-data-detectors] {
                color: inherit !important;
                text-decoration: inherit !important;
            }

            #MessageViewBody a {
                color: inherit;
                text-decoration: none;
            }

            p {
                line-height: inherit
            }

            @media (max-width:660px) {
                .icons-inner {
                    text-align: center;
                }

                .icons-inner td {
                    margin: 0 auto;
                }

                .row-content {
                    width: 100% !important;
                }

                .column .border {
                    display: none;
                }

                .stack .column {
                    width: 100%;
                    display: block;
                }
            }
        </style>
    </head>
    <body style="background-color: #f8f8f9; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
    <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #f8f8f9;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1aa19c;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #1aa19c; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td>
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff; color: #000000; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="empty_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td>
    <div></div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #f8f8f9; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="20" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td>
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff; color: #000000; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="padding-bottom:12px;padding-top:60px;">
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="image_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="padding-left:40px;padding-right:40px;width:100%;">
    <div align="center" style="line-height:10px"><img alt="I'm an image" src="https://iitbombay.digitalhrms.com/images/ingograph.png" style="display: block; height: auto; border: 0; width: 256px; max-width: 100%;" title="I'm an image" width="256"/></div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="padding-top:50px;">
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td style="padding-bottom:10px;padding-left:25px;padding-right:25px;padding-top:10px;">
    <div style="font-family: sans-serif">
    <div style="font-size: 12px; mso-line-height-alt: 14.399999999999999px; color: #555555; line-height: 1.2; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;">
    <p style="margin: 0; font-size: 16px; text-align: center;"><span style="font-size:30px;color:#2b303a;"><strong>Hi,</strong></span></p>
    </div>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:10px;">
    <div style="font-family: sans-serif">
    <div style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;">
    <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 22.5px;"><span style="color:#808389;font-size:15px;">Based on the subject of email you are requested to take further action for marking your attendance in HRMS.</span></p>
    <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 18px;"> </p>
    <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 22.5px;"><span style="color:#808389;font-size:15px;">If the status is SUCCESS, you don't need to make any further action and you can safely delete this email.</span></p>
    <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 18px;"> </p>
    <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 22.5px;"><span style="color:#808389;font-size:15px;">If the status is FAILURE, requesting you to please click the below button and log into HRMS to mark your attendance.</span></p>
    </div>
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #fff; color: #000000; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="button_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="padding-left:10px;padding-right:10px;padding-top:40px;text-align:center;">
    <div align="center">
    <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="https://iitbombay.digitalhrms.com/Login.aspx" style="height:62px;width:166px;v-text-anchor:middle;" arcsize="97%" stroke="false" fillcolor="#1aa19c"><w:anchorlock/><v:textbox inset="0px,0px,0px,0px"><center style="color:#ffffff; font-family:Tahoma, sans-serif; font-size:16px"><![endif]--><a href="https://iitbombay.digitalhrms.com/Login.aspx" style="text-decoration:none;display:inline-block;color:#ffffff;background-color:#1aa19c;border-radius:60px;width:auto;border-top:1px solid #1aa19c;border-right:1px solid #1aa19c;border-bottom:1px solid #1aa19c;border-left:1px solid #1aa19c;padding-top:15px;padding-bottom:15px;font-family:Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:30px;padding-right:30px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="font-size: 16px; margin: 0; line-height: 2; word-break: break-word; mso-line-height-alt: 32px;"><strong>Log into HRMS</strong></span></span></a>
    <!--[if mso]></center></v:textbox></v:roundrect><![endif]-->
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="padding-bottom:12px;padding-top:60px;">
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 0px solid #BBBBBB;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; background-color: #2b303a; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 0px; padding-bottom: 0px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td>
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 4px solid #1AA19C;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="text_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
    <tr>
    <td style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:15px;">
    <div style="font-family: sans-serif">
    <div style="font-size: 12px; font-family: Montserrat, Trebuchet MS, Lucida Grande, Lucida Sans Unicode, Lucida Sans, Tahoma, sans-serif; mso-line-height-alt: 18px; color: #555555; line-height: 1.5;">
    <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 18px;"><span style="color:#95979c;font-size:12px;">Sent by an automated program</span></p>
    </div>
    </div>
    </td>
    </tr>
    </table>
    <table border="0" cellpadding="0" cellspacing="0" class="divider_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="padding-bottom:10px;padding-left:40px;padding-right:40px;padding-top:25px;">
    <div align="center">
    <table border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #555961;"><span> </span></td>
    </tr>
    </table>
    </div>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-7" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tbody>
    <tr>
    <td>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 640px;" width="640">
    <tbody>
    <tr>
    <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
    <table border="0" cellpadding="0" cellspacing="0" class="icons_block" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="vertical-align: middle; padding-bottom: 5px; padding-top: 5px; color: #9d9d9d; font-family: inherit; font-size: 15px; text-align: center;">
    <table cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
    <tr>
    <td style="vertical-align: middle; text-align: center;">
    <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
    <!--[if !vml]><!-->
    <table cellpadding="0" cellspacing="0" class="icons-inner" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; margin-right: -4px; padding-left: 0px; padding-right: 0px;">
    <!--<![endif]-->
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table>
    </td>
    </tr>
    </tbody>
    </table><!-- End -->
    </body>
    </html>
    """
    
    # Create a text/html message from a rendered template
    emailbody = MIMEText(TEMPLATE, "html")
    
    # Add HTML parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(emailbody)
    emailcontent = message.as_string()

    # Create secure connection with server and send email
    context = ssl._create_unverified_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(SMTP_LOGIN, SMTP_PASSWORD)
        server.sendmail(
            SMTP_LOGIN, SMTP_LOGIN, emailcontent
        )

    # Save copy of the sent email to sent items folder
    with imaplib.IMAP4_SSL(SMTP_SERVER, IMAP_PORT) as imap:
        imap.login(SMTP_LOGIN, SMTP_PASSWORD)
        imap.append('Sent', '\\Seen', imaplib.Time2Internaldate(time.time()), emailcontent.encode('utf8'))
        imap.logout()
              
with open('Holiday_List.csv', 'r') as holiday_list:
    try:
        if todays_date in holiday_list.read() or todays_day == "Sunday" or todays_day == "Saturday":
            print ("It's a holiday today")
        else:
            # Pick a random number between 1 to 3600 seconds (within an hour)
            random = randint(1, 3600)

            # Sleep for the random number before logging into HRMS
            time.sleep(random)

            # Retrieve contents from .env file
            URL = os.getenv("URL")
            LOGIN = os.getenv("LOGIN")
            PASSWORD = os.getenv("PASSWORD")

            driver = webdriver.Chrome(ChromeDriverManager().install())

            # Open HRMS Page
            driver.get(URL)

            # Wait
            driver.implicitly_wait(15)

            # Enter Username
            driver.find_element_by_id("txtUserName").send_keys(LOGIN)

            # Enter password
            driver.find_element_by_id ("txtPassword").send_keys(PASSWORD)

            # Click on the Login Button
            driver.find_element_by_id("btnLogin").click()
            
            time.sleep(15)

            # # Click on the Check-in/Check-out button
            driver.find_element_by_id("btnCheckin").click()
            
            time.sleep(15)

            driver.quit()
            
            # Send email on success
            subject = "HRMS Auto Check-in/out | Status: SUCCESS"
            send_email()
            
            sys.exit()
    except:
        subject = "HRMS Auto Check-in/out | Status: FAILURE"
        send_email()
        sys.exit()