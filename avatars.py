from PIL import Image
from random import randint

# Assets - https://www.figma.com/community/file/881358461963645496

RESIZE_TO = (1024, 1024)

background_id = randint(1, 8)
face_id = randint(1, 8)
facial_id = randint(0, 14)
smile_id = randint(1, 8)
eye_id = randint(1, 8)
hair_id = randint(1, 15)

# Background
image = Image.open(f'avatars/background/{background_id}.png')

# Face
face = Image.open(f'avatars/faces/{face_id}.png')
image.paste(face, (287, 249), face)

# Facial hair
if (facial_id > 10):
    facial = Image.open(f'avatars/facials/{facial_id-10}.png')
    image.paste(facial, (248, 181), facial)

# Smile
smile = Image.open(f'avatars/smiles/{smile_id}.png')
image.paste(smile, (247, 177), smile)

# Eye
eye = Image.open(f'avatars/eyes/{eye_id}.png')
image.paste(eye, (247, 177), eye)

# Hair
hair = Image.open(f'avatars/hairs/{hair_id}.png')
if hair_id == 6: image.paste(hair, (247, 138), hair)
else: image.paste(hair, (247, 177), hair)

image = image.convert('RGB')
image = image.resize(RESIZE_TO, resample=Image.Resampling.BOX)
image.save(f'image.png')
image.show()
