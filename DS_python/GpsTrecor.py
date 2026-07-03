data={
    "surat":["left","left","right","left","right","right"],
    "ahmedabad":["left","right","left","right","left","right"],
    "vadodara":["right","left","right","left","right","left"],
}
city=input("where u want to go? Enter the city name: ")
if city in data:
    for i in range(len(data[city])):
        path=input(f"Enter the path for {city} (left/right): ")
        if path != data[city][i]:
            print("Go Back.")
            break
    else:
        print("You reached", city)
else:
    print("City not found.")