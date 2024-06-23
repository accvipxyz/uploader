import os


class Config:

    BOT_TOKEN = os.environ.get("7348415101:AAHCeZz25fmNlnsmvmx_275xHueDgrBa98E")

    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")

    API_ID = int(os.environ.get("27907125"))

    API_HASH = os.environ.get("334db6079e137ae12532a00b8786eafc")

    CLIENT_ID = os.environ.get("185686440219-95imbm2k1f42ok6qcvp2id3va9l31b6v.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("5599020702"))

    AUTH_USERS_TEXT = os.environ.get("5599020702", "")

    AUTH_USERS = [BOT_OWNER, 5599020702] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
