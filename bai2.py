# Introduce your city
from guizero import App, Text, Box

# Main app
window = App(title = "Introduction to Nha Trang City")

# Title + the essay
header_box = Box(window, align = "top")

title = Text(header_box, text = "Introduction to Nha Trang City", color = "blue", size = 20, align = "top")

essay = Text(header_box, text = """
                                Thành phố Nha Trang nổi tiếng với những bãi biển dài, 
                                làn nước trong xanh và bờ cát trắng mịn. 
                                Nơi đây còn có nhiều danh lam thắng cảnh hấp dẫn như Hòn Mun, Hòn Tằm, Tháp Bà Ponagar và Vinpearl Land. Ẩm thực Nha Trang cũng rất phong phú, trong đó nổi bật là bún chả cá, nem Ninh Hòa, bánh căn và hải sản tươi sống. Với cảnh đẹp thiên nhiên hòa quyện cùng con người thân thiện, 
                                Nha Trang luôn là điểm đến hấp dẫn của du khách trong và ngoài nước.""")

# App display
window.display()