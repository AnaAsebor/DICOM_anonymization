# DICOM_anonymization
Python script for anonymization of images in DICOM format.  

This script is intended to serve as a tool for anonymizing DICOM (Digital Imaging and Communications in Medicine) format images using the pydicom library from a specific directory. 

DICOM images contain information about both the medical image itself and the associated metadata. This includes data such as patient identification, study type, date and time of acquisition, image settings, and other clinical details. The DICOM format is crucial to ensure that medical information is managed and shared effectively, maintaining the integrity and security of the data.  

This basic script is tailored to the needs of my project, but it can serve as a foundation for the development of a script customized to your requirements.



### How to use:

1. Previous requirements:  

Make sure you have the pydicom library installed in your Python environment. You can install it using the following command:

```python  
pip install pydicom    
```




2. Directory Configuration:

Defines the path of the directory containing the DICOM files in the path variable at the beginning of the script.

3. Script Execution:

Run the provided script in your Python environment.

### Principal functions  

1. Route Extraction:

The extract_paths function loops through the specified directory and extracts the full paths of each DICOM file in the directory.  

2. Deleting "Dose Report" Files:

The is_doseinf function checks if a DICOM file has the serial description "Dose Report". If so, the file is removed from the directory. (This file is attached to the imaging study, but is not relevant to their assessment and contains printed patient data that cannot be anonymized. You can assess if in your case you do not need to do this step.)

3. Anonymization of Patient Data:

The anonymize function checks if a DICOM file has the attributes PatientName, PatientID, PatientBirthDate, and PatientSex. If these attributes are present, the patient data is anonymized and the file is saved with the changes.  

### Results  

- During execution, informational messages are provided in the console indicating actions taken, such as deleting files and anonymizing patient data.

### Contributions and Problems 

- If you encounter issues or want to contribute to the project, feel free to open an issue or submit a pull request. All contributions are welcome!