from fastapi import UploadFile
import numpy as np
from PIL import Image
import io

async def img_to_np_array(img_file: UploadFile):
    # Read the file content into a BytesIO object
    contents = await img_file.read()
    img_stream = io.BytesIO(contents)

    # Open the image file using PIL
    with Image.open(img_stream) as img:
        # Resize the image to (256, 192)
        img_resized = img.resize((192, 256))
        # img_resized = img.resize((256, 192))
        # Convert the image to a numpy array
        img_array = np.array(img_resized)

    # It's important to seek back to the start of the file for potential further use
    # img_file.file.seek(0)

    return img_array