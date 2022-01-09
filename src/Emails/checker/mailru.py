"""
Thanks to: @8Y
"""
import requests


def checker(email):
    req = requests.get(
        f"https://auth.mail.ru/api/v1/pushauth/info?language=en_US&reqmode=fg&country=US&md5_signature=4fd4fade80dc06fb19e781ae27385399&device_name=Soud%E2%80%99s%20iPhone&current=MRMail&mp=iOS&MailboxNumber=1&mmp=mail&os=iOS&udid=C4967436-C8B3-46DA-B55C-06D742CA941D&device_vendor=Apple&segments=condition_1085_MCONF-696%2Ccondition_1685_APayJSONLD%2C753_2061_pulse%20onboarding_Variant%20A6%2Ccondition_2055_MCONF-895%2Ccondition_549_MCONF-467-488-501&ver=14.3.0.16899&login={email}&concl=2&os_version=15.0&appbuild=16899&model=iPhone14%2C2&timezone=GMT%2B3&device_type=Smartphone&DeviceID=00000000-0000-0000-0000-000000000000&").json()
    print(req)
    if req["body"]["exists"] == True:
        return True
    elif req["body"]["exists"] == False:
        return False
    else:
        return None
