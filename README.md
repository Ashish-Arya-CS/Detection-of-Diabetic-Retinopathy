# Detection-of-Diabetic-Retinopathy
  This is a model for detection of Diabetic Retinopathy.Diabetic retinopathy is a diabetes complication that affects eyes. It's caused by damage to the blood vessels of the light-sensitive tissue at the back of the eye (retina). At first, diabetic retinopathy may cause no symptoms or only mild vision problems.You might not have symptoms in the early stages of diabetic retinopathy. As the condition progresses, diabetic retinopathy symptoms may include:  Spots or dark strings floating in your vision (floaters), Blurred vision, Fluctuating vision, Impaired color vision, Dark or empty areas in your vision, Vision loss. Diabetic retinopathy usually affects both eyes.


![IMAGE](https://github.com/Ashish-Arya-CS/Detection-of-Diabetic-Retinopathy/blob/master/images/Difference-between-Normal-Retina-and-Diabetic-Retinopathy.png)

## The Model has been trained on Colab using a GPU Hardware Accelerator
  The Dataset was taken from Kaggle and here is the link for the [DATA](https://www.kaggle.com/sovitrath/diabetic-retinopathy-224x224-gaussian-filtered?).
  
## [DR Image processing](https://github.com/Ashish-Arya-CS/Detection-of-Diabetic-Retinopathy/blob/master/DR%20Image%20processing.ipynb) and [Power Transformation](https://github.com/Ashish-Arya-CS/Detection-of-Diabetic-Retinopathy/blob/master/Power%20Transformation.ipynb)
  Since,many features of the image were lost after applying Guassian Filters.So,these notebooks basically contains the image processing part which we did to restore the image and   since there was class imbalance in the dataset we also did some augmentations in the original data to balance our dataset.
  
## [DR 91.07% Accr](https://github.com/Ashish-Arya-CS/Detection-of-Diabetic-Retinopathy/blob/master/DR%2091.07%25%20Accr.ipynb)
  This conatins the main model trainig part and the accessing of Model Performance.
  
## [appstreamlit](https://github.com/Ashish-Arya-CS/Detection-of-Diabetic-Retinopathy/blob/master/appstreamlit.py)  
  This conatins the python executable file for our model deployment on a web app.For building the web app we have used Streamlit.
  
## [Web_App_Launcher](https://github.com/Ashish-Arya-CS/Detection-of-Diabetic-Retinopathy/blob/master/Web_App_Launcher.ipynb)  
  This contains the web app launcher notebook.
  
#### Since everything was done on Colab,so everything is in the format of .ipynb  
