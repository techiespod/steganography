import cv2

d = {}
c = {}

for i in range(257):
    d[chr(i)] = i
    c[i] = chr(i)

print("c : ", c)
print("d : ", d)

img = cv2.imread("D:/ass-1/2.jpg")

i = img.shape[0]
j = img.shape[1]
print("Height =", i, "and Width =", j)
data = input("Enter text to hide :  ")

nr = 0  # number of row
mc = 0  # number of column
z = 0
print(img[nr,mc])
l = int(len(data))
print("l = ", l)
for i in range(l):
    print(data)
    print("d[data[i]] : ",d[data[i]])
    print("img[nr, mc, z] : ",img[nr, mc, z])

    a = img[nr, mc, z] = d[data[i]]
    print("img[nr, mc, z] = d[data[i]] : ", a)
    print('---------------------------------')
    nr = nr + 1
    mc = mc + 1
    mc = (mc + 1) % 3


print('nr', nr)
print('mc', mc)
print('z', z)
cv2.imwrite("encrypted_img.jpg", img)
print("Data Hiding in Image completed successfully.")

n = 0
m = 0
z = 0
decrypt = ""
for i in range(l):
    decrypt += c[img[n, m, z]]
    n = n + 1
    m = m + 1
    m = (m + 1) % 3
print("Encrypted text was : ", decrypt)