from typing import Union

import pyrogram
from pyrogram.types import (InputMediaAudio, InputMediaDocument, InputMediaPhoto,
                            InputMediaVideo)

from ... import TG_AutoPoster
from .parser import Post


class Sender:
    def __init__(
        self,
        bot: TG_AutoPoster.AutoPoster,
        post: Post,
        chat_ids: list[Union[int, str]],
        disable_notification: bool = False,
        disable_web_page_preview: bool = True,
        **kwargs,
    ):
        self._bot = bot
        self.post = post
        self.chat_ids = chat_ids
        self.disable_notification = disable_notification
        self.disable_web_page_preview = disable_web_page_preview

    def send_post(self):
        for chat_id in self.chat_ids:
            self.send_splitted_message(self.post.text, chat_id)
            if len(self.post.text) > 1 or len(self.post.attachments) == 0:
                self._bot.send_message(
                    chat_id,
                    self.post.text[-1],
                    reply_markup=self.post.reply_markup,
                    disable_web_page_preview=self.disable_web_page_preview,
                    disable_notification=self.disable_notification,
                )
                caption = ""
            else:
                caption = self.post.text[-1]

            if self.send_attachments(chat_id, self.post.attachments["media"], caption):
                caption = ""
            if self.send_attachments(chat_id, self.post.attachments["audio"], caption):
                caption = ""
            self.send_attachments(chat_id, self.post.attachments["docs"], caption)

            if hasattr(self.post, "poll") and self.post.poll:
                print(hasattr(self.post, "poll") and self.post.poll)
                self.send_poll(chat_id)

    def send_attachments(self, chat_id, attachments, caption):
        if len(attachments) == 0:
            return False
        elif len(attachments) == 1:
            attachment = attachments[0]
            if isinstance(attachment, InputMediaPhoto):
                self._bot.send_photo(
                    chat_id,
                    attachment.media,
                    caption=caption,
                    reply_markup=self.post.reply_markup,
                    disable_notification=self.disable_notification,
                )
            elif isinstance(attachment, InputMediaVideo):
                self._bot.send_video(
                    chat_id,
                    attachment.media,
                    caption=caption,
                    reply_markup=self.post.reply_markup,
                    disable_notification=self.disable_notification,
                )
            elif isinstance(attachment, InputMediaDocument):
                self._bot.send_document(
                    chat_id,
                    document=attachment.media,
                    caption=caption,
                    disable_notification=self.disable_notification,
                )
            elif isinstance(attachment, InputMediaAudio):
                self._bot.send_audio(
                    chat_id,
                    attachment.media,
                    thumb=attachment.thumb,
                    duration=attachment.duration,
                    title=attachment.title,
                    performer=attachment.performer,
                    caption=caption,
                )
        else:
            attachments[0].caption = caption
            self._bot.send_media_group(
                chat_id,
                media=attachments,
                disable_notification=self.disable_notification,
            )
        return True

    def send_poll(self, chat_id):
        # log.info("Отправка опроса")
        try:
            self._bot.send_poll(
                chat_id,
                **self.post.poll,
                disable_notification=self.disable_notification,
            )
        except pyrogram.errors.BroadcastPublicVotersForbidden:
            # log.exception(
            #     "Отправка публичных опросов в каналы запрещена. Попытка отправить анонимный опрос."
            # )
            self.post.poll["is_anonymous"] = False
            self._bot.send_poll(
                chat_id,
                **self.post.poll,
                disable_notification=self.disable_notification,
            )

    def send_splitted_message(self, text, chat_id):
        for i in range(len(text) - 1):
            self._bot.send_message(
                chat_id, text[i], disable_notification=self.disable_notification
            )
