import os
import re
import telebot
from telebot import types

BOT_TOKEN = re.sub(r"\s+", "", os.environ["TELEGRAM_BOT_TOKEN"])
WEB_APP_URL = os.environ.get("WEB_APP_URL", "")

bot = telebot.TeleBot(BOT_TOKEN)

bot.set_chat_menu_button(menu_button=types.MenuButtonWebApp(text="Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL)))

# ============================================
# SCREEN 1 — START
# ============================================
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn_open = types.InlineKeyboardButton(text="📰 Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL))
    btn_headlines = types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines")
    btn_summary = types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario")
    markup.add(btn_open)
    markup.row(btn_headlines, btn_summary)

    text = (
        "📰 *Benvenuti su Rai News.*\n\n"
        "_«L'informazione è un diritto di tutti.»_\n\n"
        "Dal *1954*, la Rai accompagna gli italiani con informazione, "
        "cultura e intrattenimento. Oggi anche qui su Telegram. "
        "Ogni stagione una piccola selezione di cultura, viaggi, "
        "cucina, scienza e sport, da leggere in chat con calma.\n\n"
        "Per cominciare, toccate *I titoli del giorno*."
    )

    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 2 — HEADLINES
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "headlines")
def headlines(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton(text="🎨 Cultura — mostre d'autunno", callback_data="culture"),
        types.InlineKeyboardButton(text="🍝 Cucina — ricette regionali", callback_data="cuisine"),
        types.InlineKeyboardButton(text="🏠 Viaggi — cinque borghi", callback_data="travel"),
        types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario")
    )

    text = (
        "📋 *I titoli del giorno*\n\n"
        "Tre letture scelte per oggi. Ognuna leggibile per intero in chat.\n\n"
        "*Cultura* — mostre d'autunno: cinque appuntamenti da non perdere "
        "nei musei italiani.\n\n"
        "*Cucina* — ricette regionali: quattro piatti classici della "
        "tradizione italiana.\n\n"
        "*Viaggi* — cinque borghi italiani da scoprire nei fine settimana "
        "d'autunno.\n\n"
        "Toccate un titolo per aprire l'articolo completo."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 3 — CULTURE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "culture")
def culture(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="📰 Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    markup.row(types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"))

    text = (
        "🎨 *Mostre d'autunno: cinque appuntamenti nei musei italiani*\n\n"
        "I musei riaprono con la nuova stagione. Cinque appuntamenti "
        "che meritano attenzione questo autunno.\n\n"
        "*Roma — arte del Novecento*\n"
        "Una grande retrospettiva presso una delle gallerie nazionali "
        "raccoglie opere di alcuni fra i maggiori pittori italiani "
        "del secolo scorso. Accanto ai dipinti, materiali d'archivio "
        "e fotografie inedite.\n\n"
        "*Milano — design e industria*\n"
        "Una mostra dedicata al design industriale italiano ripercorre "
        "sessant'anni di oggetti quotidiani, dalla lampada da tavolo "
        "alla macchina da scrivere. Catalogo particolarmente curato.\n\n"
        "*Firenze — disegno rinascimentale*\n"
        "Fogli e taccuini di grandi maestri esposti in dialogo con "
        "opere contemporanee ispirate alla stessa tradizione. "
        "Occasione rara per vedere disegni normalmente conservati "
        "in deposito.\n\n"
        "*Napoli — fotografia del secondo dopoguerra*\n"
        "Un percorso di reportage in bianco e nero racconta la città "
        "e il Sud negli anni della ricostruzione. Sguardo empatico "
        "e documentario insieme.\n\n"
        "*Torino — scultura contemporanea*\n"
        "Il museo cittadino ospita nuove installazioni negli spazi "
        "aperti del parco. Le opere, dedicate al tema dell'acqua, "
        "dialogano particolarmente bene con la luce d'autunno.\n\n"
        "_Date e orari vanno verificati sui siti ufficiali dei musei._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 4 — CUISINE
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "cuisine")
def cuisine(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="📰 Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    markup.row(types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"))

    text = (
        "🍝 *Ricette regionali: quattro piatti classici*\n\n"
        "La cucina italiana è un patrimonio di sapori regionali. "
        "Quattro ricette per riscoprire la tradizione.\n\n"
        "*Cacio e pepe (Lazio)*\n"
        "Tonnarelli, pecorino romano e pepe nero. La semplicità "
        "che richiede maestria: la crema si ottiene amalgamando "
        "il formaggio con l'acqua di cottura. Nient'altro.\n\n"
        "*Pesto alla genovese (Liguria)*\n"
        "Basilico di Prà, pinoli, aglio, parmigiano, pecorino "
        "e olio extravergine. Pestato nel mortaio, mai frullato. "
        "Servire con trofie o trenette.\n\n"
        "*Arancini (Sicilia)*\n"
        "Riso al ragù, impanato e fritto. La forma cambia da città "
        "a città — tonda a Palermo, a punta a Catania. Il cuore "
        "di mozzarella filante è obbligatorio.\n\n"
        "*Ribollita (Toscana)*\n"
        "Zuppa di pane raffermo, cavolo nero, fagioli cannellini "
        "e verdure dell'orto. Si prepara il giorno prima e si "
        "ribollisce — da qui il nome. Comfort food toscano.\n\n"
        "_Dosi e tempi si adattano al gusto personale e ai prodotti di stagione._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 5 — TRAVEL
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "travel")
def travel(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="📰 Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    markup.row(types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines"), types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"))

    text = (
        "🏠 *Cinque borghi italiani per l'autunno*\n\n"
        "Lontano dalle mete più affollate, cinque piccoli borghi "
        "che in autunno mostrano il loro lato migliore.\n\n"
        "*Civita di Bagnoregio (Lazio)*\n"
        "Il borgo sospeso sul tufo raggiunto solo tramite un lungo "
        "ponte pedonale. Le luci d'autunno accentuano i colori della "
        "roccia; meglio visitarlo in un giorno feriale.\n\n"
        "*Bobbio (Emilia-Romagna)*\n"
        "Sull'antica via Francigena, con la sua abbazia e il ponte "
        "medievale detto \"del diavolo\". Osterie tranquille per "
        "una sosta di mezza giornata.\n\n"
        "*Volpaia (Toscana)*\n"
        "Piccolo borgo del Chianti, quasi interamente restaurato. "
        "Le vigne intorno cambiano colore in fretta e le cantine "
        "offrono degustazioni discrete.\n\n"
        "*Castelmezzano (Basilicata)*\n"
        "Fra le Dolomiti Lucane, con le case appoggiate a picchi "
        "di roccia. Sentieri di crinale per gli amanti del trekking; "
        "ottima cucina montana.\n\n"
        "*Erice (Sicilia)*\n"
        "Sospeso in alto sul mare, spesso avvolto nella nebbia "
        "autunnale. Pasticcerie storiche, chiese normanne e vicoli "
        "lastricati; una tappa che rimane a lungo nella memoria.\n\n"
        "_Per il pernottamento si consiglia la prenotazione infrasettimanale._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 6 — SOMMARIO
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "sommario")
def sommario(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="📰 Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    markup.add(types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines"))
    markup.row(types.InlineKeyboardButton(text="📖 Glossario", callback_data="glossario"), types.InlineKeyboardButton(text="❓ Domande frequenti", callback_data="faq"))
    markup.row(types.InlineKeyboardButton(text="✏️ Contatti redazione", callback_data="contact"), types.InlineKeyboardButton(text="🏛 Su Rai News", callback_data="about"))

    text = (
        "🏛 *Sommario*\n\n"
        "Da questo menu potete:\n\n"
        "• Leggere *i titoli del giorno* e i nostri articoli, "
        "direttamente qui.\n"
        "• Consultare le rubriche: Cultura, Viaggi, Cucina, "
        "Scienza, Sport, Economia pratica.\n"
        "• Sfogliare il glossario e le domande frequenti.\n"
        "• Conoscere la storia di Rai News e contattare la redazione.\n\n"
        "Per l'edizione integrale, usate il pulsante di apertura qui sotto."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 7 — GLOSSARIO
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "glossario")
def glossario(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"))

    text = (
        "📖 *Piccolo glossario*\n\n"
        "Alcuni termini ricorrenti in queste rubriche:\n\n"
        "*Redazione* — squadra che raccoglie, seleziona e prepara "
        "i testi per la pubblicazione.\n\n"
        "*Fondo* — articolo di riflessione, spesso firmato, che apre "
        "una sezione o una pagina.\n\n"
        "*Fotoreportage* — servizio giornalistico costruito attorno "
        "a una serie di fotografie.\n\n"
        "*Contenuto evergreen* — testo la cui attualità non dipende "
        "da una notizia del giorno: cultura, viaggi, cucina.\n\n"
        "*Inviato* — giornalista che raccoglie notizie sul campo.\n\n"
        "*Rubrica* — sezione ricorrente del giornale dedicata a un "
        "tema specifico.\n\n"
        "_Termini usati secondo l'uso corrente del giornalismo italiano._"
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 8 — FAQ
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "faq")
def faq(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text="📋 I titoli del giorno", callback_data="headlines"))
    markup.add(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"))

    text = (
        "❓ *Domande frequenti*\n\n"
        "*Questo bot è ufficiale?*\n"
        "Questa versione Telegram permette di leggere in chat "
        "i contenuti evergreen di Rai News. L'attività editoriale "
        "è curata dalla redazione; i contatti sono nella sezione "
        "Contatti redazione.\n\n"
        "*Con che frequenza si aggiorna?*\n"
        "La selezione in chat viene rinnovata stagionalmente. "
        "Per l'edizione aggiornata usate il pulsante di apertura.\n\n"
        "*Come si silenziano le notifiche?*\n"
        "Dalle impostazioni della chat Telegram potete silenziare "
        "le notifiche di questo bot o disattivarle del tutto.\n\n"
        "*Posso condividere un articolo?*\n"
        "Sì. Usate le opzioni di condivisione integrate in Telegram "
        "per inoltrare il messaggio in un'altra chat o in un'app esterna."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 9 — CONTACT
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "contact")
def contact(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.row(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"), types.InlineKeyboardButton(text="🏛 Su Rai News", callback_data="about"))

    text = (
        "✏️ *Contatti redazione*\n\n"
        "Per la corrispondenza editoriale:\n"
        "• E-mail: rainews@rai.it\n"
        "• Servizio telespettatori: rai.it/contatti\n\n"
        "*Editore*\n"
        "Rai — Radiotelevisione Italiana S.p.A.\n"
        "Viale Mazzini, 14\n"
        "00195 Roma\n"
        "Italia\n\n"
        "Segnalazioni, diritti di replica e osservazioni dei lettori "
        "sono gestiti dal servizio telespettatori nei giorni lavorativi."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# SCREEN 10 — ABOUT
# ============================================
@bot.callback_query_handler(func=lambda call: call.data == "about")
def about(call):
    bot.answer_callback_query(call.id)
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton(text="📰 Apri Rai News", web_app=types.WebAppInfo(url=WEB_APP_URL)))
    markup.row(types.InlineKeyboardButton(text="🏛 Sommario", callback_data="sommario"), types.InlineKeyboardButton(text="✏️ Contatti", callback_data="contact"))

    text = (
        "🏛 *Su Rai News*\n\n"
        "_Rai News_ è il canale all-news della Rai, la radiotelevisione "
        "pubblica italiana. Nata nel *1954*, la Rai è la più grande "
        "azienda culturale italiana e una delle più importanti in Europa.\n\n"
        "Rai News 24 trasmette notizie 24 ore su 24 dal *1999*, "
        "offrendo copertura nazionale e internazionale su politica, "
        "economia, cultura, sport e cronaca.\n\n"
        "Tra televisione, radio, sito web e applicazioni mobili, "
        "la Rai raggiunge quotidianamente milioni di italiani. "
        "La sede principale è a Roma; il sito è rainews.it.\n\n"
        "Questa versione Telegram è pensata per rendere più comoda "
        "la lettura dei contenuti evergreen dall'interfaccia di chat."
    )

    bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=markup)


# ============================================
# RUN
# ============================================
print("Rai News Bot is running...")
bot.infinity_polling()
