import msal
import config


def login():

    app = msal.PublicClientApplication(
        config.CLIENT_ID,
        authority=config.AUTHORITY
    )

    result = app.acquire_token_interactive(
        scopes=config.SCOPES
    )

    return result