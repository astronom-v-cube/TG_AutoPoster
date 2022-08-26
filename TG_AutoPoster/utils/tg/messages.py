ACCESS_DENIED = (
    "Список администраторов бота не был настроен.\n"
    "Для доступа к настройкам отправьте команду /register с токеном этого бота."
)

HELP = (
    "<b>Доступные команды:</b>\n"
    "/help - список команд\n"
    "/settings - настройка автопостинга\n"
    "/get_full_logs - получить полные логи\n"
    "/get_last_logs [n] - получить последние n строк логов (по умолчанию 15)\n"
    "/remove - удалить источник постов\n"
    "/add - добавить источник постов\n"
    "/get_config - получить файл конфигурации бота\n"
    "/restart - перезапустить бота\n"
    "/about - о боте\n\n"
    "Для настройки источников необходимо включить <a href='https://core.telegram.org/bots/inline'>inline mode.</a>"
)

ADD = (
    "Команда используется для добавления нового источника постов.\n\n"
    "Использование:\n`/add <домен или ссылка группы ВК> <ID Telegram чата (или ссылка через @)> "
    "[ID поста] [ID закрепленного поста] [ID истории]`\n"
    "`<>` - обязательный параметр\n`[]` - необязательный параметр\n"
    "`ID поста ВК` - начиная с какого поста бот должен начать отправку постов "
    "(если не указано, бот отправит последние 11 постов)"
)

REMOVE = (
    "Команда используется для удаления источника постов.\n\n"
    "Использование:\n`/remove <домен группы ВК>`\n"
    "`<>` - обязательный параметр"
)

SEND_POST = (
    "Команда используется для отправки конкретного поста.\n\n"
    "Использование:\n `/send_post <ссылка на пост> [ID Telegram чата (или ссылка через @)]`\n"
    "`<>` - обязательный параметр\n`[]` - необязательный параметр\n"
    "Если не указан ID Telegram чата, будет использовано значение main_group из файла конфигурации"
)

INLINE_INPUT_MESSAGE_CONTENT = (
    "Источник https://vk.com/{}\n\n"
    "Посты отправляются в чат: {}\n"
    "ID последнего отправленного поста: {}\n"
    "ID последней отправленной истории: {}\n"
    "ID закрепленного поста: {}\n"
    "Отправляемые вложения: `{}`\n"
)

GLOBAL_SETTINGS = "**Текущие настройки бота:**\n\nОтправляемые вложения: `{}`"

PARTIAL_REPOSTS = (
    "\n\nТолько пост (частичная отправка) означает отправлять пост без самого репоста"
    " (если пост содержит только репост, он не будет отправлен)"
)

SOURCE_USE_GLOBAL_SETTINGS = (
    "Этот источник использует общие настройки отправки репостов (см. в /settings)."
    "Изменения настроек здесь приведет к их переопределению\n"
)

SECTION_DELETED = (
    "Источник {0} был удален.\nДля его восстановления используйте команду"
    " `/add {0} {channel} {last_id} {pinned_id} {last_story_id}`"
)

LOG_MESSAGE = (
    "Пользователь {message.from_user.first_name} {message.from_user.last_name} "
    "c ID {message.from_user.id} использовал команду {message.text}"
)

LOG_INLINE_QUERY = (
    "Пользователь {message.from_user.first_name} {message.from_user.last_name} "
    "c ID {message.from_user.id} выполнил запрос со следующим текстом: {message.query}"
)

LOG_CALLBACK_QUERY = (
    "Пользователь {message.from_user.first_name} {message.from_user.last_name} "
    "c ID {message.from_user.id} использовал обратный запрос со следующим содержимым {message.data}"
)

ABOUT = (
    "[TG_AutoPoster](https://github.com/qwertyadrian/TG_AutoPoster) - бот, "
    "предназначенный для пересылки постов из ВКонтакте в Telegram.\n\n"
    "Связаться с разработчиком: @QwertyAdrian"
)

ATTACHMENTS_TYPES = {
    "text": "Текст: {}",
    "link": "Ссылки: {}",
    "photo": "Фото: {}",
    "doc": "Документы: {}",
    "video": "Видео: {}",
    "music": "Музыка: {}",
    "polls": "Опросы: {}",
}
