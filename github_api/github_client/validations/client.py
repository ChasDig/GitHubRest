import dataclasses
import json
import requests

from github_api.github_client.auth import Auth
from github_api.config.github_client.exceptions import BaseAPIError
from github_api.config.github_client.exceptions import (
    github_client_messages_error
)


class BaseGitHubClientValidator:

    @staticmethod
    def check_base_response(github_api_response: requests.Response) -> bool:
        """
         Валидация ответа на запрос в GitHubApi.

        :param requests.Response github_api_response: Ответ на запрос.
        :return bool: Результат валидации.
        """
        if 200 <= github_api_response.status < 400:
            return True
        if github_api_response.status in [401, 403]:
            pass
        raise BaseAPIError(json.dumps(dataclasses.asdict(github_api_response.status)))

    @staticmethod
    def check_github_client(
            login: str | None = None,
            password: str | None = None,
            token: str | None = None,
    ) -> bool:
        """
         Проверяем валидность данных

        :param str | None login: Логин пользователя.
        :param str | None password: Пароль пользователя.
        :param str | None token: Токен для авторизации пользователя.
        :return bool: Результат валидации.
        """
        # Проверка логина:
        assert login is None or isinstance(login, str), github_client_messages_error.get("login_error").format(
            type(login),
        )
        # Проверка пароля:
        assert password is None or isinstance(password, str), github_client_messages_error.get("password_error").format(
            type(password),
        )
        # Проверка токена:
        assert token is None or isinstance(token, str), github_client_messages_error.get("token_error").format(
            type(token),
        )
        return True
