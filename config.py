from pydantic_settings import BaseSettings


# define a class for the settings keys
class Settings(BaseSettings):
    google_api_key: str =""
    logfire_token: str =""

    class Config:
        env_file = ".env"

if __name__ == "main__":
    settings = Settings()
    print(f"google:{settings.google_api_key}")