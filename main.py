from dotenv import load_dotenv, find_dotenv

from priority_queue_web_api import create_app


load_dotenv(find_dotenv())
app = create_app()
app.app_context().push()
