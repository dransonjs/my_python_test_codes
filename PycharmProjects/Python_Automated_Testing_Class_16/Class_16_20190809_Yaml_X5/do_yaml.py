import yaml

f = open("./demo.yml", "r")
caps = yaml.load(f, Loader=yaml.FullLoader)
print(caps)
