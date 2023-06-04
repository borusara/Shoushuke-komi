from Messi import dispatcher
from Messi import Update
from Messi.ext import CallbackContext
from Messi.modules.helper_funcs.decorators import Messi

@register(command='shout')
def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = [" ".join(list(text))]
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")
