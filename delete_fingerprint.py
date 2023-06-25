from pyfingerprint.pyfingerprint import PyFingerprint
from VARIABLES import (
    FINGERPRINT_DEVICE_PORT,
    FINGERPRINT_BAUD_RATE,
    FINGERPRINT_ADDRESS,
    FINGERPRINT_PASSWORD,
)

## Deletes a finger from sensor
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

## Tries to delete the template of the finger
try:
    positionNumber = input("Please enter the template position you want to delete: ")
    positionNumber = int(positionNumber)

    if f.deleteTemplate(positionNumber) == True:
        print("Template deleted!")

except Exception as e:
    print("Operation failed!")
    print("Exception message: " + str(e))
    exit(1)
