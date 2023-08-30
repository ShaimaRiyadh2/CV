

class CV:
#A class to represent a curriculum vitae.

  def __init__(self, name):
    #Initializes the CV
    self.name = name
    self.skills = []
    self.educations = []
    self.experiences = []

  def add_skills(self):
    #Adds a skill to the CV
    skill = input("Enter your skills : ")
    percentage = input("Enter your Percentage : ")
    skill = Skill(skill, percentage)
    self.skills.append(skill)

  def add_education(self):
    #Adds an education to the CV
    degree = input("Enter your degree: ")
    institution = input ("Enter Name of institution that you studied in: ")
    completion_date = input ("Enter the completion_date:")
    education = Education(degree, institution, completion_date)
    self.educations.append(education)

  def add_experience(self):
    #Adds an experience to the CV
    company = input("Enter the company name: ")
    job_title = input("Enter the title of the your job: ")
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    experience = Experience(company, job_title, start_date, end_date)
    self.experiences.append(experience)

  def display_cv(self):
    #Displays the CV
    print("Name:", self.name)
    print("Skills:")
    for skill in self.skills:
      print(skill)
    print("Educations:")
    for education in self.educations:
      print(education)
    print("Experiences:")
    for experience in self.experiences:
      print(experience)


#------------------------------------------------

class Experience:
  #A class to represent an experience in a curriculum vitae

  def __init__(self, company, job_title, start_date, end_date):
    #Initializes the experience
    self.company = company
    self.job_title = job_title
    self.start_date = start_date
    self.end_date = end_date

  def display_experience(self):
    #Displays the experience
    print("Company:", self.company)
    print("Title:", self.job_title)
    print("Start date:", self.start_date)
    print("End date:", self.end_date)



class Education:
  #A class to represent an educational qualification

  def __init__(self, degree, institution, completion_date):
    """Initializes the education."""
    self.degree = degree
    self.institution = institution
    self.completion_date = completion_date

  def display_education(self):
    #Displays the education
    print("Degree:", self.degree)
    print("Institution:", self.institution)
    print("Completion date:", self.completion_date)
    


class Skill:
  #A class to represent a skill

  def __init__(self, skill, percentage):
    #Initializes the skill
    self.skill = skill
    self.percentage = percentage

  def display_skill(self):
    #Displays the skill
    print("Skill:", self.skill)
    print("Percentage:", self.percentage)




#------------------------------------------------

def main():
 #The main function
  name = input("Enter your name: ")

  cv = CV(name)

  while True:
    answer = input("Do you want to add skills? (y/n): ")
    if answer == "n":
      break
    cv.add_skills()

  while True:
    answer = input("Do you want to add education? (y/n): ")
    if answer == "n":
      break
    cv.add_education()

  while True:
    answer = input("Do you want to add experience? (y/n): ")
    if answer == "n":
      break
    cv.add_experience()

  cv.display_cv()



if __name__ == "__main__":
  main()

