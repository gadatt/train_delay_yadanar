from train_delay.models import TrainInfo

def create_single_text_message(message):
    for objects in TrainInfo.objects.all():
        if message==objects.operator_en:
            message=''
            for operator_en in TrainInfo.objects.filter(operator_en = objects.operator_en):
                message+= operator_en.railway_en + ' : '+ objects.information_en + '\n'
        
            test_message=[
                {
                    'type' : 'text',
                    'text' : message
                }
                ]
            return test_message
                    