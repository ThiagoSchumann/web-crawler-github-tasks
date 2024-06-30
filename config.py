# config.py

from decouple import config

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")
DRIVER_PATH = "C:\\Projects\\web-crawler-github-tasks\\driver\\chromedriver.exe"
GITHUB_LOGIN_URL = "https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home"
PROJECT_URL = "https://github.com/users/ThiagoSchumann/projects/10"
