import requests
import json

def make_supabase_api_call():
    """
    Make a GET request to Supabase API to fetch password of account with username 'admin'
    """
    
    # API endpoint
    url = "https://dpyxnwiuwzahkxuxrojp.supabase.co/rest/v1/users"
    
    # Query parameters
    params = {
        "select": "password",
        "username": "eq.admin"
    }
    
    # Headers
    headers = {
        "apikey": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRweXhud2l1d3phaGt4dXhyb2pwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3NjA1MDcsImV4cCI6MjA2NzMzNjUwN30.C3-ninSkfw0RF3ZHJd25MpncuBdEVUmWpMLZgPZ-rqI",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRweXhud2l1d3phaGt4dXhyb2pwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTE3NjA1MDcsImV4cCI6MjA2NzMzNjUwN30.C3-ninSkfw0RF3ZHJd25MpncuBdEVUmWpMLZgPZ-rqI"
    }
    
    try:
        # Make the GET request
        response = requests.get(url, params=params, headers=headers)
        
        # Return parsed JSON if successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

if __name__ == "__main__":
    result = make_supabase_api_call()
    if result:
        print(result[0].get("password"))
