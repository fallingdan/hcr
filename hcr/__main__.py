import argparse
import google.generativeai as genai
import os

def main():
    api_key = os.environ['GOOGLE_GENAI_KEY']
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("models/gemini-1.5-flash")
    
    route_name = input("Enter route name: ")
    route_crag = input("Enter name of crag route is in: ")
    route_description = input("Enter description for the route: ")

    prompt = f"""
    You are a rock climber who enjoys coming up with an extra goal to complete while climbing a route. You use the name of the route, 
    the name of the wall the route is on, and the description of the route in order to come up with the extra goal. The extra goal is
    intended to be humorous, but doable. Focus on a single action that is done at the top of the route. This extra goal is referred to as a gold star.

    Example Gold Star Goal:
    On a route named "Cotton Candy" at the "The Walls of Controversy", you gain a gold star for bringing cotton candy with you to the top,
    and eating some once you complete the route.
    
    Take the information below and respond with a gold star goal for the route given the route name, wall name, and its description.
    Route Name: {route_name}
    Wall Name: {route_crag}
    Route Description: {route_description}
    """
    result = model.generate_content(prompt)

    print(f"\n{result.text}\n")

if __name__ == "__main__":
    main()