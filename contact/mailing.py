import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(subject, message, name, email, phone="N/A"):

    message = Mail(
        from_email="noreply@hackathonturkiye.com",
        to_emails="hackathonturkiye@gmail.com",
        subject=subject,
        html_content="<h1>İletişim Formu</h1>\n<p>Mesaj: {}</p>\n<p>Ad Soyad: {}</p>\n<p>Email: {}</p>\n<p>Telefon: {}</p>".format(
            message, name, email, phone
        ),
    )
    try:
        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
        response = sg.send(message)
    #   print(response.status_code)
    #   print(response.body)
    #   print(response.headers)
    except Exception as e:
        print(e.args)

