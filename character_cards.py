from core.schema import Schema
from data.source import OnlineSource
from elements.text import TextElement
from elements.rect import RectElement
from elements.conditional import ConditionalElement
from core.alignment import *
from core.geometry import Point
from core.scaling import PARENT
from core.color import Color


src = OnlineSource('https://docs.google.com/spreadsheets/d/e/2PACX-1vQd8e0poc7VR1-vKW3GnrVuywCL0IHOHAMfUpW3m90ctsUOgClQL04NuzVUNid8Q5Cb9PwjGT5hXPdt/pub?gid=1442076058&single=true&output=csv')
schema = Schema(
    naming='characters/$name$',
    elements=[
        # Title
        TextElement(
            text='$name$', 
            font_path='squealer', 
            fill='blue',
            font_size=60,
            offset=Point(0, 50),
            alignment=TopCenter
        ),

        # Underline
        RectElement(
            fill='blue',
            alignment=TopCenter,
            size=Point(PARENT - 80, 1),
            offset=Point(0, 120)
        ),

        # Domains
        RectElement(
            fill='white',
            alignment=TopCenter,
            size=Point(PARENT - 80, 40),
            offset=Point(0, 120),
            children=[
                TextElement(
                    text='$title$',
                    font_path='alegreya_italic',
                    font_size=30,
                    fill='black',
                    alignment=TopCenter,
                    offset=Point(0, 0),
                ),
            ]
        ).make_invisible(),

        # Effect
        RectElement(
            fill='white',
            alignment=TopCenter,
            size=Point(PARENT - 80, PARENT - 150),
            offset=Point(0, 180),
            children=[
                TextElement(
                    text='<bold>Skills:</bold> $skills$ <br> <br> <br> <bold>Domains:</bold> $domains$',
                    font_path='alegreya',
                    fill='black',
                    font_size=40,
                    alignment=TopLeft,
                    line_spacing=10,
                ),
            ]
        ).make_invisible()
    ]
)
schema.process(src)