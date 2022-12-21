# Course Certificator Generator Python Client

## Goal

It's common to have some events at the university for the "extra hours" stuff, which results in a certificate of presence. The problem is keeping track of everyone and sending all the certificates later on...

Therefore, I built this project where you'll inform:

- The certificate template where the student name should be written to
- The CSV file containing all the names and e-mails
- SMTP credentials to send e-mails

Certificates will then be generated and sent to students.

## How to use it?

1. Install the library.

```
$ pip install ccgenerator
```

2. Declare environment variables for SMTP authentication.

```
$ export SMTP_PASSWORD='<password>'
$ export SMTP_EMAIL=<email>
$ export SMTP_SERVER=<smtp server>
$ export SMTP_PORT=<port>
```

3. Code.

```
import ccgenerator


if __name__ == '__main__':
    c = ccgenerator.CertificateGenerator('<email subject>',
                                         '<spreadsheet>.csv',
                                         '<certificate template>.png',
                                         <x position of the name>,
                                         <y position of the name>,
                                         '<font name>.ttf',
                                         <font size>)
    c.run()
```

## Example

```
import ccgenerator


if __name__ == '__main__':
    c = ccgenerator.CertificateGenerator('[WORKSHOP FEEVALE] - Certificado de Conclusão',
                                         'participantes.csv',
                                         'certificate.png',
                                         640,
                                         1000,
                                         'DejaVuSans.ttf',
                                         200)
    c.run()
```