# hackathon_power_to_fly
## **OCR Personal Information Identification System Summarized Report()**
# **FrontEnd**
-	The identification the function is displayed showing the title of the event, “Hackathon”
-	Subheading is also initialized below the title 
-	The use of OCR and the relevant system is displayed 
-	Functionalities to drag and drop different formats or browse through your files to upload has been given.
# **BackEnd**
- After the user uploads, the image is opened by the system and converted into an array (num pi)
- The image is opened in the back end and if the system sees anything in the English language, it is separated and stored into different variables
-	Only English will be ready by the system
-	System will look for the text in the image using the array
-	The resulting image will be provided
-	A separate font has been initialized for the output
-	Dimensions of the text in different areas of the image or document are identified
-	Whatever text is received by the OCR PIIS system is displayed in green on top of the original image
-	Green boxes are placed on the image to identify the parts recognized by the the system
-	We gave the system some reliance on types of personal information, for example: whatever text is extracted from the image or documents contain the keywords “Master card” , “Visa” , “Username:”, “ ID:” ,”Name:” etc.
-	The extracted text is taken and formatted into lowercase
-	Or function is used to display a warning “ Personal information identified” in case of any of keywords indicating that the information might be personal 
## **Team**

1. Muhammad Owais 2. Irfan Ali 3. Subhan Farooq 4. Rahat Ali
