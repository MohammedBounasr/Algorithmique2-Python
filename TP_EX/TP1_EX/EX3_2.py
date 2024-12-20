
seconds = int(input("Veuillez entrer le temps en secondes : "))

hours = seconds // 3600  
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60  
  

print(f"{hours} heures, {minutes} minutes et {remaining_seconds} secondes.")
