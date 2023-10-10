from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  TG_BOT_API_KEY: str
  TG_ADMIN_CHAT_ID: str
  model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

config = Settings() # type: ignore
