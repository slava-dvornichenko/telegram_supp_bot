from loader import dp
from aiogram.types import Message
from keyboards.default import faq, starting
from aiogram.dispatcher.filters import Command,Text



@dp.message_handler(Command("faq"))
async def faq_start(message:Message):
    await message.answer("Что вас интересует?", reply_markup=faq)

@dp.message_handler(Text(equals=["FAQ"]))
async def show_faq2(message:Message):
    await message.answer(f"Что вас интересует?", reply_markup=faq)


@dp.message_handler(Text(equals=["Что такое VPN?"]))
async def show_faq1(message:Message):
    await message.answer(f"VPN – это виртуальная частная сеть, обеспечивающая пользователю анонимность при работе в интернете. С помощью данной технологии создается новое соединение поверх основной сети. Она позволяет защитить личную информацию, скрыть свое местонахождение и обойти блокировки. ")

@dp.message_handler(Text(equals=["Законность VPN"]))
async def show_faq2(message:Message):
    await message.answer(f"В данный момент на территории РФ нет закона, запрещающего использование VPN")

@dp.message_handler(Text(equals=["Законность обхода блокировки"]))
async def show_faq3(message:Message):
    await message.answer(f"Да. \nПруф 1 - https://radiosputnik.ria.ru/20220314/vpn-1778025406.html \nПруф 2 - https://news.rambler.ru/internet/48294998-rossiyanam-rasskazali-zakonno-li-ispolzovat-vpn/Но помните, совершая на любых ресурсах (заблокированных и нет) противозаконные действия - вы нарушаете закон")

@dp.message_handler(Text(equals=["Преимущества вашего VPN"]))
async def show_faq4(message:Message):
    await message.answer(f"- Скорость. Вы даже не заметите, что у вас включен VPN.\n- Защищенность. Мы не пишем логи наших клиентов, все клиентские каналы защищены шифрованием. Построение маршрутов трафика происходит в автоматическом режиме с распредилением нагрузки, поэтому мы не знаем и не можем предугадать каким именно путем пойдет трафик клиента. На серверах не храниться никаких личных данных пользователей.\n- Шанс блокировки сведен к нулю. Популярные зарубежные VPN-сервисы активно блокируются РосКомНадзором, потому что их достаточно лего вычислить. Наша сеть приватная, вычислить ее практически невозможно. А даже если вычислят - у нас есть запасная 🙂  \n- Цена. Стоимость нашего VPN всего 500руб в месяц (акция на первые 3 месяца). Далее 1000руб/мес. В любой тарифный план включено 3 устройства (можно поставить себе, второй половинке и коту). Для сравнения, основная масса зарубежных VPN стоит от 10$ в месяц (от 1100руб) ")

@dp.message_handler(Text(equals=["Поддержка устройствами"]))
async def show_faq5(message:Message):
    await message.answer(f"Любые устройства компании Apple. Все современные Android. И конечно Windows и Ubuntu 🙂 ")

@dp.message_handler(Text(equals=["Преимущества платного VPN"]))
async def show_faq6(message:Message):
    await message.answer(f"У многих сервисов есть бесплатные планы, однако в обмен на это пользователь теряет высокую скорость соединения, возможность выбрать лучший сервер или подключить больше одного устройства, а иногда и вовсе отдает свои персональные данные третьим лицам и подвергается слежению посторонними сайтами.")

@dp.message_handler(Text(equals=["Вернуться в меню"]))
async def show_faq2(message:Message):
    await message.answer(f"Выберите действие:", reply_markup=starting)

