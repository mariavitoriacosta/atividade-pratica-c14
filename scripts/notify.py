import smtplib
import os
from email.mime.text import MIMEText

destino   = os.environ["EMAIL_DESTINO"]
remetente = os.environ["EMAIL_REMETENTE"]
senha     = os.environ["EMAIL_SENHA"]
test      = os.environ["TEST_RESULT"]
build     = os.environ["BUILD_RESULT"]
deploy    = os.environ["DEPLOY_RESULT"]

status = "SUCESSO" if all(r == "success" for r in [test, build, deploy]) else "FALHA"

corpo = f"""
Pipeline finalizada com status: {status}

- Test:   {test}
- Build:  {build}
- Deploy: {deploy}
"""

msg = MIMEText(corpo)
msg["Subject"] = f"Pipeline CI/CD - {status}"
msg["From"]    = remetente
msg["To"]      = destino

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(remetente, senha)
    server.sendmail(remetente, destino, msg.as_string())

print(f"Notificacao enviada para {destino}")