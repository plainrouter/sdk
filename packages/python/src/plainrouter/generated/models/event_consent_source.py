from enum import Enum


class EventConsentSource(str, Enum):
    CMPCONSENTSTACK = "cmp:consentstack"
    CMPCOOKIEBOT = "cmp:cookiebot"
    CMPCOOKIEYES = "cmp:cookieyes"
    CMPIUBENDA = "cmp:iubenda"
    CMPUSERCENTRICS = "cmp:usercentrics"
    CONSENT_MODE = "consent_mode"
    EXPLICIT = "explicit"
    PLAINROUTER = "plainrouter"
    TCF = "tcf"

    def __str__(self) -> str:
        return str(self.value)
