def countChars(string1):
  my_dict = {}
  for i in string1:
    if (i in my_dict):
      my_dict[i] += 1
    else:
      my_dict[i] = 0
      my_dict[i] += 1
  return my_dict

print(countChars("adsgjklasdgjsadg"))