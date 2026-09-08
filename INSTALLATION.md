# Орнату нұсқаулығы — Alem Trans.KZ лендингі

Жобаны екі бөлек орынға жариялаймыз:
- **`index.html` + `assets/`** — GitHub Pages-те (статикалық сайт, тегін, тұрақты)
- **`telegram-bot.py`** — Railway-де (форманы Telegram-ге жіберетін backend, тегін тарифпен)

## 1. Telegram BOT_TOKEN алу

1. Telegram-да [@BotFather](https://t.me/BotFather)-ге кіріңіз.
2. `/newbot` командасын жіберіп, боттың атын және юзернеймін енгізіңіз.
3. BotFather сізге токен береді, мысалы: `123456789:AAExxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

## 2. CHAT_ID алу

1. Жаңа ботпен диалог ашып, оған кез келген хабарлама (мыс. `/start`) жіберіңіз.
2. Браузерде мына сілтеманы ашыңыз (TOKEN орнына өз токеніңізді қойыңыз):
   `https://api.telegram.org/bot<TOKEN>/getUpdates`
3. Жауаптан `"chat":{"id": ...}` мәнін тауып алыңыз — бұл сіздің `CHAT_ID`.

> Кеңес: хабарламалар компанияның топ-чатына келуін қаласаңыз, ботты сол топқа қосып, топтың chat_id-ін (әдетте теріс сан, мыс. `-1001234567890`) пайдаланыңыз.

**Маңызды:** `BOT_TOKEN` мен `CHAT_ID` енді кодта жазылмайды — `telegram-bot.py` оларды `os.environ`-нан оқиды. Себебі репозиторий GitHub-та ашық (public) тұрады, ал токенді ешқашан кодпен бірге жариялауға болмайды.

## 3. Backend-ті Railway-де іске қосу

1. [railway.app](https://railway.app) сайтына GitHub аккаунтпен кіріңіз
2. "New Project" → "Deploy from GitHub repo" → осы репозиторийді таңдаңыз
3. Railway `requirements.txt` пен `Procfile`-ды автоматты танып, деплой бастайды
4. Жоба ішінде **Variables** бөліміне өтіп, қосыңыз:
   - `BOT_TOKEN` = @BotFather-ден алған токен
   - `CHAT_ID` = 2-қадамдағы chat ID
5. Deploy аяқталған соң Railway сізге тұрақты URL береді (мыс. `https://alem-trans-bot.up.railway.app`)

Жергілікті түрде тексеру керек болса:
```bash
cd "Айеке контейнеравоз"
pip install -r requirements.txt
BOT_TOKEN=... CHAT_ID=... python telegram-bot.py
```

## 4. index.html-ды backend-пен байланыстыру

`index.html` файлындағы `<script>` соңында мына жолды тауып алыңыз:

```js
var API_URL = '/api/order';
```

Railway-ден алған нақты URL-ге ауыстырыңыз:
```js
var API_URL = 'https://alem-trans-bot.up.railway.app/api/order';
```

## 5. Сайтты GitHub Pages-те жариялау

1. GitHub репозиторийінің **Settings → Pages** бөліміне өтіңіз
2. Source: "Deploy from a branch", Branch: `main`, Folder: `/ (root)`
3. Сақтаңыз — бірнеше минуттан кейін сайт мына мекенжайда пайда болады:
   `https://<github-username>.github.io/<repo-name>/`
4. Меншікті домен (мыс. alemtrans.kz) қосу үшін: Pages бөліміндегі "Custom domain" өрісіне доменді жазып, домен провайдеріңізде CNAME/A жазбаларын GitHub нұсқауы бойынша қосыңыз

## 6. Тексеру

1. GitHub Pages сілтемесін ашыңыз
2. "Өтінім қалдыру" формасын толтырып жіберіңіз
3. Telegram-да ботыңыздан (немесе топтан) жаңа хабарлама келгенін тексеріңіз
4. Хабарлама келмесе — Railway жобасының "Deployments → Logs" бөлімін қараңыз (BOT_TOKEN/CHAT_ID дұрыс орнатылғанын тексеріңіз)

## Ауыстыру қажет орындар тізімі

| Орын | Не істеу керек |
|------|--------------------|
| Railway → Variables | `BOT_TOKEN`, `CHAT_ID` қосу |
| `index.html` | `API_URL`-ді Railway URL-іне ауыстыру |
| `robots.txt`, `sitemap.xml`, `index.html` (canonical/og/schema) | `alemtrans.kz` орынбасарын нақты доменге (немесе GitHub Pages URL-іне) ауыстыру |
| `index.html` | Телефон/WhatsApp/email өзгерсе — барлық `+77015448182` және `erbol.kts@mail.ru` кездесулерін ауыстыру |
| `assets/` | Жаңа фото қосу үшін файлдарды қосып, `index.html`-дағы галерея блогына сурет тегін қосу |
