def total_trolley(request):
    total=200
    if 'trolley' in request.session:
        for key,value in request.session['trolley'].items():
            total= total +(float(value['price'])* value['amount'])
    return{'total_trolley': total}