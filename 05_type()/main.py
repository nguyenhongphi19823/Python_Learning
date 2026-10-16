#--------01--------------#

#--------02--------------#
print("Hello Automation")

#--------03--------------#
name = "Phi"
age = 25
is_tester = True

print(name)
print(age)
print(is_tester)


company = "ABC"
experience = 3
print(f"I work at {company} and I have {experience} years of experience")

#--------04--------------#
#--List--#
skills = ["manual", "api", "automation"]
print(skills[0])
#--Dictionary--#
user = {
    "username": "phi",
    "password": "123456",
    "role": "tester"
}
print(user["username"])

#--BÀI TẬP 2--#
state = {
    "email": "test@gmail.com",
    "password": "abc123",
     "status": "active"
}
print(state["email"])

#--------05--------------#
print(type(name))
print(type(age))
print(type(skills))
print(type(user))

#--BÀI TẬP NHỎ CHO BẠN--#
users = [
    {"name": "Phi", "email": "phi@example.com"},
    {"name": "An", "email": "an@example.com"},
    {"name": "Binh", "email": "binh@example.com"}
]
print(users[1]["email"])