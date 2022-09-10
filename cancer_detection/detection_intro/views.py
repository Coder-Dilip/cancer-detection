from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Prediction
from cancer_detection import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,'detection_intro/index.html')

def prediction(request):
    return render(request,'detection_intro/prediction.html')

@csrf_exempt
def predict(request):
    # if request.method=='POST':
        import tensorflow as tf
        import cv2
        model = tf.keras.models.load_model('my_model.h5')
        imagePrediction=Prediction()
        imagePrediction.image = request.FILES.get('image')
        imagePrediction.save()
        # print(model.summary())
        cancer_data=Prediction.objects.last()
        test_paths=[str(settings.BASE_DIR)+str(cancer_data.image.url)]
        x_test=[]
        for el in test_paths:
            x_test.append(cv2.resize(cv2.imread(el, cv2.IMREAD_UNCHANGED),(150,150), interpolation = cv2.INTER_AREA))
        x_tests=tf.convert_to_tensor(x_test,dtype='float32')
        predictions=model.predict(x_tests)
        print(predictions[0][0])
        return JsonResponse({'msg':'Oops that is Cancerous tumor'} if predictions[0][0]>=0.5 else {'msg':"Congrats! your skin is not Cancerous"})