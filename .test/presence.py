from pypresence import Presence
from time import time
RPC = Presence("1008645854426583090")
btns = [
    {
        "label": "⚡DiscordServer⚡",
        "url": "https://bit.ly/3RIIn5Q"
    },
    # Допоснительная кнопка, можете изменить и добавить)
    #{
    #    "label": "‍💻GitHub💻",
    #   "url": "https://github.com/mrf0rtuna4"
    #}
]
RPC.connect()
RPC.update(
    state="Minecraft server",
    details="Игра в сюжет",
    start=time(),
    buttons=btns,
    large_image="1",
    small_image="mrf",
    large_text="Heypers Laboratory",
    small_text="Владелец сервера"
)
input()
