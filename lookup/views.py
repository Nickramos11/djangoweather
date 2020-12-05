from django.shortcuts import render

def hom3(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=D222E436-5937-4950-A050-2ACA0EB81BA4")
        
        try:
            # calling json to load content from above var
            api = json.loads(api_request.content)

            if api[0]['Category']['Name'] == "Good":
                category_description = "Good: (0-50) Air quality is satisfactory, and air pollution poses little or no risk."
                category_color = "good"

            elif api[0]['Category']['Name'] == "Moderate": 
                category_description = "Moderate: (51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
                category_color = "moderate"

            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
                category_description = "Unhealthy for Sensitive Groups: (101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
                category_color = "unhealthyforsensitivegroups"
        
            elif api[0]['Category']['Name'] == "Unhealthy":
                category_description = "Unhealthy: (151-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
                category_color = "unhealthy"
        
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "Very Unhealthy: (201-300) Health alert: The risk of health effects is increased for everyone."
                category_color = "veryunhealthy"

            elif api[0]['Category']['Name'] == "Very Unhealthy": 
                category_description = "Hazardous: (301+) Health warning of emergency conditions: everyone is more likely to be affected."
                category_color = "hazardous"

        except Exception as e:
            api = "Error..."
            category_description = "Error..."
            category_color = "hazardous"

        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color})


    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=85001&distance=25&API_KEY=D222E436-5937-4950-A050-2ACA0EB81BA4")
        
        try:
            # calling json to load content from above var
            api = json.loads(api_request.content)
            
            if api[0]['Category']['Name'] == "Good":
                category_description = "Good: (0-50) Air quality is satisfactory, and air pollution poses little or no risk."
                category_color = "good"

            elif api[0]['Category']['Name'] == "Moderate": 
                category_description = "Moderate: (51-100) Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
                category_color = "moderate"

            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups": 
                category_description = "Unhealthy for Sensitive Groups: (101-150) Members of sensitive groups may experience health effects. The general public is less likely to be affected."
                category_color = "unhealthyforsensitivegroups"
        
            elif api[0]['Category']['Name'] == "Unhealthy":
                category_description = "Unhealthy: (151-200) Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
                category_color = "unhealthy"
        
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_description = "Very Unhealthy: (201-300) Health alert: The risk of health effects is increased for everyone."
                category_color = "veryunhealthy"

            elif api[0]['Category']['Name'] == "Very Unhealthy": 
                category_description = "Hazardous: (301+) Health warning of emergency conditions: everyone is more likely to be affected."
                category_color = "hazardous"

        except Exception as e:
            api = "Error..."
            category_description = "Error..."
            category_color = "hazardous"

        
        return render(request, 'home.html', {
            'api': api,
            'category_description': category_description,
            'category_color': category_color})

def about(request):
    return render(request, 'about.html', {})