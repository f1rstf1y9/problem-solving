while True:
  str = input()
  if str == "#":
    break
  replaced_str = str.replace("%", "%25").replace("$","%24").replace(" ", "%20").replace("!", "%21").replace("(", "%28").replace(")", "%29").replace("*", "%2a")
  print(replaced_str)
