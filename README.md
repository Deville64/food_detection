I developed a web application using the Django framework, incorporating a YOLOv8-based object detection solution.  
The primary goal was to start from scratch and engage in the entire process to enhance my learning.  
I employ AI for ingredient identification, automatically populating a recipe form with the detected ingredients.  
The app features user authentication, recipe management, and a user-friendly interface. Key phases included meticulous prototyping, data collection through web scraping, and model training with YOLOv8.  
I ensured code organization and database integrity, implemented monitoring using debug.log, and conducted unit tests for login functionality.  
Future enhancements could involve quantity detection, ingredient recommendations, and even voice recognition integration and of course more ingredient detection.  

# About AI

### Scrapping
I gathered data for my project by scraping images from Instagram and Google.   
Subsequently, I cleaned the dataset by eliminating duplicates, converting file formats, and renaming files, ensuring a standardized collection for effective model training.  


### Labeling
For labeling the collected data, I employed the LabelImg tool, streamlining the annotation process.  
This tool proved convenient as it supports the YOLO format, generating text files containing bounding box coordinates and corresponding labels.   
With careful annotation, I ensured precise bounding boxes around each object of interest, facilitating effective training and testing of my YOLOv8-based object detection model.  

### Data Visualization
After obtaining labeled images, I conducted data visualization to gain insights into ingredient distribution. Using a bar chart, I depicted the quantities of labeled ingredients, providing a clear overview of their prevalence in the dataset.   
This visualization step enhanced my understanding of the composition of the dataset, allowing for better-informed decisions during the model training process.  

### Data Organization for Model Training
To prepare the data for training, I organized it into distinct sets for optimal model learning.   
Utilizing 80% of the labeled data for training and allocating 10% each for testing and validation, I ensured a balanced distribution.   
This organization, along with a custom YAML file, facilitated seamless integration with the YOLOv8 model during the training phase.  

### Training
For training, I employed YOLOv8 and organized the labeled photos into distinct datasets for training, testing, and validation. Utilizing Google Colab with a GPU, I leveraged a pre-trained model for efficient transfer learning.  
The training process involved configuring parameters, such as image size and batch size, to optimize model performance.    
After 500 epochs, the model exhibited effective detection of ingredients, particularly eggs, demonstrating satisfactory Mean Average Precision (mAP) results.  
<br>Final result with object detection
<img src="https://github.com/Deville64/food_detection/assets/62333333/800c942f-5119-44e3-a6d7-39c13e81b836" width="800px">
<br>
<br>



# About the application

### User Interface Design and Integration. 
For the application design, I created a user-friendly interface using Django. The mockups included features for ingredient detection, recipe creation, and user authentication.  
The goal was to seamlessly integrate YOLOv8's object detection capabilities into a practical and visually intuitive web application, ensuring a smooth user experience.  
<img src="https://github.com/Deville64/food_detection/assets/62333333/3b1f83f1-75d1-4462-8654-53be3face38f" width="600" alt="Description de l'image">
<img src="https://github.com/Deville64/food_detection/assets/62333333/89c85811-469e-43f8-913e-0b6c572d9ea0" width="800px">


### Database Architecture and Design
I established a robust database structure using Django models, ensuring seamless storage and retrieval of recipe-related data.  
The database schema was carefully designed to accommodate ingredients, recipes, and user information, facilitating efficient data management within the application.  

