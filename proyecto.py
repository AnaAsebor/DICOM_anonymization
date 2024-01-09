import pydicom as pm
import os

path = r'C:\Users\fat\Documents\NEUROVASCULAR\BIOSHIP_anonymous\B-HUVM-438'

#Function to extract the paths of each image:

def extract_paths(folder):
    paths = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            complete_path = os.path.join(root, file)
            paths.append(complete_path)
    return paths

#Function that checks if the file is the "Informe de Dosis" and deletes it:

def is_doseinf(path_image):
    try:
        # Try to load the DICOM file:
        dicom_file = pm.dcmread(path_image)

        # Checks if it is a DICOM object that has the 'PatientName' attribute:
        if hasattr(dicom_file, 'SeriesDescription') and dicom_file.SeriesDescription == 'Informe de Dosis':
            print(f"{path_image} is a DICOM file. Series Description: {dicom_file.SeriesDescription}")
            os.remove(path_image)
            print('The file with "Informe de Dosis" was deleted')
            return True
        else:
            return False

    except Exception as e:
        # If there is an error uploading the file, it is not a DICOM file
        #print(f"{path_image} is not a DICOM file. Error: {e}")
        return False

#Function that checks if the file has the attributes: PatientName, PatientID, PatientBirthDate and PatientSex and then anonymizes them:

def anonymize(path_image):
    try:
        # Try to load the DICOM file
        dicom_file = pm.dcmread(path_image)

        # Checks if it is a DICOM object that has the 'PatientName' attribute
        if hasattr(dicom_file, 'PatientName'):
            print(f"{path_image} is a DICOM file. Data of patient: {dicom_file.PatientName, dicom_file.PatientID, dicom_file.PatientBirthDate, dicom_file.PatientSex}")
            dicom_file.PatientName = 'Anonymous'
            dicom_file.PatientID = '**********'
            dicom_file.PatientBirthDate = '********'
            dicom_file.PatientSex = '*'
            dicom_file.save_as(path_image)
            print(f"The image {path_image} has been anonymized: Name of patient: {dicom_file.PatientName}, patient ID: {dicom_file.PatientID}, patient birthdate: {dicom_file.PatientBirthDate}, patient sex: {dicom_file.PatientSex}")
            return True
        else:
            print(f"{path_image} is a DICOM file, but doesn't have the 'PatientName' attribute.")
            return False


    except Exception as e:
        # If there is an error uploading the file, it is not a DICOM file
        print(f"{path_image} is not a DICOM file. Error: {e}")
        return False

all_paths_images = extract_paths(path)

for path_image in all_paths_images:
    is_doseinf(path_image)
    anonymize(path_image)
