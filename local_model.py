from transformers import pipeline


generator = pipeline("text-generation", model="distilgpt2")

def generate_local_itinerary(name, present, destination, interests, dates, budget):
    prompt = (
        f"Plan a trip for {name} from {present} to {destination} on {dates} "
        f"with a budget of {budget}. Interests include: {interests}. Day 1:"
    )
    result = generator(prompt, max_length=500, do_sample=True, top_k=50)[0]["generated_text"]
    return result
