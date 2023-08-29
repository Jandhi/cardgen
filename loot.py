from core.schema import Schema
from core.geometry import Point
from data.source import OnlineSource, ManualSource
from elements.rect import RectElement
from elements.text import TextElement
from core.scaling import PARENT
from settings import Settings
from core.alignment import MiddleCenter

# load
import font_loaders.open_sans_loader

URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRCV1U8jK89yxbItQ5kS5_YpgP9b9T9vAULtqsY-6wAX4OR3OfjRa9RZWQ4tHFl8kkCo4JkZljib_vW/pub?gid=1294971844&single=true&output=csv'

Settings.CardsDirectory = 'out/loot/cards'
Settings.DecksDirectory = 'out/loot/decks'

schema = Schema(
    naming='$name$',
    elements=[
        RectElement(
            fill='white',
            offset=Point(0, PARENT * 0.5),
            size=Point(PARENT, PARENT * 0.5),
            children=[
                TextElement(
                    text='$effect$',
                    font_path='opensans',
                    fill='black',
                    font_size=50,
                    alignment=MiddleCenter,
                    max_icon_size=Point(1000, 1000),
                )
            ]
        ),
    ],
    count='$copies$',
)

src = OnlineSource(url=URL)

src=ManualSource(entries=[
    {
        'name' : 'Leather Armour',
        'cost' : '2',
        'type' : 'Chest',
        'copies' : '1',
        'effect' : '#open1to3 : 1 #shield'
    }
])

schema.process(src)