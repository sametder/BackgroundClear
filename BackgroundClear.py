from rembg import remove as rm 

input_path = "ppw.png"
output_path = "output.png"

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        inputF = i.read()
        outputF = rm(inputF)
        o.write(outputF)
