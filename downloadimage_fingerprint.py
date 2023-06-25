import tempfile
from pyfingerprint.pyfingerprint import PyFingerprint
from VARIABLES import (
    FINGERPRINT_DEVICE_PORT,
    FINGERPRINT_BAUD_RATE,
    FINGERPRINT_ADDRESS,
    FINGERPRINT_PASSWORD,
)

## Reads image and download it
##

## Tries to initialize the sensor
try:
    f = PyFingerprint(
        FINGERPRINT_DEVICE_PORT,
        FINGERPRINT_BAUD_RATE,
        FINGERPRINT_ADDRESS,
        FINGERPRINT_PASSWORD,
    )
    if f.verifyPassword() == False:
        raise ValueError("The given fingerprint sensor password is wrong!")

except Exception as e:
    print("The fingerprint sensor could not be initialized!")
    print("Exception message: " + str(e))
    exit(1)

## Gets some sensor information
print(
    "Currently used templates: "
    + str(f.getTemplateCount())
    + "/"
    + str(f.getStorageCapacity())
)

## Tries to read image and download it
try:
    print("Waiting for finger...")

    ## Wait that finger is read
    while f.readImage() == False:
        pass

    print("Downloading image (this take a while)...")

    imageDestination = tempfile.gettempdir() + "/fingerprint.bmp"
    f.downloadImage(imageDestination)

    print('The image was saved to "' + imageDestination + '".')

except Exception as e:
    print("Operation failed!")
    print("Exception message: " + str(e))
    exit(1)
