import google.generativeai as genai

genai.configure(api_key = 'AIzaSyDEIIdMaX1qY_qNDgJmRmkJLRVmXnudhjo')

model = genai.GenerativeModel('gemini-2.0-flash')

def generate_itinerary(name,present, destination, interests,dates,budget):
    prompt = f"""
    Create a travel itinerary on the dates {dates} for a user named {name} who wants to visit {destination} from 
    the current location {present} with a budget of {budget}.
    Their interests include: {interests}.
    The itinerary should include daily plans, attractions, local cuisine, and tips.
    """
    response = model.generate_content(prompt)
    return response.text
