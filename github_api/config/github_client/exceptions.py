
class BaseAPIError(Exception):
    pass


github_client_messages_error = {
    "login_error": "Error: логин должен быть типом 'str'. Указанный Вами тип: {}",
    "password_error": "Error: пароль   должен быть типом 'str'. Указанный Вами тип: {}",
}
