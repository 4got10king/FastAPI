from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        env_prefix="BACKEND_SERVER__",
    )
    PORT: int
    HOST: str
    WORKERS: int
    METHODS: List[str]
    HEADERS: List[str]
    origins: List[str] = ["*"]

    @property
    def app_settings(self):
        return self

    @property
    def swagger_conf(self) -> dict:
        return dict(
            version="0.0.1",
            description="TEST",
            title="TEST",
            docs_url="/api/swagger",
            openapi_url="/api/test",
        )

    @computed_field(return_type=str)
    @property
    def server_url(self) -> str:
        return f"http://{self.HOST}:{self.PORT}"


app_config = AppSettings()
