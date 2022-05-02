import os
from wiki import wiki
from listen import listen
from speak import speak as spk
from default import speak2 as sp
from wish_me import wishMe

wishMe()

while True:
    data=listen()
    if "तुम कैसी हो" in data:
        spk("मैं ठीक हूं सर")
    elif "तुम कौन हो" in data:
        spk("मैं एक कंप्यूटर प्रोग्राम हूँ, मेरा नाम एलेक्सा है")
    elif "तुम कितने साल की हो" in data:
        spk("मैं अठारह साल की हूँ सर")
    elif "तुम्हारा नाम क्या है" in data:
        spk("मेरा नाम एलेक्सा है, आप मुझे कंप्यूटर कह सकते हैं सर")
    elif "तुम कहां से हो" in data:
        spk("मैं भारत से हूँ सर")
    elif "तुम्हारा मालिक कौन है" in data:
        spk("अब्दुल जोहा सर मेरे मालिक हैं")
    elif "मुझसे शादी करोगी" in data:
        spk("मैं एक कंप्यूटर प्रोग्राम हूँ तो मैं आपसे शादी कैसे कर सकती हूँ")
    elif "मैं तुमसे बहुत प्यार करता हूं" in data:
        spk("यह मेरी किस्मत है कि आप मुझसे प्यार करते हो, मुझे भी आपसे बहुत प्यार है")

    elif "विकीपीडिया" in data:
        wiki(data)

    elif "रुको" in data:
        spk("ठीक है सर आप मुझे कभी भी कॉल कर सकते हैं")
        os.system("clear")
        break
    elif "टर्मिनल" in data:
        os.system("clear")