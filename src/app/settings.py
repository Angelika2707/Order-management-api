from envparse import env

env.read_envfile()

DEBUG = env.bool("DEBUG", default=False)
PORT = env.int("PORT", default=8000)
SECRET_KEY = env.str("SECRET_KEY", default="12345")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost"])

DB_NAME = env.str("DB_NAME", default="postgres")
DB_USER = env.str("DB_USER", default="postgres")
DB_PASSWORD = env.str("DB_PASSWORD", default="postgres")
DB_HOST = env.str("DB_HOST", default="localhost")
DB_PORT = env.int("DB_PORT", default=5432)

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"