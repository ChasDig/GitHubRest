import aiohttp
import requests

from github_api.config.github_client import consts
from github_api.github_client.validations import BaseGitHubClientValidator


class BaseGitHubClient:
    DEFAULT_API = consts.DEFAULT_BASE_URL

    def __init__(
            self,
            login: str | None = None,
            password: str | None = None,
            token: str | None = None,
            base_url: str = DEFAULT_API,
            timeout: int = aiohttp.ClientTimeout(total=consts.DEFAULT_API_REQUEST_TIMEOUT)
    ) -> None:
        """
         GitHubClient - базовый клиент для работы с GitHubApi.

        :param str | None login: Логин пользователя.
        :param str | None password: Пароль пользователя.
        :param str | None token: Токен для авторизации пользователя.
        :param str | None base_url: Базовый URL.
        :return: None
        """
        if BaseGitHubClientValidator.check_github_client(
            login=login,
            password=password,
            token=token,
        ):
            self.login = login
            self.password = password
            self.token = token
            self.base_url = base_url
            self._timeout = timeout

    @property
    def _base_header(self) -> dict:
        """
         Базовый заголовок запроса.

        :return dict base_header: Заголовок запроса.
        """
        base_header = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self.token}",
            "content-type": "application/json"
        }
        return base_header

    async def _call_api(self, method: str, url: str, *args, **kwargs) -> dict:
        """
         Базовый запрос на GItHub API.

        :param str method: Метод запрос.
        :param str url: URL-запроса.
        :return: None
        """
        headers = self._base_header
        async with aiohttp.ClientSession(timeout=self._timeout) as session:
            _method = getattr(session, method)
            async with _method(self.DEFAULT_API + url, *args, **kwargs, headers=headers, ssl=False) as res:
                return await self._github_api_response(res)

    def _github_api_response(self, res: requests.Response) -> dict:
        """
         Обработка ответа на запрос в GitHubApi.

        :param requests.Response res: Ответ на запрос.
        :return dict _response: Сериализованный ответ на запрос.
        """
        _response = res.json()
        BaseGitHubClientValidator.check_base_response(github_api_response=res)
        return _response

    async def get(self, url: str, *args, **kwargs) -> dict:
        """
         Базовый GET-запрос на GItHub API.

        :param str url: URL-запроса.
        :return dict result_get: результат GET-запроса.
        """
        result_get = await self._call_api(method="get", url=url, *args, **kwargs)
        return result_get
