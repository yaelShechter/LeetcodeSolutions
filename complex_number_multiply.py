def complex_number_multiply(num1: str, num2: str) -> str:
    real1, img1 = num1.replace("i", "").split("+")
    real2, img2 = num2.replace("i", "").split("+")
    real = str((int(real1) * int(real2)) - (int(img1) * int(img2)))
    img = str((int(real1) * int(img2)) + (int(real2) * int(img1)))
    return real + "+" + img + "i"
