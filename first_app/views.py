from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from PIL import Image
import numpy as np
import os
from django.conf import settings
from .models import PredictionLog

# Create your views here.
def index(request):
    context = {'a':1}
    return render(request,'index.html',context)


def predict(request):
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage(location=settings.MEDIA_ROOT)  # Use media root
    filePathName = fs.save(fileObj.name, fileObj)
    filePath = fs.path(filePathName) 
    fileUrl = fs.url(filePathName)
    print("******************fileURl*****************:",fileUrl)
    
    model = tf.keras.models.load_model('./models/mnist_simple_cnn_10_Epochs.h5')
    
    # Load, Resize and Preprocess the Image
    img = Image.open(filePath).convert('L')  # Convert to grayscale
    img = img.resize((28, 28), Image.ANTIALIAS)  # Resize to 28x28
    img_arr = np.array(img) / 255.0  # Normalize
    img_arr = img_arr.reshape(1, 28, 28, 1)  # Reshape to match model input
    

    # Predict
    prediction = model.predict(img_arr)
    predicted_class = np.argmax(prediction, axis=-1)[0]
    
    log_entry = PredictionLog(
        request_data= fileObj.name,
        prediction_result=str(predicted_class)  # Assuming predicted_class is your prediction result
    )
    log_entry.save()

    context = {
        'predictedClass': predicted_class,
        'fileUrl': fileUrl
    }


    return render(request, 'index.html', context)
    