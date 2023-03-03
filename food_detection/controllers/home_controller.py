from django.shortcuts import render
from ultralytics import YOLO
from django.core.files.storage import FileSystemStorage
import uuid


def show_ingredients_check(request):
    if request.method == 'POST' and request.FILES['picture']:
        ingredients_list = []
        fs = FileSystemStorage()
        picture = request.FILES.get('picture')
        picture_name = str(uuid.uuid4()) + '.' + picture.name.split('.')[-1]
        fs.save('media/not_enrolled/' + picture_name, picture)

        model = YOLO("best.pt")
        results = model('media/not_enrolled/' + picture_name,
                        conf=0.8, show=False, save=False)

        for result in results:
            for ingredient_id in result.boxes.cls:
                if model.names[int(ingredient_id)] not in ingredients_list:
                    ingredients_list.append(model.names[int(ingredient_id)])

        request.session['ingredients_list'] = ingredients_list
        request.session['picture_path'] = 'media/not_enrolled/' + picture_name

        return render(request, 'views/home.html', {'ingredients_list': ingredients_list})

    else:
        return render(request, 'views/home.html')
