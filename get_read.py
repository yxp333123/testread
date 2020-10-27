import base64

with open("ddct2.txt", mode="rb") as f1:
    data = f1.read()

final_data = base64.b64encode(data)

with open("ddct264.txt", mode="wb") as f2:
    f2.write(final_data)


# with open("ddct164.txt", mode="rb") as f1:
#     data = f1.read()
#
# final_data = base64.b64decode(data)
#
# with open("ddctxxx.txt", mode="wb") as f2:
#     f2.write(final_data)

