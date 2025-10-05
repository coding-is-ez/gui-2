# Create a GUI introducing yourself, including:
# Name, age, gender, current school, a pic
from guizero import App, Text, Picture

# Main app
window = App(title = "Introduction")

# Texts
# Name + age
name_age = Text(window, text = """
                            Tên: Hoàng Đức Bảo Lâm
                            Tuổi: 16""", width = "fill", align = "bottom", size = 20)

# Gender + current school
gender_school = Text(window, text = """
                            Giới tính: Nam
                            Trường: THPT Lý Tự Trọng""", width = "fill", align = "top", size = 20)

# Picture
picture = Picture(window, image = "maidass.jpg", align = "center")


# Run app
window.display()