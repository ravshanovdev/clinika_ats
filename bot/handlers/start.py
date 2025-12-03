from aiogram import types, Router
from aiogram.filters import Command
from asgiref.sync import sync_to_async
from connect.models import TgAdmin, SendMessage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()


@router.message(Command('start'))
async def start_cmd(msg: types.Message):
    if msg.from_user.username in ['maybe_0101', 'jamzayn10']:
        await sync_to_async(TgAdmin.objects.get_or_create)(
                username=msg.from_user.username,
                chat_id=msg.from_user.id
            )
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="today"), KeyboardButton(text="week")]
            ],
            resize_keyboard=True
        )

        await msg.answer('Salom! Statistikalarni olish uchun:', reply_markup=keyboard)

    elif msg.from_user.username not in ['maybe_0101', 'jamzayn10']:
        await msg.answer('Salom! Siz bu botdan foydalana olish huquqiga ega emas siz.!')


@router.message(lambda msg: msg.text == 'today')
async def today_cmd(msg: types.Message):

    is_admin = await sync_to_async(TgAdmin.objects.filter(username=msg.from_user.username).exists)()
    if not is_admin:
        return

    @sync_to_async
    def get_rows():
        from datetime import date

        today = date.today()
        return list(SendMessage.objects.filter(created_at__date=today).values(
            'username', 'phone', 'email', 'text', 'created_at')
        )

    rows = await get_rows()

    if not rows:
        await msg.answer("Bugun murojaat yo‘q.")
        return

    text = "📅 Bugungi murojaatlar:\n\n"

    for row in rows:
        time_str = row['created_at'].strftime('%H:%M')
        text += f"👤 {row['username']}\n📱 " \
                f"{row['phone']}\n📧  " \
                f"{row['email']}\n💬 " \
                f"{row['text']}\n⏰ " \
                f"{time_str}\n\n"

    await msg.answer(text)


@router.message(lambda msg: msg.text == 'week')
async def week_cmd(msg: types.Message):

    is_admin = await sync_to_async(TgAdmin.objects.filter(username=msg.from_user.username).exists)()
    if not is_admin:
        return

    @sync_to_async
    def get_row():
        from django.utils.timezone import now
        from datetime import timedelta

        week_ago = now() - timedelta(days=7)
        return list(SendMessage.objects.filter(created_at__date__gte=week_ago.date()).values(
            'username', 'phone', 'email', 'text', 'created_at')
        )

    rows = await get_row()

    if not rows:
        await msg.answer("hatfalik murojatlar mavjud emas.!")
        return

    text = "📊 Oxirgi 7 kun murojaatlari:\n\n"
    for row in rows:
        time_str = row['created_at'].strftime('%H:%M')
        text += f"👤{row['username']}\n📱 " \
                f"{row['phone']}\n📧  " \
                f"{row['email']}\n💬 " \
                f"{row['text']}\n⏰ " \
                f"{row['created_at'].date()} ({time_str})\n\n"

    await msg.answer(text)


