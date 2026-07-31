def BMI(weight, height):

    return weight/(height**2)

def get_bmi_category(bmi):
  d={ 
    'Underweight': 18.5,
    'normal': 24.9,
    'overweight':29.9,
    'obese': float('inf')

  }
  if bmi < d['Underweight'] :  
        return"UW"
  elif d['Underweight'] <= bmi <=d['normal']:
       return"healthy"
  elif d['normal'] <= bmi <=d['overweight']:
       return"Over weight"
  else:
       return 'obese'
    

def main():
  height = float(input("Type your height in "))
  weight = float(input("Type your weight in "))
  n= BMI(weight, height) 
  category = get_bmi_category(n)
  print(category)

     








