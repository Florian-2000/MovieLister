import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


if __name__ == '__main__':
    install("clipboard")
    install("inflect")
    install("google-api-python-client")     # If this does not work, execute following in terminal:
                                            # pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
