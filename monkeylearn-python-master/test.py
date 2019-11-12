from monkeylearn import MonkeyLearn
import json
ml = MonkeyLearn('7946ba4a43dc8c1f07b08b70a6007e97318c49ef')
data = ['Khoa is so handsome and stupid and weak and terrible']
model_id = 'cl_pi3C7JiL'
result = ml.classifiers.classify(model_id, data)
print(result.body)
