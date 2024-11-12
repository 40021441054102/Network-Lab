import smtpd
import asyncore

class SimpleSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print("Incoming Message from:", peer)
        print(" - Sender:", mailfrom)
        print(" - Recipient:", rcpttos)
        print(" - Message Content:\n", data.decode("utf-8"))
        return

if __name__ == "__main__":
    server = SimpleSMTPServer(("127.0.0.1", 1025), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print("\nSMTP Server has been Stopped.")
