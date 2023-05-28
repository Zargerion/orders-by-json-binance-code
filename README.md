# Binance make and cancel N orders by JSON file with some parameters.

## Использованы фьючерсы BNBUSDT.

## Json файл был немного измененен. А именно числовые параметры были подкорректированы под фьючерсный инструмент.

## Чтобы запустить:

1. Выполните в командной строке: ```pip install python-binance==1.0.17```, если ранее у вас не была установлена данная библиотека.
2. Измените ```api = "Your API Key``` и ```secret = "Your API Secret"``` на ваши значения API ключа в ```simple-code.ipynb``` или ```main.py```. (Из можно получить по ссылке ```https://testnet.binancefuture.com/en/futures/BNBUSDT``` там, где отображаются открытые ордера, позиции и т.д.)
3. Запустите ```simple-code.ipynb``` или ```main.py``` или ```tests.py```.
* При этом рекомендуется открыть данную ссылку для более комфортного мониторинга происходящего: ```https://testnet.binancefuture.com/en/futures/BNBUSDT```. Возможно для прохождения по ссылке может потребовать регистрация обычного binance-аккаунта.
* Код был написан c помощью версии Python 9.11.