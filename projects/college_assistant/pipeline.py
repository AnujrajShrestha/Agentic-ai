from agentic import app

def run_pipeline(programme):
    print(f"\nGreat! You're set as a {programme} student.")

    while True:
        user_query= input("You: ")
        if user_query.lower() in ['exit','quit']:
            break
    
        result= app.invoke({
            'programme': programme,
            'messages': [("user",user_query)]
        })
    
        print(f"Assistant : {result['messages'][-1].content}")
        

if __name__=="__main__":
    print("Welcome to the College assistant \n\n")
    print("which programe are you in ")
    print("1. BCA")
    print("2. BBA")
    print("3. B.com (H)")

    choice= input("\nEnter 1,2 or 3: ")
    programme_map= {
        "1": "BCA",
        "2": "BBA",
        "3": "B.Com (H)"
    }
    student_programme = programme_map.get(choice, "BCA")
    run_pipeline(student_programme)