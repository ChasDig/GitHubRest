import abc


class Auth(abc.ABC):
    """Базовый"""

    @property
    @abc.abstractmethod
    def token(self) -> str:
        """
        Абстрактный метод для авторизации чрез token. Метод возвращает токен.

        :return str: Токен авторизации.
        """
        pass


class TokenAuth(Auth):

    def __init__(self, token: str) -> None:
        """
         Dunder-метод. Инициализация.

        :param str token: GitHub-token для авторизации.
        :return str token:  GitHub-token для авторизации.
        """
        self._token = token

    @property
    def token(self) -> str:
        return self._token

