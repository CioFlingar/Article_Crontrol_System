import resend

resend.api_key = "re_6W4SZhy3_4K8LCFrsYkX4DWS8rb6iFKEe"

resp = resend.Emails.send({
  "from": "onboarding@resend.dev",
  "to": "rcrickymarvin@gmail.com",
  "subject": "Hello World",
  "html": "<p>Congrats on sending your <strong>first email</strong>!</p>"
})

if resp == "200":
    print("success")
else:
    print(resp)