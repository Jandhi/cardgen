from font_atlas import transformation_tags, transformations, paths

CONDENSED = 'Condensed'
SEMICONDENSED = 'SemiCondensed'

path = 'Open Sans/OpenSans'

WEIGHTS = ['Light', 'Regular', 'Medium', 'SemiBold', 'Bold', 'ExtraBold']
DENSITIES = ['', f'_{SEMICONDENSED}', f'_{CONDENSED}']

for weight in WEIGHTS:
    for density in DENSITIES:
        for is_italic in (True, False):
            full_path = f'{path}{density}-{weight}'
            
            name = 'opensans'

            if density != '':
                name += density.lower()

            if weight != 'Regular':
                name += f'_{weight.lower()}'

            if is_italic:
                name += '_italic'

            if is_italic:
                full_path += 'Italic'

            full_path += '.ttf'

            if full_path.endswith('RegularItalic'):
                full_path = full_path.replace('Regular', '')

            paths[name] = full_path